"""initial migration

Revision ID: 5f24e582d7be
Revises: 
Create Date: 2023-03-08 15:26:46.387932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f24e582d7be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name_en', sa.String(length=255), nullable=False),
    sa.Column('name_ua', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cities')),
    sa.UniqueConstraint('name_en', name=op.f('uq_cities_name_en')),
    sa.UniqueConstraint('name_ua', name=op.f('uq_cities_name_ua'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('cities')
    # ### end Alembic commands ###