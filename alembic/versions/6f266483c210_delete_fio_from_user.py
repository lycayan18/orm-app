"""delete fio from User

Revision ID: 6f266483c210
Revises: 2bfce8909ac1
Create Date: 2023-03-15 18:32:47.246389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f266483c210'
down_revision = '2bfce8909ac1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'fio')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fio', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
