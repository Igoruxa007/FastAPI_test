"""create table

Revision ID: 727bd23a2343
Revises: 259a90f5cdc1
Create Date: 2025-01-29 07:40:59.092966

"""
from __future__ import annotations

from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '727bd23a2343'
down_revision: str | None = '259a90f5cdc1'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
