"""empty message

Revision ID: afa76758760e
Revises: ce0b8ccd98ce
Create Date: 2017-01-20 01:43:03.384268

"""

# revision identifiers, used by Alembic.
revision = 'afa76758760e'
down_revision = 'ce0b8ccd98ce'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('access_codes', sa.Column('access_url', sa.String(), nullable=True))
    op.add_column('discount_codes', sa.Column('discount_url', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('discount_codes', 'discount_url')
    op.drop_column('access_codes', 'access_url')
    ### end Alembic commands ###