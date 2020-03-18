#!/usr/bin/env bash

echo "Creating services, deployments and horizontal pod autoscalers from jinja templates for manager microservice..."
j2 services/manager/deployment/manager-service.yaml.jinja services/manager/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/manager/deployment/manager-deployment.yaml.jinja services/manager/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/manager/deployment/manager-hpa.yaml.jinja services/manager/deployment/production_jinja.json --format=json | kubectl apply -f -


echo -e "\n\nCreating services, deployments and horizontal pod autoscalers from jinja templates for session_manager microservice..."
j2 services/session_manager/deployment/session-manager-service.yaml.jinja services/session_manager/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/session_manager/deployment/session-manager-deployment.yaml.jinja services/session_manager/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/session_manager/deployment/session-manager-hpa.yaml.jinja services/session_manager/deployment/production_jinja.json --format=json | kubectl apply -f -


echo -e "\n\nCreating services, deployments and horizontal pod autoscalers from jinja templates for weather_data_retrieval microservice..."
j2 services/weather_data_retrieval/deployment/weather-data-retrieval-service.yaml.jinja services/weather_data_retrieval/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/weather_data_retrieval/deployment/weather-data-retrieval-deployment.yaml.jinja services/weather_data_retrieval/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/weather_data_retrieval/deployment/weather-data-retrieval-hpa.yaml.jinja services/weather_data_retrieval/deployment/production_jinja.json --format=json | kubectl apply -f -


echo -e "\n\nCreating services, deployments and horizontal pod autoscalers from jinja templates for model_execution microservice..."
j2 services/model_execution/deployment/model-execution-service.yaml.jinja services/model_execution/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/model_execution/deployment/model-execution-deployment.yaml.jinja services/model_execution/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/model_execution/deployment/model-execution-hpa.yaml.jinja services/model_execution/deployment/production_jinja.json --format=json | kubectl apply -f -


echo -e "\n\nCreating services, deployments and horizontal pod autoscalers from jinja templates for postprocessor microservice..."
j2 services/postprocessor/deployment/postprocessor-service.yaml.jinja services/postprocessor/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/postprocessor/deployment/postprocessor-deployment.yaml.jinja services/postprocessor/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/postprocessor/deployment/postprocessor-hpa.yaml.jinja services/postprocessor/deployment/production_jinja.json --format=json | kubectl apply -f -


echo -e "\n\nCreating services, deployments and horizontal pod autoscalers from jinja templates for user_server microservice..."
j2 services/user_server/deployment/user-server-service.yaml.jinja services/user_server/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/user_server/deployment/user-server-deployment.yaml.jinja services/user_server/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/user_server/deployment/user-server-hpa.yaml.jinja services/user_server/deployment/production_jinja.json --format=json | kubectl apply -f -


echo -e "\n\nCreating services, deployments and horizontal pod autoscalers from jinja templates for user_server microservice..."
j2 services/user_interface/deployment/user-interface-service.yaml.jinja services/user_interface/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/user_interface/deployment/user-interface-deployment.yaml.jinja services/user_interface/deployment/production_jinja.json --format=json | kubectl apply -f -
j2 services/user_interface/deployment/user-interface-hpa.yaml.jinja services/user_interface/deployment/production_jinja.json --format=json | kubectl apply -f -
