"""category table

Revision ID: 92e1acb54831
Revises: 75a3c4eaa514
Create Date: 2021-03-11 20:30:40.450785

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '92e1acb54831'
down_revision = '75a3c4eaa514'
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_table('category')
    # ### end Alembic commands ###
