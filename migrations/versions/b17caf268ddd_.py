"""empty message

Revision ID: b17caf268ddd
Revises: 
Create Date: 2020-06-03 09:53:33.417554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b17caf268ddd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender', sa.String(length=80), nullable=True),
    sa.Column('receiver', sa.String(), nullable=True),
    sa.Column('subject', sa.String(), nullable=True),
    sa.Column('msg_content', sa.String(), nullable=True),
    sa.Column('creation_date', sa.String(), nullable=True),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
