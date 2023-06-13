"""add content column to posts table

Revision ID: 472b7dd565b4
Revises: db49c1a93afa
Create Date: 2023-06-13 00:43:00.567223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '472b7dd565b4'
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