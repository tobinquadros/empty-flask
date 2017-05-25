# empty-flask

Simple Python Flask setup with Prometheus & Grafana dashboards. Can be useful
for local testing.

## Setup

To start the app server standalone on http://localhost:5000/

```
make app
```

To start monitoring services & Grafana dashboards. Log in `user=admin`
`password=admin` at  http://localhost:3000/

```
make dashboards
```

To check that the app is up and running

```
make check
```

To clean up the Docker mess when you're done

```
make clean
```
