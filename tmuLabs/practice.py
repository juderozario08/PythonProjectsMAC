from random import randrange


class TuesdayLabs():
    def lab9(self):
        # List to store user input as it is
        input_list = []
        # List to store all elements separately from the user input
        final_list = []
        enter_counter, user_input, go_back, smaller_list = 0, 0, False, []
        while True:
            user_input = input()
            if user_input == '':
                enter_counter += 1
            if enter_counter == 1 and user_input == '':
                input_list.append(smaller_list)
                smaller_list = []
                continue
            if enter_counter == 2:
                break
            for i in user_input:
                if i.isalpha() or i == '.':
                    print('Please enter a valid integer')
                    go_back = True
                    break
            if not go_back:
                smaller_list.append(int(user_input))
                enter_counter = 0
            go_back = False
        for i in input_list:
            for j in i:
                final_list.append(j)
        num_in_even_index = final_list[randrange(0, len(final_list), 2)]
        for i in range(len(input_list)):
            if i % 2 != 0:
                for j in range(len(input_list[i])):
                    input_list[i][j] *= num_in_even_index
        print(input_list)


if __name__ == '__main__':
    tuesday8am = TuesdayLabs()
    tuesday8am.lab9()
