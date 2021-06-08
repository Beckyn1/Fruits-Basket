def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):

    user_input = input(m)
    return user_input


def review_fruit(l):
    for x in l:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)
    return None


def add_fruit(l):
    # print list with indexes
    for i in range(0, len(l)):
        output = "{}: {} {}".format(i, l[i][1], l[i][0])
        print(output)

    choice = get_integer("please choose a fruit number")
    # validate
    if 0 <= choice or choice < len(l):
        quantity = get_integer("how many {} would you like to add".format(l[choice][0]))
        # validate
        l[choice][1] += quantity
        print("You  now have {}".format(l[choice]))
    else:
        print("Unrecognised entry, can only be between 0 and 10")
        return add_fruit(l)


def eat_fruit(l):

    # print list with indexes
    for i in range(0, len(l)):
        output = "{}: {} {}".format(i, l[i][1], l[i][0])
        print(output)
    choice = get_integer("please choose a fruit number")
    # validate
    if 0 >= choice or choice < len(l):
        print("{} is chosen".format(l[choice]))
        quantity = get_integer("how many {} would you like to eat".format(l[choice][0]))
        # validate
        l[choice][1] -= quantity
        print("You  now have {}".format(l[choice]))
    else:
        print("Unrecognised entry, can only be between 0 and 10")
        return eat_fruit(l)


def new_fruit(l):
    new_fruits = get_string("Please enter a fruit name")
    quantity = get_integer("Please enter a quantity")
    new_list = [new_fruits, quantity]
    l.append(new_list)
    print("{} {} has been added to the fruit bowl".format(quantity, new_fruits))


def delete_fruit(l):

    for i in range(0, len(l)):
        print("{}:{}".format(i, l[i]))

    delete_fruit = get_integer("Which fruit type do you want to delete?")
    if delete_fruit >= 0 or delete_fruit < len(l):
        l.pop(delete_fruit)
        output = ("{} is removed".format(delete_fruit))
        print(output)
    else:
        output = "Unrecognisable entry"
        print(output)


def main():

    fruit_list = [
        ["apples", 2],
        ["pears", 3],
        ["quinces", 3],
        ["lemons", 7]
    ]
    print()
    print("Welcome to fruits basket!")
    print("-"*42)
    print("Please select an option from the menu:")
    menu_list = [
        ["R", "Review Fruit"],
        ["A", "Add Fruit"],
        ["E", "Eat Fruit"],
        ["N", "New Fruit"],
        ["D", "Delete Fruit"],
        ["Q", "Quit"]
    ]
    run_program = True
    while run_program:
        for x in menu_list:

            output = "{}: {}".format(x[0], x[1])
            print(output)
            print("-" * 42)
        user_choice = get_string("Please select an option: -> ")
        user_choice = user_choice.upper()
        user_choice = user_choice.strip()
        if user_choice == "R":
            review_fruit(fruit_list)
        elif user_choice == "A":
            add_fruit(fruit_list)
        elif user_choice == "E":
            eat_fruit(fruit_list)
        elif user_choice == "N":
            new_fruit(fruit_list)
        elif user_choice == "D":
            delete_fruit(fruit_list)
        elif user_choice == "Q":
            print("Thank you for using fruit bowl!")
            run_program = False
        else:
            print("Unrecognised entry must be R, A, E or Q")


if __name__ == "__main__":

    main()
