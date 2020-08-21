"""students table

Revision ID: 4824dbadaad2
Revises: ce693c4508bd
Create Date: 2020-08-21 00:16:37.791090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4824dbadaad2'
down_revision = 'ce693c4508bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.String(length=36), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_external_id'), 'student', ['external_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_student_external_id'), table_name='student')
    op.drop_table('student')
    # ### end Alembic commands ###
