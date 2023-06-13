"""add last few columns to posts

Revision ID: d8dff0bd5e73
Revises: ab206d50a773
Create Date: 2023-06-13 15:09:59.244020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8dff0bd5e73'
down_revision = 'ab206d50a773'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column(
            'published',
            sa.Boolean(),
            nullable=False,
            server_default="TRUE"
        )
    )
    op.add_column(
        'posts',
        sa.Column(
            'created',
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text('NOW()')
        )
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created')
    pass
