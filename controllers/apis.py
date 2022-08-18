from models import db
from flask_restful import Resource
from flask import redirect, request
from models.posts import Posts
from flask_security import auth_required


def valid(x):
    for y in x:
        if y == None:
            return False
    return True


def GetAllPosts():
    d = Posts.query.all()
    return d


def GetPosts_by_User(user):
    d = Posts.query.filter_by(created_by=user).all()
    return d


def GetPosts_by_Id(post_id):
    d = Posts.query.filter_by(id=post_id).first()
    return d


class Posts_by_Users(Resource):

    # @auth_required("token")
    def get(self, id):
        g = GetPosts_by_User(id)
        # return g
        if g != []:
            d = []
            for x in g:
                d.append(x.GetDict())
            return d, 200
        else:
            return [], 200


class Posts_Others(Resource):

    # @auth_required("token")
    def get(self):
        g = GetAllPosts()
        # return g.GetDict(),200
        d = []
        for x in g:
            d.append(x.GetDict())
        return d, 200


class Posts_Fun(Resource):
    def get(self, post_id):
        g = GetPosts_by_Id(post_id)
        return g.GetDict(), 200

    def delete(self, post_id):
        g = GetPosts_by_Id(post_id)
        if g == None:
            return {"Error": "Not Found"}, 404
        else:
            db.session.delete(g)
            db.session.commit()
            return 200

    def put(self, post_id):
        g = GetPosts_by_Id(post_id)
        g.likes = g.likes + 1
        db.session.commit()
        return g.GetDict(), 200


# Function to create post
def create_Post(text="", likes=0, created_by=0):
    d = Posts(text=text, likes=likes, created_by=created_by)
    db.session.add(d)
    db.session.commit()
    return d


class Posts_Create(Resource):

    # @auth_required("token")
    def post(self):
        if request.content_type == "application/json":
            text = request.json["text"]
            likes = request.json["likes"]
            created_by = request.json["created_by"]
            if not (valid([text, likes, created_by])):
                return {"Error": "Incorrect Parameter"}, 400
            else:
                d = create_Post(text, likes, created_by)
                return d.GetDict(), 201
