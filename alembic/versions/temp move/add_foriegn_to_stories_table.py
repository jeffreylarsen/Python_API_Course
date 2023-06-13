"""empty message

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
    pass


def downgrade() -> None:
    pass
