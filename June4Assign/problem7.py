def receive_alphabet():
    """
    create words dictionary

    return
    --------------------
    alphabet_dict : dictionary
        list of all distinct words starts with English alphabets.
    """

    alphabet_dict, alphabet_table = create_dict()
    result_alphabet_dict = {}
    while True:
        input_alphabet = input('enter alphabet: ')

        if input_alphabet == 'exit':
            result_alphabet_dict = clean_dict(alphabet_dict, alphabet_table, result_alphabet_dict)

            return result_alphabet_dict

        if input_alphabet == '':
            continue

        alphabet_dict[input_alphabet[0].upper()].append(input_alphabet)


def create_dict():
    """
    sort alphabet dictionary

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


def clean_dict(alphabet_dict, alphabet_table, result_alphabet_dict):
    """
    delete value if there is not word in the list

    parameter
    ------------------------------
    alphabet_dict : dictionary
        all distinct words are including

    alphabet_table : list
        include all alphabet

    result_alphabet_dict : dictionary
        initialized new dictionary for add result

    return
    -----------------------------
    result_alphabet_dict : dictionary
        all distinct words starts with English alphabets for result
    """
    for i in alphabet_table:
        if not len(alphabet_dict[str(i).upper()]) == 0:
            result_alphabet_dict[str(i).upper()] = set(alphabet_dict[str(i).upper()])
    return result_alphabet_dict

def main():
    """
    problem7

    print result
    """
    print(receive_alphabet())

main()
