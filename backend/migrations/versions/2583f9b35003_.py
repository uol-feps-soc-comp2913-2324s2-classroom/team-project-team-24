"""empty message

Revision ID: 2583f9b35003
Revises: 2aecffa86b5d
Create Date: 2024-05-01 12:59:11.456985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2583f9b35003'
down_revision = '2aecffa86b5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owner')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_owner', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_owner')

    op.create_table('owner',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=32), nullable=False),
    sa.Column('password', sa.VARCHAR(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###
