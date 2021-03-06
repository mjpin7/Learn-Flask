"""new fields in user model

Revision ID: 9adaaa75e4b4
Revises: ede686e1d146
Create Date: 2018-11-04 11:09:29.474675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9adaaa75e4b4'
down_revision = 'ede686e1d146'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('bio', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'bio')
    # ### end Alembic commands ###
