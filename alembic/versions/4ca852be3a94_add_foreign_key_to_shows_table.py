"""add foreign key to shows table

Revision ID: 4ca852be3a94
Revises: da981d97540e
Create Date: 2023-06-20 00:55:02.276833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ca852be3a94'
down_revision = 'da981d97540e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_foreign_key(
        'show_created_by_fk',
        source_table='shows',
        referent_table='users',
        local_cols=['created_by'],
        remote_cols=['username'],
        ondelete='CASCADE'
    )
    pass


def downgrade() -> None:
    op.drop_constraint(
        'show_created_by_fk',
        table_name='shows'
    )
    pass
