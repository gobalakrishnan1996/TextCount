# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


TEXT = 'Happy day! I love life!'


def get_counts_dict(str):
    """
    Returns a dictionary with where each key is a character and the corresponding
    value is the number of times that character appeared in the string str passed in.
    """
    counts = {}                             # create empty dictionary

    for ch in str:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] += 1

    return counts


def print_counts(dict):
    """
    This function prints out the key and its associated value for each
    key/value pair in the dictionary passed in.
    """
    print('Counts from dictionary')
    for key in dict:
        print(str(key) + ' = ' + str(dict[key]))


def main():
    """
    Display the number of times each character appears in the constant TEXT.
    """
    count_dict = get_counts_dict(TEXT)
    print('count_dict = ', count_dict)
    print_counts(count_dict)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
