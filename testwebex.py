import requests

# Webex OAuth 2.0 Token URL
url = "https://webexapis.com/v1/access_token"

# Your Webex client ID, client secret, and redirect URI (replace with your values)
client_id = "C72041716155774afd8b7d3ee4946e3f4c19c97811a8b95733a987a2b7bea2f7d"
client_secret = "10336a065f88d510a6b2c30c30a141c961f29c61414cb561b9c33854d7b8f4df"
redirect_uri = "http://localhost:5000"

# The authorization code you received
authorization_code = "OGY0ZDdlZTEtOTYzOS00Mjc2LWIyMGYtMmM5MGY5ZWUyMDA0YzQ4ZWFhMDEtZDk4_P0A1_cfa89592-51e1-40cd-8755-9b04181bfbb6"

# Prepare the data for the POST request
data = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": redirect_uri,
    "client_id": client_id,
    "client_secret": client_secret
}

# Make the POST request to exchange the authorization code for an access token
response = requests.post(url, data=data)

# Check the response
if response.status_code == 200:
    # Parse the access token from the response
    access_token = response.json().get('access_token')
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to get access token: {response.status_code} - {response.text}")
