"""create table

Revision ID: 4ff630764209
Revises: d23c58946ffe
Create Date: 2025-01-29 07:31:46.239174

"""
from __future__ import annotations

from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '4ff630764209'
down_revision: str | None = 'd23c58946ffe'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
