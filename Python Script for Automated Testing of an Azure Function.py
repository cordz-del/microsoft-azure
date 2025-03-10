# test_azure_function.py
# This script automates testing of an Azure Function with an HTTP trigger.
# It sends a request to the deployed function and verifies the response, ensuring performance and correctness.

import requests

# Replace with your actual function app URL
function_url = "https://<your_function_app_name>.azurewebsites.net/api/HttpTrigger"
params = {"name": "Automation QA"}

response = requests.get(function_url, params=params)

assert response.status_code == 200, "Function did not return HTTP 200"
assert "Hello, Automation QA" in response.text, "Unexpected response from Azure Function"

print("Azure Function test passed successfully!")
