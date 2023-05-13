print("Items in store:\n1.Biscuit - Rs.10/-\n2.Chocolate - Rs.5/-\n3.Ice Cream - Rs.15/-")
item=str(input("Enter the Item to Purchase: "))
quantity=int(input("Enter the Quantity: "))
if(item == 'Biscuit' or item == 'biscuit'):
    price = 10
elif(item == 'Chocolate' or item == 'chocolate'):
    price = 5
elif(item == 'Ice Cream' or item == 'ice cream' or item == 'Ice cream'):
    price = 15
else:
    print("Sorry",item,"is not Available. Try the above products.")
print("***********************BILL*************************")
print("****")
print("Item Name     Item Quantity     Item Price")
print("{}            {}             {}".format(item,quantity,price))
print("****************************************************")
print("******Total Amount to be paid:    ",quantity*price)
print("****************************************************")
print("****")