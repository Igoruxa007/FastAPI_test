"""create account table

Revision ID: d23c58946ffe
Revises: 18e97a8f5a65
Create Date: 2025-01-29 07:26:29.755705

"""
from __future__ import annotations

from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'd23c58946ffe'
down_revision: str | None = '18e97a8f5a65'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
