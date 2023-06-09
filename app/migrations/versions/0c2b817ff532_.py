"""empty message

Revision ID: 0c2b817ff532
Revises: 3fa52052d150
Create Date: 2023-04-06 12:28:55.407109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c2b817ff532'
down_revision = '3fa52052d150'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('emp_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('job_desc', sa.String(length=100), nullable=True),
    sa.Column('salary', sa.String(length=100), nullable=True),
    sa.Column('empolyee_id', sa.String(length=100), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('emp_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    # ### end Alembic commands ###
