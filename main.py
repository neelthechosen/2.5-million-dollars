from pycoingecko import CoinGeckoAPI
import time
import json
import os

cg = CoinGeckoAPI()
alerts = {}

def search_coin(query):
    coins = cg.get_coins_list()
    return [coin for coin in coins if query.lower() in coin['id'] or query.lower() in coin['symbol']]

def set_alert(coin_id, direction, target_price):
    if coin_id not in alerts:
        alerts[coin_id] = []
    alerts[coin_id].append({'direction': direction, 'price': target_price})
    print(f"✅ Alert set for {coin_id.upper()} when price goes {direction} ${target_price}")

def save_alerts(filename="alerts.json"):
    with open(filename, 'w') as f:
        json.dump(alerts, f)
    print("💾 Alerts saved.")

def load_alerts(filename="alerts.json"):
    global alerts
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            alerts = json.load(f)
        print("📂 Alerts loaded.")

def monitor_prices(interval_sec=30):
    print("🚀 Monitoring prices... Press Ctrl+C to stop.
")
    while True:
        for coin_id, alert_list in alerts.items():
            try:
                price = cg.get_price(ids=coin_id, vs_currencies='usd')[coin_id]['usd']
                print(f"{coin_id.upper()} - ${price}")
                for alert in alert_list:
                    direction = alert['direction']
                    target = alert['price']
                    if direction == 'above' and price >= target:
                        print(f"🔔 {coin_id.upper()} is ABOVE ${target} → Current: ${price}")
                    elif direction == 'below' and price <= target:
                        print(f"🔔 {coin_id.upper()} is BELOW ${target} → Current: ${price}")
            except Exception as e:
                print(f"⚠️ Error checking {coin_id}: {e}")
        time.sleep(interval_sec)

if __name__ == "__main__":
    print("Welcome to Crypto Price Alert Bot 🚨")
    print("Use functions like search_coin(), set_alert(), save_alerts(), load_alerts(), monitor_prices()")