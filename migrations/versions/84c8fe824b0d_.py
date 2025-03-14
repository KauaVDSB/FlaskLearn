"""empty message

Revision ID: 84c8fe824b0d
Revises: f0b5817c9868
Create Date: 2025-03-05 15:31:31.116151

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84c8fe824b0d'
down_revision = 'f0b5817c9868'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=True),
    sa.Column('sobrenome', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.Column('data_cadastro', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('usuario')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nome', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('senha', sa.VARCHAR(), nullable=True),
    sa.Column('data_cadastro', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###
