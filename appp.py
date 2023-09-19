import requests

# API URL
api_url = 'https://randomuser.me/api/'

#  parameters for the request
params = {
    'results': 1,  
    'format': 'json',  
}

# A HTTP GET request to the API
response = requests.get(api_url, params=params)


if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Print the entire response data
    print(data)
else:
    # Print an error message if the request failed
    print(f"Request failed with status code: {response.status_code}")
 