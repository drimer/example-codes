def singleton(klass):
    class wrapper(klass):
        _instance = None

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(wrapper, cls).__new__(cls, *args,
                                                            **kwargs)

            return cls._instance

    return wrapper


@singleton
class Vehicle(object):
    def __init__(self):
        self.wheels = 0


if __name__ == '__main__':
    car = Vehicle()
    car.wheels = 4
    bike = Vehicle()
    bike.wheels = 2
    print 'Out[1]:', car.wheels
    # Out[1]: 2
