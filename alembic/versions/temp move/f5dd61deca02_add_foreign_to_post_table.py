"""add foreign to post table

Revision ID: f5dd61deca02
Revises: f17f18a6fdbc
Create Date: 2023-02-22 04:31:51.963063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5dd61deca02'
down_revision = 'f17f18a6fdbc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column(
            'owner_id',
            sa.Integer(),
            nullable=False
        )
    )
    op.create_foreign_key(
        'post_user_fk',
        source_table='posts',
        referent_table='users',
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete='CASCADE'
    )
    pass


def downgrade() -> None:
    op.drop_constraint(
        'post_user_fk', 
        table_name='posts'
    )
    op.drop_column('posts', 'owner_id')
    pass
