def recieve_list(list):

    word_dict = {}

    for i in list:
        word_dict = {i[0].upper() : i}

    return word_dict

def main():
    list = ['Ali', 'Atushi', 'Hello']
    print(recieve_list(list))


main()