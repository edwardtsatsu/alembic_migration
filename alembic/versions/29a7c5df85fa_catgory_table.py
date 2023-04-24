"""catgory table

Revision ID: 29a7c5df85fa
Revises:
Create Date: 2023-04-24 14:50:37.939889

"""
from alembic import op
from sqlalchemy import INTEGER, TIMESTAMP, VARCHAR, Column, func



# revision identifiers, used by Alembic.
revision = '29a7c5df85fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
    'category',
        Column('id', INTEGER, primary_key=True, autoincrement=True),
        Column('name', VARCHAR(50), nullable=False),
        Column('description', VARCHAR(200)),
        Column('timestamp', TIMESTAMP, server_default=func.now())
    )


def downgrade() -> None:
    pass
