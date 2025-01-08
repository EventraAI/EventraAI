from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import sessionmaker

# Database Configuration
DATABASE_URL = "postgresql://username:password@localhost:5432/solana_event_watcher"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Define tables
metadata = MetaData()
subscriptions = Table(
    "subscriptions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("chat_id", String, nullable=False),
    Column("wallet_address", String, nullable=False),
)

# Create tables if they don't exist
metadata.create_all(engine)

# Helper function
def add_subscription(chat_id, wallet_address):
    with engine.connect() as conn:
        conn.execute(subscriptions.insert().values(chat_id=chat_id, wallet_address=wallet_address))
