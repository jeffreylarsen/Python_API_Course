"""add shows table

Revision ID: 5c4af2a0ea8e
Revises: , 0f836d44194b
Create Date: 2023-06-13 15:38:58.524561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c4af2a0ea8e'
down_revision = '0f836d44194b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'shows',
        sa.Column(
            'id',
            sa.Integer(),
            primary_key=True
        ),
        sa.Column(
            'show_name',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'show_air_date',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now() + sa.text("'1 DAY'"),
            nullable=False
        ),
        sa.Column(
            'show_end_date',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.func.now() + sa.text("'1 DAY 1 HOUR'"),
            nullable=False
        )
    )
    pass


def downgrade() -> None:
    op.drop_table('shows')
    pass
