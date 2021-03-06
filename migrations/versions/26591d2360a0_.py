"""empty message

Revision ID: 26591d2360a0
Revises: 7572c5195845
Create Date: 2020-01-28 14:09:54.544771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26591d2360a0'
down_revision = '7572c5195845'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('thread',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=55), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('thread')
    # ### end Alembic commands ###
