# 🪙 Crypto Price Alert Bot

A simple Python bot that tracks cryptocurrency prices using the CoinGecko API and alerts you when prices cross your set targets.

## 📦 Features
- Search any coin by name or symbol
- Set target price alerts (above/below)
- Save/load your alerts
- Monitor prices and get notified in terminal

## 🚀 How to Use

### 1. Install Requirements
```
pip install -r requirements.txt
```

### 2. Run the Bot
```
python main.py
```

Then use the following inside the script:
```python
search_coin("eth")
set_alert("ethereum", "above", 3200)
monitor_prices(30)
```

## 📂 Save & Load Alerts
```python
save_alerts()
load_alerts()
```

---
Built by Neel ⚡