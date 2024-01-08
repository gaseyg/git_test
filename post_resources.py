from flask import jsonify, request
from flask_restful import Resource, reqparse, abort

from models import db, Post


# создаем объект парсера данных получаемых в запросе
parser = reqparse.RequestParser()
# передаем ему все поля в качестве аргументов
parser.add_argument('title', required=True)
parser.add_argument('text', required=True)


# создаем функцию проверки на ошибку 404
def abort_if_post_doesnt_exist(post_id):
    post = Post.query.get(post_id)
    if not post:
        abort(
            404,
            message = f"Post with id={post_id} doesn't exist"
        )

# класс обработки списка объектов 
class PostListResource(Resource):
    # метод получения списка публикаций
    def get(self):
        posts = Post.query.all()
        return jsonify(
           {
               'posts': [
                   post.to_dict(only=('text',))
                   for post in posts
               ]
           }
        )
    
    # метод добавления объекта публикации 
    def post(self):
        data1 = request.json
        post = Post(text=data1['text'])
        db.session.add(post)
        db.session.commit()
        return jsonify(
            {
                'posts': post.to_dict(only=('text'))
            }
        )


class PostResource(Resource):
    # Получение отдельной статьи 
    def get(self, post_id):
        abort_if_post_doesnt_exist(post_id)
        post = Post.query.get(post_id)
        return jsonify(
            {
                'posts': post.to_dict(only=('title', 'text'))
            }
        )
    