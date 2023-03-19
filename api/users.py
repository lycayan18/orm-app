from hashlib import md5

from flask import jsonify
from flask_restful import Resource, abort, reqparse

from data.db_session import create_session
from data.users import User


class UsersListResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("fio", required=True)
        self.parser.add_argument("email", required=True)
        self.parser.add_argument("password", required=True)

    def get(self):
        session = create_session()
        users = session.query(User).all()
        return jsonify({
            "users": list(map(User.to_dict, users))
            # list(map(lambda u: u.to_dict(), users))
        })

    def post(self):
        args = self.parser.parse_args()
        session = create_session()
        user = User(
            fio=args["fio"],
            email=args["email"]
        )
        user.set_password("12345")
        session.add(user)
        session.commit()
        resp = jsonify(user.to_dict())
        resp.status_code = 201
        return resp


class UsersResource(Resource):

    def get(self, user_id):
        session = create_session()
        user = session.query(User).get(user_id)
        if not user:
            abort(404, error=f"No user with id = {user_id}")
        return jsonify(user.to_dict())
