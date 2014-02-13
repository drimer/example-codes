class APIDocumentation(object):
    def _gen_attrib_doc(self, target, attrib_name):
        attribute = getattr(target, attrib_name)
        if callable(attribute) and hasattr(attribute, 'im_func'):
            return '\n'.join(['Instance method:',
                              '\tName: %s' % attribute.im_func.__name__])
        elif type(attribute) in (str, int, float, unicode):
            return '\n'.join(['Attribute:',
                              '\tName: %s' % str(attrib_name),
                              '\tValue: %s' % str(attribute)])


    def _gen_docs(self, target):
        public_attr_names = [attr_name for attr_name in dir(target)
                             if not attr_name.startswith('_')]
        attribs_docs = [self._gen_attrib_doc(target, attr_name)
                          for attr_name in public_attr_names]
        return '\n'.join(attribs_docs)

    def __get__(self, instance, klass):
        target = instance if instance is not None else klass
        return self._gen_docs(target)


class ExampleClass(object):
    __doc__ = APIDocumentation()

    public_attribute = 'I am public!'

    def cool_method(self):
        '''Cool docstring'''
        pass

    def not_so_cool_method(self):
        '''Not so cool doctring'''
        pass


if __name__ == '__main__':
    print 'Output[1]:'
    print ExampleClass.__doc__
    # Output[1]:
    # Instance method:
    # Name: cool_method
    # Instance method:
    # Name: not_so_cool_method
    # Attribute:
    # Name: public_attribute
    # Value: I am public!

    instance = ExampleClass()
    print 'Output[2]:'
    print instance.__doc__
    # Output[2]:
    # Instance method:
    # Name: cool_method
    # Instance method:
    # Name: not_so_cool_method
    # Attribute:
    # Name: public_attribute
    # Value: I am public!
