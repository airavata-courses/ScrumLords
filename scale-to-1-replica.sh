#!/usr/bin/env bash

kubectl scale -n default deployment manager --replicas=1
kubectl scale -n default deployment session-manager --replicas=1
kubectl scale -n default deployment data-retrieval --replicas=1
kubectl scale -n default deployment model-execution --replicas=1
kubectl scale -n default deployment postprocessor --replicas=1
kubectl scale -n default deployment user-interface --replicas=1
kubectl scale -n default deployment user-server --replicas=1
