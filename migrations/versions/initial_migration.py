"""initial migration

Revision ID: initial
Revises: 
Create Date: 2023-10-05 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = 'initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create tables based on the current models
    op.create_table('dentist',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appointment',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('patient_id', sa.Integer(), nullable=False),
        sa.Column('dentist_id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('appointment')
    op.drop_table('patient')
    op.drop_table('dentist')
