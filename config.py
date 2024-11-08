import os

# Trading parameters
TARGET_PROFIT = float(
    os.getenv("TARGET_PROFIT", 0.001))  # Default target profit if not provided via environment variable

# Fetch the trading symbol dynamically from the environment or use a default one
SYMBOL = os.getenv("SYMBOL", "BTCUSDT")  # Default symbol is 'BTCUSDT', but can be overridden by an environment variable

ORDER_SIZE = 0.0001  # Order size (adjust as needed)
ACCOUNTTYPE = "UNIFIED"  # Account type for Bybit

# API credentials (ensure you are not sharing sensitive data publicly)
BYBIT_API_KEY = 'NRJMo0hxaeWkoxhCBX'
BYBIT_API_SECRET = 'vMemeMGETeQHPpuHM03u2hMpcv4f6D8iUrUi'

# Telegram bot configuration
TELEGRAM_TOKEN = '6901257804:AAEAZ2dP399pa75NLqHexhr7rhIhO0wYBuc'
TELEGRAM_CHAT_ID = '1380803567'  # You may use the user or group chat ID where messages will be sent

# Bybit API URL (Testnet or Live)
API_URL = 'https://api-testnet.bybit.com'