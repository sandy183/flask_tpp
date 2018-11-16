"""empty message

Revision ID: 6fc5fa403c6e
Revises: 30c88f26707c
Create Date: 2018-11-15 15:49:29.231998

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6fc5fa403c6e'
down_revision = '30c88f26707c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('showname', sa.String(length=128), nullable=True),
    sa.Column('shownameen', sa.String(length=128), nullable=True),
    sa.Column('director', sa.String(length=64), nullable=True),
    sa.Column('leadingRole', sa.String(length=256), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('language', sa.String(length=64), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('screeningmodel', sa.String(length=32), nullable=True),
    sa.Column('openday', sa.Date(), nullable=True),
    sa.Column('backgroundpicture', sa.String(length=64), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('movie')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('showname', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('shownameen', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('director', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('leadingRole', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('type', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('country', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('language', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('duration', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('screeningmodel', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('openday', sa.DATE(), nullable=True),
    sa.Column('backgroundpicture', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('flag', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('isdelete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('movies')
    # ### end Alembic commands ###