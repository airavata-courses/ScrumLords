#!/usr/bin/env bash

echo "Fetching cluster credentials..."
gcloud container clusters get-credentials weather-forecast-cluster --zone us-central1-c --project weather-forecast-266119
echo -e "Done.\n\n"
pwd

echo "Installing jinja2, j2-client and jq"
pip install jinja2 j2cli
apt-get update && apt-get install -y jq
echo -e "Done.\n\n"

echo "Updating with latest commit tag..."
jq --arg LC "$LC" '. + { "manager_version_tag": $LC }' deployment/production_jinja.json > deployment/updated_production_jinja.json
echo -e "Done. Here's what the properties look like:\n"
cat ./deployment/updated_production_jinja.json
echo -e "\n\n"

echo "Creating services, deployments and horizontal pod autoscalers from jinja templates..."
j2 ./deployment/manager-service.yaml.jinja deployment/updated_production_jinja.json --format=json | kubectl apply -f -
j2 ./deployment/manager-deployment.yaml.jinja deployment/updated_production_jinja.json --format=json | kubectl apply -f -
j2 ./deployment/manager-hpa.yaml.jinja deployment/updated_production_jinja.json --format=json | kubectl apply -f -

echo -e "\n\nBuild complete."
