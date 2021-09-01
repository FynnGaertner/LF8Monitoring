def my_riegel(riegel):
    true = input("Willst du ein " + riegel + " ? [j/n]")

    if true == "j":
        print(riegel)

    else:
        print("Fuck Off")


my_riegel(input("Was willste?"))

