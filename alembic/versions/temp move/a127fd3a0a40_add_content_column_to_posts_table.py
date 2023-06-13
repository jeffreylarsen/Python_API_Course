"""add content column to posts table

Revision ID: a127fd3a0a40
Revises: db49c1a93afa
Create Date: 2023-02-22 03:24:43.875559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a127fd3a0a40'
down_revision = 'db49c1a93afa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column(
            'content',
            sa.String(),
            nullable=False
        )
    )
    pass


def downgrade() -> None:
    op.drop_column(
        'posts',
        'content'
    )
    pass
