import datetime
import sys


from operations import sell_laptop, purchase_laptop
from read import store_details

# function to display the distels of shop.
def disply_main():
    print("")
    print("----------------------------------------------------------")
    print("\t\t","---------FREE LATOP SHOP--------")
    print("----------------------------------------------------------")
    print(''''
          ############################################################
          _____________WELCOME TO FREE LAPTOP SHOP____________________
          -----------------KATHMANDU,NEW ROAD-------------------------
          ************************************************************

          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          THE LIST OF PRODUCTS WE HAVE
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
           ''')
    sell_laptop = store_details()
    main_display()
    print("\n")
    print("----------------------------------------------------------")




# function used to give option to user to go to sale,purchase or exit
def main_display():
    print("---------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------")
    print("\n")
    print("\t\t\t\t-----Welcome to free Laptop shop-----")
    print("""
        Enter What you want to do.
        1 : Sale
        2 : purchase
        3 : disply
        4 : Exit Store
        """)
    print("---------------------------------------------------------------------------------")
    print("----------------------------------------------------------------------------------")
    print("\n")
    option = input("Enter the options for forthwr process..: " )
    if option.upper() == "1":
        sell_laptop()

    elif option.upper() == "2":
        # buyFunction.purchase_laptop()
        purchase_laptop()

    elif option.upper() == "3":
        # display.disply_main()
        disply_main()

    elif option.upper() == "4":
        print("Thank you for your visit!")
        sys.exit()

    else:
        print("Enter valid input")

main_display()

