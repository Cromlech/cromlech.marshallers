cromlech.marshallers
====================

`cromlech.marshallers` provides a collection of independant
uniformized marshallers, to use in data manipulation and persistence.

Marshallers using third party libraries use conditionnal import.
Check the `setup.py` `extra_requires` to include them transparently.


Examples
--------

  >>> from cromlech.marshallers import JSONMarshaller
  >>> marshaller = JSONMarshaller()
  >>> struct = [1, "two", 3]
  >>> data = marshaller.dumps(struct)
  >>> assert marshaller.loads(data) == struct


Features
--------

Each marshaller can handle strings or bytes (according to their binary
nature), streams and files.

   >>> marshaller.dumps(struct)
   >>> marshaller.loads(data)
   >>> marshaller.dump(struct, stream)
   >>> marshaller.load(stream)

File access is watched by a lock that prevents concurrency. This lock
can be configured to include a comprehensive timeout.

   >>> marshaller.dump_to(struct, path, timeout=2)
   >>> marshaller.load_from(path, timeout=2)

In addition to that, the marshaller can be used as a decorator, in
order to marshal the result of a function or method :

   >>> @marshaller.wraps
   ... def hello():
   ...     return 'world'


Current available marshallers
-----------------------------

Currently, `cromlech.marshallers` provides :

  - JSON (native & RapidJSON)
  - pickle (native)
  - marshal (native)
  - msgpack
  - YAML
  - BSON
