class FullName(object):
    def __init__(self):
        self._name = ''
        self._surname = ''

    def __get__(self, instance, klass):
        if '' in (self._name, self._surname):
            return ''

        name = self._name[0].upper() + self._name[1:]
        surname = self._surname[0].upper() + self._surname[1:]
        return name + ' ' + surname

    def __set__(self, instance, value):
        self._name, self._surname = value.split()


class Person(object):
    full_name = FullName()



if __name__ == '__main__':
    person = Person()
    print 'Output[1]: ', person.full_name
    # Output[1]: ''
    person.full_name = 'alberto aguilera'
    print 'Output[2]:', person.full_name
    # Output[2]: 'Alberto Aguilera'
