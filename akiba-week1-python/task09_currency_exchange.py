usd_dollar = float(input("Enter USD amout : "))
exchange_rate = 150

etb_birr = usd_dollar * exchange_rate

print(f"""
==============================
      CURRENCY EXCHANGE
==============================

USD Amount: {usd_dollar}

Exchange Rate: 1 USD = {exchange_rate} ETB

ETB Amount: {etb_birr} ETB
==============================

      """)
