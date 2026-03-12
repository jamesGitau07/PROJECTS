items = {
    "sugar": 150,
    "bread": 70,
    "milk": 80,
    "rice": 210,
    "soap": 90,
} 

goods_dispatched = []
goods_arrived = []

print("welcome to the james k supermarket")

while True:
    print("\nChoose an option:")
    print("1. view available items")
    print("2. view items prices")
    print("3.view goods dispatched")
    print("4.view goods arrived")
    print("5.add arrived goods")
    print("6.dispatched goods")
    print("7.Exit")
    
    choice = input("enter your choice(1-7) ") 
    
    if choice == "1":
        print("\navailable items: ")
        for item in items :
            print("-",item)
    elif choice =="2":
        print("n\item prices: ")
        for item,price in items.items():
            print(item,"cost ksh",price)
    elif choice == "3":
        print("n\goods_dispatched: ")
        if len(goods_dispatched) == 0:
            print("no have not been dispatched. ")
        else:
            for items in goods_dispatched:
                print("-",item)
    elif choice == "4":
        print("\nview goods arrived: ")
        if len (goods_arrived)== 0:
            print("no new goods have arrived.")
        else:
            for items in goods_arrived:
                print("-",items)
    elif choice == "5":
        new_item = input("enter name of goods arrived: ")
        goods_arrived.append(new_item)
        print(new_item,"has been added to arrived goods.")
    elif choice == "6":
        dispatched_items = input("enter item to dispatch: ")
        if dispatched_items in items:
            goods_dispatched.append(dispatched_items)
            print(dispatched_items,"has been dispatched")
        else:
            print("item not found in supermarket. ")
    elif choice =="7":
        print("exiting system... thankyou!")
        break
    else:
        print("invalid choice.please try again.")
    

    

