from hashlib import md5

import sqlalchemy as sa
import sqlalchemy.orm as orm
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):

    __tablename__ = "users"
    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    first_name = sa.Column(sa.String)
    second_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String)
    email = sa.Column(sa.String)
    password = sa.Column(sa.String)

    # cars = orm.relationship("Car", secondary="car_user", backref="owners")

    def check_password(self, password):
        return md5(password.encode("utf-8")).hexdigest() == self.password

    def set_password(self, new_password):
        self.password = md5(new_password.encode("utf-8")).hexdigest()