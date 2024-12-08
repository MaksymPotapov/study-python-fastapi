import requests


site = 'https://jsonplaceholder.typicode.com/posts/'

data  = {
    'userName': 'test',
    'password': 'test_password'
}

try:
    response = requests.post(url= site, json= data)
    print(response.status_code)
    print(response.reason)
    print(response.text)
    print('----------------------------')
    print('The page contains:')
    for key in response.json().keys():
        print(f'--> {key}')
    with open(file= 'saves', mode= 'w') as file:
        file.write(str(response.text))
except requests.exceptions.RequestException as error:
    print(f'An error occurred: {error}')