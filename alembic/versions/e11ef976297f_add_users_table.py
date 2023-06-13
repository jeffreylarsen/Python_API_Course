"""add users table

Revision ID: e11ef976297f
Revises: 472b7dd565b4
Create Date: 2023-06-13 01:17:01.469628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e11ef976297f'
down_revision = '472b7dd565b4'
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
            server_default="TRUE"
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
