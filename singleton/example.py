class OnlyOne(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(OnlyOne, cls).__new__(cls, *args, **kwargs)

        return cls._instance


if __name__ == '__main__':
    car = OnlyOne()
    car.wheels = 4
    bike = OnlyOne()
    bike.wheels = 2
    print 'Out[1]:',  car.wheels
    # Out[1]: 2
