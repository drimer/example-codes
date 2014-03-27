from datetime import datetime
import random


def create_dictionaries(num):
    for _ in xrange(num):
        dictionary = dict.fromkeys(range(500), True)
        yield dictionary, random.choice(dictionary.keys())

def remove_from_dict_with_del(num_iters=100000):
    for dictionary, key in create_dictionaries(num_iters):
        del dictionary[key]


def remove_from_dict_with_pop(num_iters=100000):
    for dictionary, key in create_dictionaries(num_iters):
        dictionary.pop(key)


if __name__ == '__main__':
    t1 = datetime.now()
    remove_from_dict_with_del()
    t2 = datetime.now()
    print 'Remove elements fromm dictionary using `del`:'
    print '|--> took %s seconds' % (t2 - t1).total_seconds()


    t1 = datetime.now()
    remove_from_dict_with_pop()
    t2 = datetime.now()
    print 'Remove elements fromm dictionary using `pop`:'
    print '|--> took %s seconds' % (t2 - t1).total_seconds()
