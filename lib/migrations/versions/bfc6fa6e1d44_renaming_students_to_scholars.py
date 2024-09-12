"""Renaming students to scholars

Revision ID: bfc6fa6e1d44
Revises: 791279dd0760
Create Date: 2024-09-12 18:13:41.173132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfc6fa6e1d44'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
