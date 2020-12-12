inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
    part = item.split(",")
    #print(item[1], item[0], item[2])
    print("The store has{} {}, each for{} USD.".format(part[1], part[0], part[2]))
