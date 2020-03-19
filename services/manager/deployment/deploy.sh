#!/usr/bin/env bash

echo "Fetching cluster credentials..."
gcloud container clusters get-credentials weather-forecast-cluster --zone us-central1-c --project "$PROJECT_ID"
echo -e "Done.\n\n"

echo "Installing jinja2, j2-client and jq"
pip install jinja2 j2cli
apt-get update && apt-get install -y jq
echo -e "Done.\n\n"

echo "Updating with latest commit tag..."
jq --arg LC "$LC" '. + { "manager_version_tag": $LC }' production_jinja.json > updated_production_jinja.json
echo -e "Done. Here's what the properties look like:\n"
cat updated_production_jinja.json
echo -e "\n\n"

echo "Creating services, deployments and horizontal pod autoscalers from jinja templates..."
j2 manager-service.yaml.jinja updated_production_jinja.json --format=json | kubectl apply -f -
j2 manager-deployment.yaml.jinja updated_production_jinja.json --format=json | kubectl apply -f -
j2 manager-hpa.yaml.jinja updated_production_jinja.json --format=json | kubectl apply -f -

echo -e "\n\nBuild complete."
