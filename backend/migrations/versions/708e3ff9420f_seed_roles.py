"""seed roles

Revision ID: 708e3ff9420f
Revises: c46235da711c
Create Date: 2026-11-03 10:49:10.551967

"""
from datetime import datetime, timezone
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '708e3ff9420f'
down_revision = 'c46235da711c'
branch_labels = None
depends_on = None

roles = sa.table(
    "roles",
    sa.column("name", sa.String),
    sa.column("description", sa.String),
    sa.column("created_at", sa.DateTime),
    sa.column("updated_at", sa.DateTime),
)
SEED = (
    ("Customer", "Cliente de la tienda"),
    ("Admin", "Administrador del backoffice"),
)

def upgrade():
    conn = op.get_bind()
    now = datetime.now(timezone.utc).replace(tzinfo=None)
    for name, description in SEED:
        exists = conn.execute(
            sa.text("SELECT id FROM roles WHERE name = :name"),
            {"name": name},
        ).first()
        if exists is None:
            op.bulk_insert(roles, [{
                "name": name,
                "description": description,
                "created_at": now,
                "updated_at": now,
            }])
def downgrade():
    conn = op.get_bind()
    conn.execute(
        sa.text(
            "DELETE FROM roles WHERE name IN ('Customer', 'Admin')"
        )
    )