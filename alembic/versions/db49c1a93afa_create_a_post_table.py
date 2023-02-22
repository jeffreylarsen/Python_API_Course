"""create a post table

Revision ID: db49c1a93afa
Revises: 
Create Date: 2023-02-22 02:52:39.880626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db49c1a93afa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True
        ),
        sa.Column(
            'title',
            sa.String(),
            nullable=False,
        )
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
