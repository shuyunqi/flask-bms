"""many to many tags to books

Revision ID: ed3b83ef0feb
Revises: 0019923df1c9
Create Date: 2017-05-12 13:29:21.573580

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ed3b83ef0feb'
down_revision = '0019923df1c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column(u'tags', sa.Column('ebook_id', sa.Integer(), nullable=True))
    op.add_column(u'tags', sa.Column('tag_id', sa.Integer(), nullable=True))
    op.drop_index('name', table_name='tags')
    op.create_foreign_key(None, 'tags', 'tag', ['tag_id'], ['id'])
    op.create_foreign_key(None, 'tags', 'ebooks', ['ebook_id'], ['id'])
    op.drop_column(u'tags', 'id')
    op.drop_column(u'tags', 'description')
    op.drop_column(u'tags', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'tags', sa.Column('name', mysql.VARCHAR(collation=u'utf8mb4_unicode_ci', length=64), nullable=True))
    op.add_column(u'tags', sa.Column('description', mysql.TEXT(collation=u'utf8mb4_unicode_ci'), nullable=True))
    op.add_column(u'tags', sa.Column('id', mysql.INTEGER(display_width=11), nullable=False))
    op.drop_constraint(None, 'tags', type_='foreignkey')
    op.drop_constraint(None, 'tags', type_='foreignkey')
    op.create_index('name', 'tags', ['name'], unique=True)
    op.drop_column(u'tags', 'tag_id')
    op.drop_column(u'tags', 'ebook_id')
    op.drop_table('tag')
    # ### end Alembic commands ###