NAME

::

   LIBOP - original programmer.


DESCRIPTION

::

   LIBOP is a python3 library providing all the tools to create a
   unix command line program, such as disk perisistence for
   configuration files, event handler to handle the client/server
   connection, code to introspect modules for commands, a parser to
   parse commandline options and values, etc.


SYNOPSIS

::

   >>> from op import Object
   >>> o = Object()
   >>> o.a = "b"
   >>> write(o, "test")
   >>> oo = Object()
   >>> read(oo, "test")
   >>> oo
   {"a": "b"}  


INSTALL

::

   $ pip install libop


AUTHOR

::

   libbot <libbotx@gmail.com>


COPYRIGHT

::

   LIBOP is placed in the Public Domain.
