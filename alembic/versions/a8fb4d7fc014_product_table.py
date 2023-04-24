"""product table

Revision ID: a8fb4d7fc014
Revises: 29a7c5df85fa
Create Date: 2023-04-24 16:13:40.840856

"""
from alembic import op
from sqlalchemy import DECIMAL, INTEGER, TIMESTAMP, VARCHAR, Column, ForeignKey, func


# revision identifiers, used by Alembic.
revision = 'a8fb4d7fc014'
down_revision = '29a7c5df85fa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
    'product',
        Column('id', INTEGER, primary_key=True, autoincrement=True),
        Column('name', VARCHAR(50), nullable=False),
        Column('quantity', INTEGER),
        Column('price', DECIMAL(10, 1)),
        Column('category_id', INTEGER, ForeignKey('category.id'), nullable=False),
        Column('timestamp', TIMESTAMP, server_default=func.now())
    )


def downgrade() -> None:
    op.drop_table('product')
