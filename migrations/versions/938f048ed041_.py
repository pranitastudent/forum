"""empty message

Revision ID: 938f048ed041
Revises: 26591d2360a0
Create Date: 2020-01-28 14:52:02.906005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '938f048ed041'
down_revision = '26591d2360a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('thread', sa.Column('date_created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('thread', 'date_created')
    # ### end Alembic commands ###
