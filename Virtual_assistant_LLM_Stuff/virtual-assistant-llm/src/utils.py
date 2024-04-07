# import pathway as pw
# import requests

# def send_discord_alerts(
#     message: pw.ColumnReference, discord_webhook_url: str
# ):
#     def send_discord_alert(key, row, time, is_addition):
#         if not is_addition:
#             return
#         alert_message = row[message.name]

#         payload = {'content': alert_message}
#         requests.post(
#             discord_webhook_url,
#             json=payload
#         ).raise_for_status()

#     pw.io.subscribe(message._table, send_discord_alert)


import requests

def send_discord_alerts(message: str, discord_webhook_url: str):
    try:
        payload = {'content': message}
        response = requests.post(discord_webhook_url, json=payload)
        response.raise_for_status()  # Check if request was successful
        print("Alert sent successfully")
    except Exception as e:
        print("Error sending alert:", e)