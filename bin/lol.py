import requests

ACCESS_TOKEN = "IGAANkkyx8GORBZAFA1U0EwQjdwOW90MjRKcnhNQmltc0lDcHhkb1NILWlZAQThPUUpxVjdjVXNQLXRram5vRjRjMWszVV9UbXFsYjR2ek53WldJZADdVNXlTeUVmUUY3UEpvakR4TldwclRYdUFnbkRRQVU2Y29xajVjcDV6cnFBZAwZDZD"
MEDIA_ID = "18048534215482538"  # Replace with a valid media ID.

url = f"https://graph.facebook.com/v17.0/{MEDIA_ID}/comments"
params = {"access_token": ACCESS_TOKEN}

response = requests.get(url, params=params)
if response.status_code == 200:
    comments = response.json()
    print("Fetched Comments:")
    for comment in comments.get("data", []):
        print(f"User: {comment['from']['name']}, Comment: {comment['text']}")
else:
    print(f"Failed to fetch comments. Status Code: {response.status_code}, Error: {response.json()}")
