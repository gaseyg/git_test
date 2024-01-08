from requests import get, post, put, delete


# запрос к списку ресурсов
# print(get('http://localhost:8080/posts').json())

# добавление нового элемента в список
# print(post('http://localhost:8080/posts',
#            json={
#                'title': 'Title 1',
#                'text': 'Text 1',
#                'author_id': 1
#            }

#         ).json()
#     )

# запрос конкретного элемента 
print(get('http://localhost:8080/posts/1').json())