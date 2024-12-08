import requests


site = 'https://jsonplaceholder.typicode.com/posts/'
post = 1  # You can choose a post
parameter = ''  # You can choose a parameter of a post like the title or body
response = requests.get(site + post if type(post) == str else site + str(post))
print(response.text if not parameter else response.json()[parameter])