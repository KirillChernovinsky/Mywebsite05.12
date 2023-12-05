from datetime import datetime

from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, JSON, Table, Column


metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON)

)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),
)


products = Table(
    "products",
    metadata,
    Column("product_id", Integer, primary_key=True),
    Column("product_name", String, nullable=False),
    Column("product_image", String),    #здесь нужно будет хранить пути к изображениям
    Column('product_description', String, nullable=False)
)
