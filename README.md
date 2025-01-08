# Solana Event Watcher with Telegram Bot

This project is an AI-based event watcher for the Solana blockchain that notifies users of blockchain events via a Telegram bot.

---

## Features
- Real-time tracking of Solana events (token transfers, contract calls, stake updates).
- AI-based filtering of events to prioritize actionable updates.
- Telegram bot for managing subscriptions and receiving notifications.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL database

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/solana-event-watcher.git
   cd solana-event-watcher
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the bot and backend:
   - Update `bot/config.py` with your Telegram bot token, Solana RPC URL, and database credentials.

4. Set up the database:
   ```bash
   psql -U postgres -c "CREATE DATABASE solana_event_watcher;"
   ```

---

## Usage

### Start the Telegram Bot
Run the Telegram bot:
```bash
python bot/bot.py
```

### Monitor Events
Run the event listener:
```bash
python backend/event_listener.py
```

---

## Commands
- `/start` – Display welcome message.
- `/subscribe <wallet>` – Subscribe to a wallet address.
- `/events` – Fetch recent events.

---

## Future Enhancements
- Add user-defined filters for notifications.
- Premium features for advanced filtering and historical data access.
