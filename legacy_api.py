from flask import jsonify, Blueprint

from data.db_session import create_session
from data.users import User


bp = Blueprint(
    "users_api",
    __name__
)


@bp.route("/api/v1/users")
def users_handler():
    session = create_session()
    users = session.query(User).all()
    return jsonify({
        "users": list(map(User.to_dict, users))
        # list(map(lambda u: u.to_dict(), users))
    })
