import requests


site = 'https://jsonplaceholder.typicode.com/posts'
print('------------------------------get')
response_get = requests.get(url= site + '/1')
print(response_get.status_code)
print(response_get.reason)
print(response_get.text)
print('------------------------------post')
body = {
    'userId': 12,
    'title': 'test',
    'body': 'test'
}
headers = {
    'Content-Type': 'application/json; charset=utf-8'
}
response_post = requests.post(url= site, json= body, headers= headers)
print(response_post.status_code)
print(response_post.reason)
print(response_post.text)
print('------------------------------put')
data = {
    'title': 'test'
}
response_put = requests.put(url= site + '/1', data= data)
print(response_put.status_code)
print(response_put.reason)
print(response_put.text)
print('------------------------------patch')
data = {
    'title': 'test'
}
response_patch = requests.patch(url= site + '/1', data= data)
print(response_patch.status_code)
print(response_patch.reason)
print(response_patch.text)
print('------------------------------delete')
response_delete = requests.delete(url= site + '/1')
print(response_delete.status_code)
print(response_delete.reason)
print(response_delete.text)
