This example shows how to spy on a method of an already existing object. In
this particular case, the Canvas object could have been created directly as a
mock.Mock() instance, which offers this functionality, but there are times
when we already have an object in which we want to inspect the calls to its
methods.
