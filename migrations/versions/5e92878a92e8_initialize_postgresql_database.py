"""Initialize PostgreSQL database

Revision ID: 5e92878a92e8
Revises: 
Create Date: 2025-01-21 16:54:48.719614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e92878a92e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drink',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('glass_type', sa.String(length=50), nullable=True),
    sa.Column('ingredients', sa.Text(), nullable=True),
    sa.Column('alcohol_type', sa.String(length=50), nullable=True),
    sa.Column('taste', sa.String(length=50), nullable=True),
    sa.Column('instructions', sa.Text(), nullable=True),
    sa.Column('measurements', sa.Text(), nullable=True),
    sa.Column('volume_ml', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('drink')
    # ### end Alembic commands ###
