import requests
import json

with open('sample_test_inputs.json') as f:
    test_cases = json.load(f)

for test in test_cases:
    response = requests.post("http://localhost:8000/classify-email", json=test)
    print(f"Input: {test}")
    print(f"Response: {response.json()}")
    print("-" * 50)
