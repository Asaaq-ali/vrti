import requests

chat_id = "6218149232"
urlp = "https://t.me/ahmt7r"
url = f"https://api.telegram.org/bot5441497314:AAF5gj27qkohYLDfPxIBi6Jj_isAb7cnF3w/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
