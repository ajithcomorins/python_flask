"""empty message

Revision ID: 8f9f673b408f
Revises: 7de7c7a9ddcb
Create Date: 2023-04-13 14:54:48.132933

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8f9f673b408f'
down_revision = '7de7c7a9ddcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=mysql.VARCHAR(length=500),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=sa.String(),
               type_=mysql.VARCHAR(length=500),
               existing_nullable=True)

    # ### end Alembic commands ###
