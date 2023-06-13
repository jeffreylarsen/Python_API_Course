"""add last few columns to posts

Revision ID: 3e1520c0ea14
Revises: f5dd61deca02
Create Date: 2023-02-22 04:49:56.429335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e1520c0ea14'
down_revision = 'f5dd61deca02'
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


# make a new migration
# alembic revision --autogenerate -m "add last few columns to posts"