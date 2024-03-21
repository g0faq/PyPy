import requests

server, port, a, b = input(), int(input()), int(input()), int(input())

response = requests.get(f"{server}:{port}", params={"a": a, "b": b})
print(response.json(["result"]))
print(response.json()["check"])