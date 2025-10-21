from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

BASE_URL = "https://api.intra.42.fr"
UID = os.getenv("42_APP_UID")
SECRET = os.getenv("42_APP_SECRET")

# dev
creds = {'access_token': '67ab3df089a5a6556488124f42ac6d42f42b2e4b7dab5d5f87221a5742869645', 'token_type': 'bearer', 'expires_in': 7188, 'scope': 'public', 'created_at': 1758130687, 'secret_valid_until': 1760546735}


def get_access_token():
	url = f"{BASE_URL}/oauth/token?grant_type=client_credentials&client_id={UID}&client_secret={SECRET}"
	req = requests.post(
		url
	)
	print(req.json())
	print(req)

def get_events(campus_id: str = '1'):
	url = f"{BASE_URL}/v2/campus/{campus_id}/events"
	headers = {
		"Authorization": f"Bearer {creds.get("access_token")}"
	}
	req = requests.get(url, headers=headers)
	data = req.json()
	with open("./data.json", 'w') as file:
		json.dump(data, file, indent=4)
	print(req)


if __name__ == "__main__":
	get_events('1')