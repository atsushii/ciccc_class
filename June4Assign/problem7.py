def receive_alphabet():
    """
    create words dictionary

    return
    --------------------
    alphabet_dict : dictionary
        list of all distinct words starts with English alphabets.
    """

    alphabet_dict, alphabet_table = create_dict()
    while True:
        input_alphabet = input('enter alphabet: ')

        if input_alphabet == 'exit':
            for i in alphabet_table:
                alphabet_dict[str(i).upper()] = set(alphabet_dict[str(i).upper()])

            return alphabet_dict

        if input_alphabet == '':
            continue

        alphabet_dict[input_alphabet[0].upper()].append(input_alphabet)


def create_dict():
    """
    set alphabet as key

    return
    --------------------
    alphabet_dict : dictionary
        dictionary which has alphabet key
    """

    alphabet_dict = {}
    alphabet_table = [chr(i) for i in range(65, 65 + 26)]

    for i in alphabet_table:
        alphabet_dict[str(i).upper()] = []
    return alphabet_dict, alphabet_table

def main():
    """
    problem7

    print result
    """
    print(receive_alphabet())

main()
