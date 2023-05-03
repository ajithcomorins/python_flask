"""empty message

Revision ID: b18794be9e47
Revises: a0756ed72436
Create Date: 2023-04-21 10:59:47.738107

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b18794be9e47'
down_revision = 'a0756ed72436'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=mysql.TEXT(),
               type_=sa.LargeBinary(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.LargeBinary(),
               type_=mysql.TEXT(),
               existing_nullable=True)

    # ### end Alembic commands ###