from random import randrange


def lab9():
    # List to store user input as it is
    input_list = []
    # Initialize the helper variables
    enter_counter, user_input, smaller_list = 0, 0, []
    while True:
        user_input = ''
        try:
            #
            user_input = input()
            if user_input == '':
                enter_counter += 1
            if enter_counter == 1 and user_input == '':
                input_list.append(smaller_list)
                smaller_list = []
                continue
            if enter_counter == 2:
                break
            smaller_list.append(int(user_input))
            enter_counter = 0
        except:
            print('Please enter a valid integer')
    final_list = []
    for i in range(len(input_list)):
        if i % 2 == 0:
            for j in range(len(input_list[i])):
                if j % 2 == 1:
                    final_list.append(input_list[i][j])
    print(final_list)
    num_in_even_index = final_list[randrange(0, len(final_list))]
    print(num_in_even_index)
    for i in range(len(input_list)):
        if i % 2 != 0:
            for j in range(len(input_list[i])):
                if j % 2 == 0:
                    input_list[i][j] *= num_in_even_index
    print(input_list)


if __name__ == '__main__':
    lab9()
