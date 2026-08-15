# import requests
# user_message="can you tell me about the black holes in the space in 3-4 lines?"
# request_message={"message":user_message}
# url="https://huzaifa45.app.n8n.cloud/webhook-test/65329c5b-ff4b-4fb3-b5a0-73ad0308a67e"
# response=requests.post(url, json=request_message)
# print(response.status_code)
# print(response.json()[0]["output"])


import requests

user_message = "can you tell me about the black holes in the space in 3-4 lines?"
request_message = {"message": user_message}

url = "https://huzaifa45.app.n8n.cloud/webhook-test/65329c5b-ff4b-4fb3-b5a0-73ad0308a67e"

response = requests.post(url, json=request_message)

print(response.status_code)
print(response.text)
print(response.json())