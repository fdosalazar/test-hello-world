# MS-HELLO-WORLD APP

> ms-hello-word is a simple python microservice
> This example has two resources:
> * GET / > return a response whit hello world and status code 200
> * GET /health > return a response with helm test and status code 200

### Kubernetes manifests

Are included in this repo, in directory k8s-manifests

### Helm templating

The charts included in this repo, create a deployment with 2 replicas, the number of replicas are in values.yaml, create a service with type ClusterIP, create a namespace and one ingress to allow traffic to the deployments pod.
