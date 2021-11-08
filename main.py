import requests


r = requests.post(
    'http://localhost:5000/classify',
    json={
        "text": ["junior machine learning engineer", "senior cloud architect"]
    }
)

print(r.json())





