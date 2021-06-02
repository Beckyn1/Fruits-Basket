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
    print("{} is chosen".format(l[choice]))
    quantity = get_integer("how many {} would you like to add".format(l[choice][0]))
    # validate
    l[choice][1] += quantity
    print("You  now have {}".format(l[choice]))

def eat_fruit(l):
    # print list with indexes
    for i in range(0, len(l)):
        output = "{}: {} {}".format(i, l[i][1], l[i][0])
        print(output)
    choice = get_integer("please choose a fruit number")
    # validate
    print("{} is chosen".format(l[choice]))
    quantity = get_integer("how many {} would you like to eat".format(l[choice][0]))
    # validate
    l[choice][1] -= quantity
    print("You  now have {}".format(l[choice]))


def main():
    fruit_list = [
        ["apples", 2],
        ["pears", 3],
        ["quinces", 3],
        ["lemons", 7]
    ]

    menu_list = [
        ["R", "Review Fruit"],
        ["A", "Add Fruit"],
        ["E", "Eat Fruit"],
        ["Q", "Quit"]
    ]
    run_program = True
    while run_program:
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        user_choice = get_string("Please select an option: -> ")
        if user_choice == "R":
            review_fruit(fruit_list)
        elif user_choice == "A":
            add_fruit(fruit_list)
        elif user_choice == "E":
            eat_fruit(fruit_list)
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry")
            print("Thank you, the program has ended")


if __name__ == "__main__":

    main()
