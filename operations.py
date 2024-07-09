import datetime
import sys
from read import store_details
# from main import main_display


# function which works on selling laptop and updating stock after selling
def sell_laptop():
    store_details()
    print("\n")
    laptops = store_details()
    user_name = str(input("Enter your Name:"))
    print("-----------------------------------------------------------------------------------------------------------------------")
    print('S.N''\t''Name of laptops''\t\t\t''Price ' '\t\t''quantity ''\t\t''processor ''\t\t''graphics ' )
    print("-----------------------------------------------------------------------------------------------------------------------")
    SN = 1
    for name, specs in laptops.items():
        print("-------------------------------------------------------------------------------------------------------------------")
        print(f"{SN}\t{name:<30}${specs['price']}\t\t{specs['quantity']}\t\t{specs['processor']}\t\t{specs['graphics']}")
        SN +=1
        
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("\n")
    laptop_name = input("Enter name  of laptop you want to buy: ")
    if laptop_name.upper() not in laptops:
        print(f" {laptop_name} is not avaliable in stock.")
        sell_laptop()

    laptop = laptops[laptop_name.upper()]
    success = False
    while True:
        try:
            quantity = int(input("Enter quantity you want to buy: "))
            if quantity < 0:
                print("Enter the valied number.")
            else:
                break
        except ValueError:
            print(f'only interger value for quantity  !!!!!!!')
            
    
    if laptop['quantity'] < quantity:
        print(f"Not aviable {laptop_name} quantity in stock to sell. PLease selected quantity from {quantity} units avliable to us.")
        return

    
    laptop['quantity'] -= quantity
    price_without_shipping= laptop['price'] * quantity
    shipping = str(input("DO you want your laptop shipped? (y/n)"))
    if(shipping.upper() == "Y"):
        shipping_cost = 150  
    else:
        shipping_cost = 0 
    total_shipping_cost = price_without_shipping + shipping_cost

    
        
    invoice = f"""
    --------------------------------------------------
    **************************************************
    --------------------------------------------------
    ________________FREE LAPTOP SHOP__________________
                   KATHMANDU,NEW ROAD
    --------------------------------------------------
    **************************************************
    ----------------BILLING FOR SELL------------------
    --------------------------------------------------
    DATE: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    CUSTOMER NAME: {user_name.upper()}  
    --------------------------------------------------
    PRODUCT:    {laptop_name.upper()}
    QUANTITY:   {quantity} 
    UNIT PRICE: ${laptop['price']:.2f}
    --------------------------------------------------
    SUBTOTAL:   ${total_shipping_cost:.2f}
    SHIPPING:   ${shipping_cost:.2f}
    TOTAL:      ${total_shipping_cost:.2f}
    --------------------------------------------------
    """
    print(invoice)
    with open(f"{user_name}_SALE_INVOICE.txt", "w") as file:
        file.write(invoice)



    #function to update the list after sell.
    with open('main.txt', 'w') as file:
        for laptop_name, laptop_details in laptops.items():
            name = laptop_name
            brand = laptop_details['brand']
            price = laptop_details['price']
            quantity = laptop_details['quantity']
            processor = laptop_details['processor']
            graphics = laptop_details['graphics']
            file.write(f"{laptop_name}, {brand}, ${price}, {quantity}, {processor}, {graphics}\n")
            
    # asking for repurchase laptop 
    more_ = input("Do you want to buy more? (y/n): ")
    if more_ == "y":
        sell_laptop()
    else:
        sys.exit()        
                
            # main_display()



#function to purchase laptop.
def purchase_laptop():
    store_details()
    print("\n")
    laptops = store_details()
    name_of_distributor = str(input("Enter name of customer: "))
    print("\n")
    print("----------------------------------------------")
    print('S.N''\t''Name of laptops''\t\t\t''Price ' )
    print("----------------------------------------------")
    SN = 1

    for name, specs in laptops.items():
        print(f"{SN}\t{name:<30}${specs['price']}")
        SN +=1
    laptop_name =  str(input("Enter name of laptop: "))
    if laptop_name.upper() not in laptops:
        print("Laptop is not avaliable in stock please enter again.!!!!!!!!")
        purchase_laptop()
        
    laptop = laptops[laptop_name.upper()]
    quantity = int(input("Enter number of laptops  :"))
    total_prize_without_VAT = laptop['price'] * quantity
    VAT_amount = (0.13 * total_prize_without_VAT)
    total_prize_with_VAT = VAT_amount + total_prize_without_VAT

    laptop['quantity'] += quantity

    invoice = f"""
    --------------------------------------------------
    DATE: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    --------------------------------------------------
                FREE LAPTOP SHOP
                KATHMANDU,NEW ROAD
    --------------------------------------------------
                BILLING FOR PURCHASE
    --------------------------------------------------
    CUSTOMER NAME: {name_of_distributor.upper()}  
    --------------------------------------------------
    LAPTOP:    {laptop_name.upper()}
    QUANTITY:   {quantity}
    UNIT PRICE: ${laptop['price']:.2f}
    --------------------------------------------------
    SUBTOTAL:   ${total_prize_without_VAT:.2f}
    SHIPPING:   ${VAT_amount:.2f}
    TOTAL:      ${total_prize_with_VAT:.2f}
    --------------------------------------------------
    THANK YOU FOR YOUR BUSINESS!
    We hope to see you again soon. 
    """
    print(invoice)
    print("Check txt file for Invoice.")
    with open(f"{name_of_distributor}_purchase_invoice.txt", "w") as file:
        file.write(invoice)

    #function which updates stock of laptop in txt file if laptop is purchased
    with open('main.txt', 'w') as file:
        for laptop_name, laptop_details in laptops.items():
            name = laptop_name
            brand = laptop_details['brand']
            price = laptop_details['price']
            quantity = laptop_details['quantity']
            processor = laptop_details['processor']
            graphics = laptop_details['graphics']
            file.write(f"{laptop_name}, {brand}, ${price}, {quantity}, {processor}, {graphics}\n")
            # main_display()

      # asking for repurchase laptop 
    more_ = input("Do you want to purchase_laptop more? (y/n): ")
    if more_ == "y":
        purchase_laptop()
    else:
        sys.exit()