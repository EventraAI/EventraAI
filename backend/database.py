from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://username:password@localhost:5432/eventra_ai"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
metadata = MetaData()

subscriptions = Table(
    "subscriptions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("chat_id", String, nullable=False),
    Column("contract_address", String, nullable=False),
)

metadata.create_all(engine)

def add_subscription(chat_id, contract_address):
    with engine.connect() as conn:
        conn.execute(subscriptions.insert().values(chat_id=chat_id, contract_address=contract_address))

def remove_subscription(chat_id, contract_address):
    with engine.connect() as conn:
        conn.execute(subscriptions.delete().where(
            (subscriptions.c.chat_id == chat_id) & (subscriptions.c.contract_address == contract_address)))

def get_subscriptions(chat_id=None):
    with engine.connect() as conn:
        if chat_id:
            query = subscriptions.select().where(subscriptions.c.chat_id == chat_id)
        else:
            query = subscriptions.select()
        return conn.execute(query).fetchall()
