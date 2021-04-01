from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    father: object = None


def prepare_test_dictionary():
    p1 = Person(first_name='name', last_name='last')
    p2 = Person(first_name='name', last_name='last', father=p1)
    return {
        'a': 'aaa',
        'b': {
            'e': 'bbb',
            'f': 'bbb',
            'g': {
                'h': 'ccc',
                'p': p2,
            },
        },
        'c': 'aaa',
        'd': 'aaa',
    }


def print_factory(value, depth):
    if isinstance(value, dict):
        return print_dictionary(value, depth+1)
    if isinstance(value, Person):
        return print_person(value, depth+1)


def print_dictionary(dictionary, depth):
    keys = dictionary.keys()
    for key in keys:
        print(key, depth)
        print_factory(dictionary[key], depth=depth)


def print_person(person, depth):
    print("first_name", depth)
    print("last_name", depth)
    print("father", depth)
    return print_factory(person.father, depth=depth)


def print_depth(data):
    print_factory(data, depth=0)


if __name__ == '__main__':
    test_dictionary = prepare_test_dictionary()
    print_depth(data=test_dictionary)
