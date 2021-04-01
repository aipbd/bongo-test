

def prepare_test_dictionary():
    return {
        'a': 'aaa',
        'b': {
            'e': 'bbb',
            'f': 'bbb',
            'g': {
                'h': 'ccc',
            },
        },
        'c': 'aaa',
        'd': 'aaa',
    }


def print_factory(value, depth):
    if isinstance(value, dict):
        return print_dictionary(value, depth+1)


def print_dictionary(dictionary, depth):
    keys = dictionary.keys()
    for key in keys:
        print(key, depth)
        print_factory(dictionary[key], depth=depth)


def print_depth(data):
    print_factory(data, depth=0)


if __name__ == '__main__':
    test_dictionary = prepare_test_dictionary()
    print_depth(data=test_dictionary)

