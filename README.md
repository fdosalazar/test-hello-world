# FIF / Test Kubernetes

Test Kubernetes for Falabella Financiero

This project was created in a macbook laptop using minikube like k8s local provider.

> ms-hello-word is a simple python microservice
> This example has two resources:
> *  GET /  return a response whit hello world and status code 200
> *  GET /health  return a response with helm test and status code 200



## Conditions
  
1.  [Docker](https://www.docker.com/get-started)
2.  [Minikube](https://kubernetes.io/es/docs/tasks/tools/install-minikube/)
3.  [Helm](https://helm.sh/docs/intro/install/)

## Flow

Deployment: It creates two replicaSet(pod) with one container in each pod. They have a default mapping port using the port 5000 like an exposed container port and targetPort.
Service: This service is ClusterIP type. It means that it's a default k8s service and allows to other pods to be able to access to the deployment created previuosly.
Ingress: This expose the ClusterIP service and allows the traffic to the microservice.

## Deploy
	
```sh
$ cd ms-hello-world
$ ./deploy.sh
```

*Date: 2020-04-02*