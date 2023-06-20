"""add stories table

Revision ID: 117453caa394
Revises: 5c4af2a0ea8e
Create Date: 2023-06-13 16:40:27.355137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '117453caa394'
down_revision = '5c4af2a0ea8e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "stories",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True
        ),
        sa.Column(
            "page_number",
            sa.String(),
            nullable=True
        ),
        sa.Column(
            'segment',
            sa.String(),
            nullable=True
        ),
        sa.Column(
            'writer',
            sa.String(),
            nullable=True
        ),
        sa.Column(
            'editor',
            sa.String(),
            nullable=True
        ),
        sa.Column(
            'source',
            sa.String(),
            nullable=True
        ),
        sa.Column(
            'script',
            sa.String(),
            nullable=True
        ),
        sa.Column(
            'mos_objects',
            sa.String(),
            server_default='[]'
        ),
        sa.Column(
            'last_modified_by',
            sa.String(),
            nullable=True
        ),
        sa.Column(
            'created_by',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'estimated_time',
            sa.String(),
            nullable=False,
            server_default='00:00:00'
        )
    )
    pass


def downgrade() -> None:
    op.drop_table('stories')
    pass
