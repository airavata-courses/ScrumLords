#!/usr/bin/env bash

kubectl delete svc manager-svc
kubectl delete svc session-manager-svc
kubectl delete svc data-retrieval-svc
kubectl delete svc model-execution-svc
kubectl delete svc postprocessor-svc
kubectl delete svc user-interface-svc
kubectl delete svc user-server-svc
echo -e "All services deleted.\n"

kubectl delete deployment manager
kubectl delete deployment session-manager
kubectl delete deployment data-retrieval
kubectl delete deployment model-execution
kubectl delete deployment postprocessor
kubectl delete deployment user-interface
kubectl delete deployment user-server
echo "All deployments and pods deleted."
