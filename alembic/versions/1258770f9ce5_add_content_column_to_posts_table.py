"""add content column to posts table

Revision ID: 1258770f9ce5
Revises: db49c1a93afa
Create Date: 2023-02-22 03:16:25.065438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1258770f9ce5'
down_revision = 'db49c1a93afa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
            primary_key=True
        ),
        sa.Column(
            'title',
            sa.String(),
            nullable=False,
        ),
        sa.Column(
            'content',
            sa.String(),
            nullable=False
        )
    )
    pass


def downgrade() -> None:
    pass
