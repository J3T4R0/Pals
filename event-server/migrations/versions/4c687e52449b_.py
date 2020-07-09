"""empty message

Revision ID: 4c687e52449b
Revises: 81ac738516a0
Create Date: 2018-08-01 14:49:04.066424

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '4c687e52449b'
down_revision = '81ac738516a0'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # ### end Alembic commands ###
    custom_forms_table = sa.sql.table('custom_forms', sa.Column('field_identifier', sa.String()))
    op.execute(custom_forms_table.update()
               .where(custom_forms_table.c.field_identifier == 'firstName')
               .values({'field_identifier': 'firstname'}))
    op.execute(custom_forms_table.update()
               .where(custom_forms_table.c.field_identifier == 'lastName')
               .values({'field_identifier': 'lastname'}))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
