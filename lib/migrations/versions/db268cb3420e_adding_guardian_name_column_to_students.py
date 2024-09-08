"""Adding guardian_name column to students

Revision ID: db268cb3420e
Revises: d56f3ae06fe1
Create Date: 2024-09-08 06:07:02.249726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db268cb3420e'
down_revision = 'd56f3ae06fe1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # From which table then sqlalchemy syntax
    op.add_column('scholars', sa.Column('guardian_name', sa.String()))

def downgrade() -> None:
    op.drop_column('scholars', 'guardian_name')
