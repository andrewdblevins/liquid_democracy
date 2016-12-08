curl -X POST -H "application/json" -d '{"name":"hyatt"}' http://127.0.0.1:5000/users
curl -X POST -H "application/json" -d '{"name":"andrew"}' http://127.0.0.1:5000/users
curl -X POST -H "application/json" -d '{"name":"bob"}' http://127.0.0.1:5000/users
curl -X POST -H "application/json" -d '{"name":"charlotte"}' http://127.0.0.1:5000/users
curl -X POST -H "application/json" -d '{"name":"david"}' http://127.0.0.1:5000/users
curl -X POST -H "application/json" -d '{"source":{"name":"hyatt"},"target":{"name":"andrew"}}' http://127.0.0.1:5000/connections
curl -X POST -H "application/json" -d '{"source":{"name":"bob"},"target":{"name":"andrew"}}' http://127.0.0.1:5000/connections
curl -X POST -H "application/json" -d '{"source":{"name":"andrew"},"target":{"name":"charlotte"}}' http://127.0.0.1:5000/connections
curl -X POST -H "application/json" -d '{"source":{"name":"bob"},"target":{"name":"charlotte"}}' http://127.0.0.1:5000/connections
curl -X POST -H "application/json" -d '{"source":{"name":"david"},"target":{"name":"hyatt"}}' http://127.0.0.1:5000/connections
curl http://127.0.0.1:5000/connections
curl http://127.0.0.1:5000/trust
