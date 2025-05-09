import requests

print("Hello from Docker!")
response = requests.get("https://api.github.com")
print(response.status_code)