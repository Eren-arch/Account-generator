import requests

# Define API endpoint and key
api_url = "http://23.27.211.158:60335/api/accounts"
api_key = "QikiKekV0NsQDWud23KxSinxqNzFzz7GXWcwZWYlwWY"

# Set parameters for the request
params = {
    'api_key': api_key
}

# Send GET request to the API
response = requests.get(api_url, params=params)

# Check for successful response
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    print("Account Data:", data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}") 