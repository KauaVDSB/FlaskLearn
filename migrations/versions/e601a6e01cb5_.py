"""empty message

Revision ID: e601a6e01cb5
Revises: 84c8fe824b0d
Create Date: 2025-03-05 15:32:31.858223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e601a6e01cb5'
down_revision = '84c8fe824b0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sobrenome_user', sa.String(), nullable=True))
        batch_op.drop_column('sobrenome')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sobrenome', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('sobrenome_user')

    # ### end Alembic commands ###
