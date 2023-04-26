"""add users table

Revision ID: f17f18a6fdbc
Revises: a127fd3a0a40
Create Date: 2023-02-22 04:19:58.771419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f17f18a6fdbc'
down_revision = 'a127fd3a0a40'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column(
            'id',
            sa.Integer(),
            primary_key=True,
            nullable=False
        ),
        sa.Column(
            'username',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'email',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'password',
            sa.String(),
            nullable=False
        ),
        sa.Column(
            'created',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text('Now()'),
            nullable=False
        ),
        sa.Column(
            'member',
            sa.Boolean(),
            nullable=False,
            server_default=int(0)
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
