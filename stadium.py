total_seats = 150
normal_seats_left = 130
recliner_seats_left = 20
normal_seat_cost = 250
recliner_seat_cost = 350
cost_normal = 0
cost_recliner = 0
total = 0
while True:
    print("welcome to the tottenham football stadium")
    print("normal seat price: 250")
    print("recliner seat price: 250")
    name = input("enter your name: ")
    phone_nub = int(input("enter your number: "))
    choice = input("which type of seats do you want normal/recliner")
    while True:
        if choice == "normal":
            choose = int(input("how many normal seats do you want: "))
            if choose <= normal_seats_left:
                cost_normal += choose * normal_seat_cost
                normal_seats_left -= choose
                print(" cost of normal seat", cost_normal)
                print("total normal seats left", normal_seats_left)
            else:
                print("normal seat is not available")

        if choice == "recliner":
            choose = int(input("how many recliner seats do you want: "))
            if choose <= recliner_seats_left:
                cost_recliner += choose * recliner_seat_cost
                recliner_seats_left -= choose
                print("cost of recliner seat left", cost_recliner)
                print("total recliner seats left", recliner_seats_left)
            else:
                print("normal seat is not available")

        repeat = input("do you want to book more normal/recliner seats(yes/no): ")
        if repeat == "no" or repeat == "NO" or repeat == "No":
            break

    print("_" * 70)
    print("customer's name", name)
    print("customer's phone number", phone_nub)
    total += cost_normal+cost_recliner
    print("total cost", total)
    print("_" * 70)
    repeat_customer = input("next customer please?")
    if repeat_customer == "no" or repeat_customer == "No" or repeat_customer == "NO":
        break