"""create table

Revision ID: 259a90f5cdc1
Revises: 4ff630764209
Create Date: 2025-01-29 07:38:26.437445

"""
from __future__ import annotations

from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '259a90f5cdc1'
down_revision: str | None = '4ff630764209'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
