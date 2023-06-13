"""add stories table

Revision ID: b5469a85d6c6
Revises: 1258770f9ce5
Create Date: 2023-06-12 20:53:40.720512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = ''
down_revision = ''
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
            'mos_objects',
            sa.JSON(),
            server_default='[]'
        ),
        sa.Column(
            'last_modified_by',
            sa.String(),
            nullable=True
        ),
        sa.Column(
            'estimated_time',
            sa.DateTime(),
            nullable=True
        )
    )
    pass


def downgrade() -> None:
    op.drop_table('stories')
    pass