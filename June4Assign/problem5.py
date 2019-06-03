def receive_user_name():
    """
    check userName


    return
    ----------------
    user_name_dict : dictionary
         dictionary which shows all the name the user has entered and how many times each name is repeated
    """
    user_name_dict = {}
    while True:
        user_name = input('enter userName: ')

        if user_name == '':
            continue

        if user_name == '0':
            return user_name_dict

        if not user_name in user_name_dict:
            user_name_dict[user_name] = 1
        else:
            user_name_dict[user_name] += 1
def main():

    print(receive_user_name())

main()
