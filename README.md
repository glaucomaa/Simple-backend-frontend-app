# Random number generator

a backend-frontend app using Kubernetes. 

- Backend: application that listens to a port and sends some response if a message comes there. Must be replicated.

- Frontend: application that sends incoming requests to the backend.


### Requirements

- Docker
- Kubectl
- Minikube

### Steps

Step 0: Clone the repo

```bash
git clone https://github.com/glaucomaa/Simple-backend-frontend-app.git
```

Step 1: Navigate to the cloned repo:

```bash
cd Simple-backend-frontend-app
```

Step 2: Start Kubernetes cluster:

```bash
minikube start && \
kubectl create namespace click && \
kubectl config set-context --current --namespace=click
```

Step 3: Build docker images

```bash
eval $(minikube docker-env) && \ 
docker build -t frontend:latest ./frontend && \
docker build -t backend:latest ./backend
```

Step 4: Deploy the application:

```bash
kubectl apply -f k8s
```

Step 5: Verify the status of all pods::

```bash
kubectl get pods
```

Step 6: obtain the URL for frontend:

```bash
minikube service frontend-service -n click --url
```

Alternatively, open URL in the default browser:

```bash
minikube service frontend-service -n click 
```

### Cleanup

To remove all resources:

```bash
kubectl -n click delete all --all
```
To shut down Minikube and remove it entirely:

```bash
minikube stop && \
minikube delete
```

#### Logging

You can access the logs via the `kubectl logs POD-NAME` command.
To obtain the POD-NAME, you can utilize the `kubectl get pods` command.


