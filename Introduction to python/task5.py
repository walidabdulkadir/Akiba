name = input("Customer name : ")
product = input("Product name : ")
price = int(input("Enter price : "))
quantity = int(input("How much do you want? : "))

total = (price * quantity)

print(f"""
        ========================================
                       RECEIPT
        ========================================

           Customer: {name}

        Product        Price       Qty
        ----------------------------------------
        {product}       {price} ETB     {quantity}

        Total:         {total} ETB

        Thank you for shopping!
        ========================================
      """)