"""add foriegn key to stories table

Revision ID: da981d97540e
Revises: 117453caa394
Create Date: 2023-06-13 16:45:04.089415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da981d97540e'
down_revision = '117453caa394'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'stories',
        sa.Column(
            'show_id',
            sa.Integer(),
            nullable=False
        )
    )
    op.create_foreign_key(
        'story_show_id_fk',
        source_table='stories',
        referent_table='shows',
        local_cols=['show_id'],
        remote_cols=['id'],
        ondelete='CASCADE'
    )
    op.create_foreign_key(
        'story_created_by_fk',
        source_table='stories',
        referent_table='users',
        local_cols=['created_by'],
        remote_cols=['username'],
        ondelete='CASCADE'
    )
    pass


def downgrade() -> None:

    op.drop_constraint(
        'story_created_by_fk',
        table_name='stories',
    )
    op.drop_constraint(
        'story_show_id_fk',
        table_name='stories',
    )
    op.drop_column('stories', 'show_id')
    pass
