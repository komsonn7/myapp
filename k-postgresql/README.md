# K-POSTGRESQL

### Build and Pust to Hub Docker

```
docker build -t komsonn7/k-postgresql .
docker push komsonn7/k-postgresql
```

### Kubernetes Run

```
export POSTGRES_PASSWORD=$(kubectl get secret --namespace postgresql aqi-postgresql -o jsonpath="{.data.postgresql-password}" | base64 --decode)
envsubst < pod.yml | kubectl apply -f -
kubectl exec -it myapp -- python /app/create.py
kubectl exec -it myapp -- python /app/select.py
```

### Docker Run

```

docker pull komsonn7/k-postgresql:latest
docker run -dit -e HOST=<host> -e PORT=5432 -e USER=postgres -e PASSWORD=<password> -e DATABASE=postgres --name mypostgresql komsonn7/k-postgresql:latest
docker exec -it mypostgresql python /app/create.py
docker exec -it mypostgresql python /app/select.py

```