"""empty message

Revision ID: 1f74e82fba0b
Revises: 
Create Date: 2020-08-24 02:00:53.059354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f74e82fba0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contact_type_external_id'), 'contact_type', ['external_id'], unique=True)
    op.create_table('service_offered',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_service_offered_external_id'), 'service_offered', ['external_id'], unique=True)
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.String(length=36), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_external_id'), 'student', ['external_id'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.String(length=36), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_external_id'), 'user', ['external_id'], unique=True)
    op.create_table('classroom',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.String(length=36), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_classroom_external_id'), 'classroom', ['external_id'], unique=True)
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('external_id', sa.String(length=36), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('contact_date', sa.Date(), nullable=True),
    sa.Column('contact_start_time', sa.Time(), nullable=True),
    sa.Column('contact_end_time', sa.Time(), nullable=True),
    sa.Column('service_offered', sa.String(length=64), nullable=True),
    sa.Column('contact_type', sa.String(length=64), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contact_external_id'), 'contact', ['external_id'], unique=True)
    op.create_table('user_student',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('classroom_student',
    sa.Column('classroom_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classroom_id'], ['classroom.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('classroom_student')
    op.drop_table('user_student')
    op.drop_index(op.f('ix_contact_external_id'), table_name='contact')
    op.drop_table('contact')
    op.drop_index(op.f('ix_classroom_external_id'), table_name='classroom')
    op.drop_table('classroom')
    op.drop_index(op.f('ix_user_external_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_student_external_id'), table_name='student')
    op.drop_table('student')
    op.drop_index(op.f('ix_service_offered_external_id'), table_name='service_offered')
    op.drop_table('service_offered')
    op.drop_index(op.f('ix_contact_type_external_id'), table_name='contact_type')
    op.drop_table('contact_type')
    # ### end Alembic commands ###
