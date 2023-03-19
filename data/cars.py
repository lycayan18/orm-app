import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase
from .users import User


class Car(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "cars"
    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    model = sa.Column(sa.String)
    year = sa.Column(sa.Integer)


car_user = sa.Table(
    "car_user",
    SqlAlchemyBase.metadata,
    sa.Column("cars", sa.Integer, sa.ForeignKey(Car.id)),
    sa.Column("users", sa.Integer, sa.ForeignKey(User.id))
)
