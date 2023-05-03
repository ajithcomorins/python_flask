"""empty message

Revision ID: 90eb1beb331e
Revises: 
Create Date: 2023-04-05 09:45:37.529773

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '90eb1beb331e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(length=100), nullable=True),
    sa.Column('datatime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('add_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('add_user',
    sa.Column('id', mysql.INTEGER(display_width=10), autoincrement=True, nullable=False),
    sa.Column('name', mysql.TEXT(), nullable=True),
    sa.Column('email', mysql.TEXT(), nullable=True),
    sa.Column('time', mysql.TIMESTAMP(), server_default=sa.text('current_timestamp() ON UPDATE current_timestamp()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('todo')
    # ### end Alembic commands ###
