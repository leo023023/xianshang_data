"""empty message

Revision ID: 0ffbc6504f29
Revises: 4d73af70b817
Create Date: 2020-09-24 11:40:54.788553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ffbc6504f29'
down_revision = '4d73af70b817'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cishu',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cishu', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article_zan',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('zaiyao', sa.Text(), nullable=False),
    sa.Column('lanmu_id', sa.INTEGER(), nullable=True),
    sa.Column('author_name', sa.String(length=100), nullable=False),
    sa.Column('article_yuedu', sa.String(length=100), nullable=False),
    sa.Column('article_time', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['lanmu_id'], ['lanmu.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'article', sa.Column('zaiyao', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'article', 'zaiyao')
    op.drop_table('article_zan')
    op.drop_table('cishu')
    # ### end Alembic commands ###
