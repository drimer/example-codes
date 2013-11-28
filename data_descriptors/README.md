Descriptors let you customize access the access to class attributes. They are
used to implement properties, class, static methods, and the super type. They
are defined as classes that specify how attributes of another class can be
accessed.

The descriptor classes need to have three special methods implemented:

__set__: This is called whenever the attribute is set.

__get__: This is called whenever the attribute is read.

__delete__: This is called when del is invoked on the attribute.

These methods are called before acessing the __dict__ attribute. So to speak, we
could say that the usual __dict__ mapping that contains all elements of an
object instance is hijacked when a class attribute is defined and has a getter
and a setter method.