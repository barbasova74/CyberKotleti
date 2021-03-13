"""added relation user - work

Revision ID: f63c1276bd77
Revises: e5e1b5fb3362
Create Date: 2021-03-13 21:55:36.517268

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f63c1276bd77'
down_revision = 'e5e1b5fb3362'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('association',
                    sa.Column('question', sa.Integer(), nullable=True),
                    sa.Column('category', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['category'], ['category.id'], ),
                    sa.ForeignKeyConstraint(['question'], ['questions.id'], )
                    )
    op.add_column('questions', sa.Column('author', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'questions', 'users', ['author'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.drop_column('questions', 'author')
    op.drop_table('association')
    op.drop_table('category')
    # ### end Alembic commands ###