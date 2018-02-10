"""mod ugw_password

Revision ID: 73d3de12159a
Revises: 238ce21d1fb4
Create Date: 2017-12-04 21:47:12.657698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73d3de12159a'
down_revision = '238ce21d1fb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ecns280s', sa.Column('ugw_password', sa.String(length=64), nullable=True))
    op.drop_column('ecns280s', 'ugw_ip_password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ecns280s', sa.Column('ugw_ip_password', sa.VARCHAR(length=64), nullable=True))
    op.drop_column('ecns280s', 'ugw_password')
    # ### end Alembic commands ###