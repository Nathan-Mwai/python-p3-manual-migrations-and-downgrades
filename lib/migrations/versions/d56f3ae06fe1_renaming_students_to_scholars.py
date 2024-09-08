"""Renaming students to scholars

Revision ID: d56f3ae06fe1
Revises: 791279dd0760
Create Date: 2024-09-08 05:56:50.780734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd56f3ae06fe1'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    
