# K-POSTGRESQL

### Build and Pust to Hub Docker

```
docker build -t komsonn7/k-postgresql .
docker push komsonn7/k-postgresql
```

### Docker Run

```
docker run -d -t -i -e HOST=<host> -e PORT=5432 -e USER=postgres -e PASSWORD=<password> -e DATABASE=postgres --name mypostgresql k-postgresql
```

### Kubernetes Run

```
kubectl apply -f pod.yml
```