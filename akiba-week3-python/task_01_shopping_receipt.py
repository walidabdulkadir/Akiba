items = [
    {"name": "Notebook", "price": 1000, "quantity": 1},
    {"name": "Pen", "price": 1000, "quantity": 1}
]

def calculate_subtotal(items):
    for item in items:
        if item["price"] <= 0 or item["quantity"] <= 0:
            return "Invalid price or quantity"
            
    total = 0        
    for item in items:
            subtotal = item["price"]  * item["quantity"]
            total += subtotal   
    return total

def calculate_discount(items):
    price = calculate_subtotal(items)
    if price == "Invalid price or quantity":
            return "Invalid price or quantity"
    five_percent = (price * 5) / 100
    ten_percent = (price * 10) / 100
    if price >= 3000:
        final_price = price - ten_percent
        return final_price
    elif price >= 1000:
        final_price = price - five_percent
        return final_price
    else:
        return price

def calculate_tax(items):
    amount = calculate_discount(items)
    if amount == "Invalid price or quantity":
            return "Invalid price or quantity"
    tax_rate = (amount * 15) / 100
    final_price = amount + tax_rate
    return final_price ,tax_rate
   
    
    
def generate_receipt(items):
    total_price = calculate_subtotal(items)
    if total_price == "Invalid price or quantity":
        print("Invalid Price  or quantity")
        return "Invalid Price or quantity"
    
    final_price , tax_rate = calculate_tax(items)
    discount_price = calculate_discount(items)
    print(f"""
          Total purchased items price is {total_price}
          the discounted price : {discount_price}
          Tax rate is {tax_rate}
          
          Total final price : {final_price}
          """)

   
calculate_subtotal(items)
calculate_discount(items)
calculate_tax(items)
generate_receipt(items)

