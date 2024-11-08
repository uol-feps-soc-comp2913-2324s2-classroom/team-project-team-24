"""start-date

Revision ID: 2aecffa86b5d
Revises: 0cc992202893
Create Date: 2024-04-29 18:57:16.323964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2aecffa86b5d'
down_revision = '0cc992202893'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('membership_start_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('membership_start_date')

    # ### end Alembic commands ###
