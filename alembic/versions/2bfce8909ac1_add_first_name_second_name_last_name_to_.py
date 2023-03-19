"""add first_name, second_name, last_name to User

Revision ID: 2bfce8909ac1
Revises: 
Create Date: 2023-03-15 18:24:08.508582

"""
from alembic import op
import sqlalchemy as sa

from data.db_session import create_session
from data.users import User

# revision identifiers, used by Alembic.
revision = '2bfce8909ac1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('second_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(), nullable=True))
    # ### end Alembic commands ###
    session = create_session()
    users = session.query(User).all()
    for u in users:
        u.last_name, u.first_name, u.second_name = u.fio.split(" ")
        session.add(u)
    session.commit()


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'second_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###
    session = create_session()
    users = session.query(User).all()
    for u in users:
        u.fio = " ".join([u.last_name, u.first_name, u.second_name])
        session.add(u)
    session.commit()
