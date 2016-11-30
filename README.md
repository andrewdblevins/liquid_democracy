# liquid_democracy
slack bot for trust rank

```python
run python app.py
```
```bash
curl -X POST -H "application/json" -d '{"name":"hyatt"}' http://127.0.0.1:5000/users
curl -X POST -H "application/json" -d '{"name":"andrew"}' http://127.0.0.1:5000/users
curl -X POST -H "application/json" -d '[{"name":"hyatt"},{"name":"andrew"}]' http://127.0.0.1:5000/connections
curl http://127.0.0.1:5000/connections
curl http://127.0.0.1:5000/trust
```
