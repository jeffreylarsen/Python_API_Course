"""add shows table

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
    op.add_column(
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
            server_default=sa.text('Now() INTERVAl 1 DAY'),
            nullable=False
        ),
        sa.Column(
            'show_end_date',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text('Now() INTERVAl 1 DAY 1 HOUR'),
            nullable=False
        )
    )
    pass


def downgrade() -> None:
    op.drop_table('shows')
    pass
