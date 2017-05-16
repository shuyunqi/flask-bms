"""add status_id

Revision ID: e5c3a4f4f9ca
Revises: f69451c1ae3f
Create Date: 2017-05-16 15:51:11.590777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5c3a4f4f9ca'
down_revision = 'f69451c1ae3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('status_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'books', 'book_status', ['status_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_column('books', 'status_id')
    # ### end Alembic commands ###