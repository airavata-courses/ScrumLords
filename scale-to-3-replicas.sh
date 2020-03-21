#!/usr/bin/env bash

kubectl scale -n default deployment manager --replicas=3
kubectl scale -n default deployment session-manager --replicas=3
kubectl scale -n default deployment data-retrieval --replicas=3
kubectl scale -n default deployment model-execution --replicas=3
kubectl scale -n default deployment postprocessor --replicas=3
kubectl scale -n default deployment user-interface --replicas=3
kubectl scale -n default deployment user-server --replicas=3
