

from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    if request.args.get('hub.verify_token') == 'IGAANkkyx8GORBZAFA1U0EwQjdwOW90MjRKcnhNQmltc0lDcHhkb1NILWlZAQThPUUpxVjdjVXNQLXRram5vRjRjMWszVV9UbXFsYjR2ek53WldJZADdVNXlTeUVmUUY3UEpvakR4TldwclRYdUFnbkRRQVU2Y29xajVjcDV6cnFBZAwZDZD':
        return request.args.get('hub.challenge'), 200
    return "Invalid token", 403

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.get_json()
    # Handle the data (e.g., log it, process comments, etc.)
    print(data)
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
