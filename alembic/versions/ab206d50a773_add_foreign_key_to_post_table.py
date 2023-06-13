"""add foreign key to post table

Revision ID: ab206d50a773
Revises: e11ef976297f
Create Date: 2023-06-13 01:43:17.472373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab206d50a773'
down_revision = 'e11ef976297f'
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
