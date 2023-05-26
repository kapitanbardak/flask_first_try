import requests

url = 'http://localhost:80/api/questions'
data = {'questions_num': 5}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=data, headers=headers)
print(response.text)
