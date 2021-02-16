# restro menu

# declare variable for calculating bill
bill = 0

data = []

# infinite loop 
while True:
    print("**********Menu***********")
    print("1 for Veg")
    print("2 for Non-Veg")
    print("3 for Exit")
    ch = input("Enter your choice => ")
    if ch == "1":
        while True:
            print("**********Veg***********")
            print("1 for Starter")
            print("2 for Main Course")
            print("3 for Breakfast")
            print("4 for Dessert")
            print("5 for Exit")
            ch = input("Enter your choice => ")
            if ch == "1":
                while True:
                    print("**********Starter***********")
                    print("1 for Chrispy    : Rs.150/- ")
                    print("2 for Manchurian : Rs.160/- ")
                    print("3 for Fried Corn : Rs.140/- ")
                    print("4 for Soup       : Rs.120/- ")
                    print("5 for Exit")
                    ch = input("Enter your choice => ")
                    if ch == "1":
                        print("**********Chrispy***********")
                        print("Cost of Chrispy will be Rs.150/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Chrispy        ',qty,150]
                        data.append(item)
                        bill = (150)*qty + bill
                    elif ch == "2":
                        print("**********Manchurian***********")
                        print("Cost of Manchurian will be Rs.160/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Manchurian     ',qty,160]
                        data.append(item)
                        bill = (160)*qty + bill
                    elif ch == '3':
                        print("**********Fried Corn***********")
                        print("Cost of Fried Corn will be Rs.140/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Fried Corn     ',qty,140]
                        data.append(item)
                        bill = (140)*qty + bill
                    elif ch == "4":
                        print("**********Soup***********")
                        print("Cost of Soup will be Rs.120/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Soup           ',qty,120]
                        data.append(item)
                        bill = (120)*qty + bill
                    elif ch == '5':
                        break
            elif ch == "2":
                while True:
                    print("**********Main Course***********")
                    print("1 for Paneer Kadai : Rs.250/- ")
                    print("2 for Kolhapuri    : Rs.270/- ")
                    print("3 for Shev Bhaji   : Rs.210/- ")
                    print("4 for Palak Paneer : Rs.230/- ")
                    print("5 for Exit")
                    ch = input("Enter your choice => ")
                    if ch == "1":
                        print("**********Paneer Kadai***********")
                        print("Cost of Paneer Kadai will be Rs.250/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Paneer Kadai   ',qty,250]
                        data.append(item)
                        bill = (250)*qty + bill
                    elif ch == "2":
                        print("**********Kolhapuri***********")
                        print("Cost of Kolhapuri will be Rs.270/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Kolhapuri      ',qty,270]
                        data.append(item)
                        bill = (270)*qty + bill
                    elif ch == '3':
                        print("**********Shev Bhaji***********")
                        print("Cost of Shev Bhaji will be Rs.210/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Shev Bhaji     ',qty,210]
                        data.append(item)
                        bill = (210)*qty + bill
                    elif ch == "4":
                        print("**********Palak Paneer***********")
                        print("Cost of Palak Paneer will be Rs.230/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Palak Paneer   ',qty,230]
                        data.append(item)
                        bill = (230)*qty + bill
                    elif ch == '5':
                        break
            elif ch == '3':
                while True:
                    print("**********Breakfast***********")
                    print("1 for Idli    : Rs.40/- ")
                    print("2 for Dosa    : Rs.55/- ")
                    print("3 for Uttappa : Rs.60/- ")
                    print("4 for Poha    : Rs.30/- ")
                    print("5 for Exit")
                    ch = input("Enter your choice => ")
                    if ch == "1":
                        print("**********Idli***********")
                        print("Cost of Idli will be Rs.40/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Idli           ',qty,40]
                        data.append(item)
                        bill = (40)*qty + bill
                    elif ch == "2":
                        print("**********Dosa***********")
                        print("Cost of Dosa will be Rs.55/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Dosa          ',qty,550]
                        data.append(item)
                        bill = (55)*qty + bill
                    elif ch == '3':
                        print("**********Uttappa***********")
                        print("Cost of Uttappa will be Rs.60/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Uttappa        ',qty,60]
                        data.append(item)
                        bill = 60*qty + bill
                    elif ch == "4":
                        print("**********Poha***********")
                        print("Cost of Poha will be Rs.30/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Poha           ',qty,30]
                        data.append(item)
                        bill = (30)*qty + bill
                    elif ch == '5':
                        break
            elif ch == "4":
                while True:
                    print("**********Dessert***********")
                    print("1 for Icecream   : Rs.50/- ")
                    print("2 for Falooda    : Rs.75/- ")
                    print("3 for Pastery    : Rs.30/- ")
                    print("4 for Gulabjamun : Rs.25/- ")
                    print("5 for Exit")
                    ch = input("Enter your choice => ")
                    if ch == "1":
                        print("**********Icecream***********")
                        print("Cost of Icecream will be Rs.50/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Icecream       ',qty,50]
                        data.append(item)
                        bill = (50)*qty + bill
                    elif ch == "2":
                        print("**********Falooda***********")
                        print("Cost of Falooda will be Rs.75/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Falooda        ',qty,75]
                        data.append(item)
                        bill = (75)*qty + bill
                    elif ch == '3':
                        print("**********Pastery***********")
                        print("Cost of Pastery will be Rs.30/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Pastery        ',qty,30]
                        data.append(item)
                        bill = (30)*qty + bill
                    elif ch == "4":
                        print("**********Gulabjamun***********")
                        print("Cost of Gulabjamun will be Rs.25/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Gulabjamun     ',qty,25]
                        data.append(item)
                        bill = (25)*qty + bill
                    elif ch == '5':
                        break
            elif ch == '5':
                break
    elif ch == "2":
        while True:
            print("**********Non-Veg***********")
            print("1 for Starter")
            print("2 for Main Course")
            print("3 for Breakfast")
            print("4 for Exit")
            ch = input("Enter your choice => ")
            if ch == "1":
                while True:
                    print("**********Starter***********")
                    print("1 for Chicken Chrispy  : Rs.370/- ")
                    print("2 for Chicken Lollipop : Rs.340/- ")
                    print("3 for Pomfret Fry      : Rs.290/- ")
                    print("4 for Frawns Fry       : Rs.310/- ")
                    print("5 for Exit")
                    ch = input("Enter your choice => ")
                    if ch == "1":
                        print("**********Chicken Chrispy***********")
                        print("Cost of Chicken Chrispy will be Rs.370/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Chicken Chrispy',qty,370]
                        data.append(item)
                        bill = (370)*qty + bill
                    elif ch == "2":
                        print("**********Chicken Lollipop***********")
                        print("Cost of Chicken Lollipop will be Rs.340/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['ChickenLollipop',qty,340]
                        data.append(item)
                        bill = (340)*qty + bill
                    elif ch == '3':
                        print("**********Pomfret Fry***********")
                        print("Cost of Pomfret Fry will be Rs.290/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Pomfret Fry    ',qty,290]
                        data.append(item)
                        bill = (290)*qty + bill
                    elif ch == "4":
                        print("**********Frawns Fry***********")
                        print("Cost of Frawns Fry will be Rs.310/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Frawns Fry     ',qty,310]
                        data.append(item)
                        bill = (310)*qty + bill
                    elif ch == '5':
                        break
            elif ch == "2":
                while True:
                    print("**********Main Course***********")
                    print("1 for Chicken Kadai  : Rs.350/- ")
                    print("2 for Prawns Masala  : Rs.340/- ")
                    print("3 for Mutton Masala  : Rs.330/- ")
                    print("4 for Butter Chicken : Rs.310/- ")
                    print("5 for Exit")
                    ch = input("Enter your choice => ")
                    if ch == "1":
                        print("**********Chicken Kadai***********")
                        print("Cost of Chicken Kadai will be Rs.350/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Chicken Kadai  ',qty,350]
                        data.append(item)
                        bill = (350)*qty + bill
                    elif ch == "2":
                        print("**********Prawns Masala***********")
                        print("Cost of Prawns Masala will be Rs.340/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Prawns Masala  ',qty,340]
                        data.append(item)
                        bill = (340)*qty + bill
                    elif ch == '3':
                        print("**********Mutton Masala***********")
                        print("Cost of Mutton Masala will be Rs.330/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Mutton Masala  ',qty,330]
                        data.append(item)
                        bill = (330)*qty + bill
                    elif ch == "4":
                        print("**********Butter Chicken***********")
                        print("Cost of Butter Chicken will be Rs.310/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Butter Chicken ',qty,310]
                        data.append(item)
                        bill = (310)*qty + bill
                    elif ch == '5':
                        break
            elif ch == '3':
                while True:
                    print("**********Breakfast***********")
                    print("1 for Omlet           : Rs.30/- ")
                    print("2 for Egg             : Rs.25/- ")
                    print("3 for Burji           : Rs.35/- ")
                    print("4 for Chicken Pattice : Rs.30/- ")
                    print("5 for Exit")
                    ch = input("Enter your choice => ")
                    if ch == "1":
                        print("**********Omlet***********")
                        print("Cost of Omlet will be Rs.30/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Omlet         ',qty,30]
                        data.append(item)
                        bill = (30)*qty + bill
                    elif ch == "2":
                        print("**********Egg***********")
                        print("Cost of Egg will be Rs.25/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Egg           ',qty,25]
                        data.append(item)
                        bill = (25)*qty + bill
                    elif ch == '3':
                        print("**********Burji***********")
                        print("Cost of Burji will be Rs.35/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Burji          ',qty,35]
                        data.append(item)
                        bill = 35*qty + bill
                    elif ch == "4":
                        print("**********Chicken Pattice***********")
                        print("Cost of Chicken Pattice will be Rs.30/-")
                        qty = int(input("Enter Quantity => "))
                        item = ['Chicken Pattice',qty,30]
                        data.append(item)
                        bill = (30)*qty + bill
                    elif ch == '5':
                        break
            elif ch == '4':
                break


        
    elif ch == "3":
        break
    else:
        print("Please Try Again...!")

print('*********************************************************')
print("Items: Quantity: Cost")
for i in data:
    print("{}: {}x{}: {}".format(i[0],i[1],i[2],i[1]*i[2]))
payable = (bill*18/100)+bill
print("Total Payable bill including GST is Rs.{}/-".format(payable))

