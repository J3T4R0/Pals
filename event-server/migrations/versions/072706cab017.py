"""empty message

Revision ID: 072706cab017
Revises: 30ca70296a1c
Create Date: 2016-03-27 14:36:59.712765

"""

# revision identifiers, used by Alembic.
revision = '072706cab017'
down_revision = None

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('avatar', sa.String(length=600), nullable=True))
    op.add_column('user', sa.Column('tokens', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'avatar')
    op.drop_column('user', 'tokens')
    ### end Alembic commands ###
