#!/usr/bin/env bash

kubectl delete svc manager-svc
kubectl delete svc session-manager-svc
kubectl delete svc data-retrieval-svc
kubectl delete svc model-execution-svc
echo -e "All services deleted.\n"

kubectl delete deployment manager
kubectl delete deployment session-manager
kubectl delete deployment data-retrieval
kubectl delete deployment model-execution
echo "All deployments and pods deleted."
