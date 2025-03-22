import requests
import json

BASE_URL = "http://localhost:8000"

def test_classify_email():
    with open("sample_test_inputs.json", "r") as file:
        test_cases = json.load(file)
    for i, test in enumerate(test_cases["test_cases"]):
        response = requests.post(f"{BASE_URL}/classify-email", json=test["input"])
        print(f"Test Case {i+1}:")
        print("Input:", test["input"])
        print("Expected:", test["expected_output"])
        print("Response:", response.json())
        print("-" * 50)

if __name__ == "__main__":
    test_classify_email()
