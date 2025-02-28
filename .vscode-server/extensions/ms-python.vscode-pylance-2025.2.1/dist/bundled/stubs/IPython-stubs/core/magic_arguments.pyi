"""
This type stub file was generated by pyright.
"""

import argparse
from IPython.utils.decorators import undoc

''' A decorator-based method of constructing IPython magics with `argparse`
option handling.

New magic functions can be defined like so::

    from IPython.core.magic_arguments import (argument, magic_arguments,
        parse_argstring)

    @magic_arguments()
    @argument('-o', '--option', help='An optional argument.')
    @argument('arg', type=int, help='An integer positional argument.')
    def magic_cool(self, arg):
        """ A really cool magic command.

    """
        args = parse_argstring(magic_cool, arg)
        ...

The `@magic_arguments` decorator marks the function as having argparse arguments.
The `@argument` decorator adds an argument using the same syntax as argparse's
`add_argument()` method. More sophisticated uses may also require the
`@argument_group` or `@kwds` decorator to customize the formatting and the
parsing.

Help text for the magic is automatically generated from the docstring and the
arguments::

    In[1]: %cool?
        %cool [-o OPTION] arg
        
        A really cool magic command.
        
        positional arguments:
          arg                   An integer positional argument.
        
        optional arguments:
          -o OPTION, --option OPTION
                                An optional argument.

Here is an elaborated example that uses default parameters in `argument` and calls the `args` in the cell magic::

    from IPython.core.magic import register_cell_magic
    from IPython.core.magic_arguments import (argument, magic_arguments,
                                            parse_argstring)


    @magic_arguments()
    @argument(
        "--option",
        "-o",
        help=("Add an option here"),
    )
    @argument(
        "--style",
        "-s",
        default="foo",
        help=("Add some style arguments"),
    )
    @register_cell_magic
    def my_cell_magic(line, cell):
        args = parse_argstring(my_cell_magic, line)
        print(f"{args.option=}")
        print(f"{args.style=}")
        print(f"{cell=}")

In a jupyter notebook, this cell magic can be executed like this::

    %%my_cell_magic -o Hello
    print("bar")
    i = 42

Inheritance diagram:

.. inheritance-diagram:: IPython.core.magic_arguments
   :parts: 3

'''
NAME_RE = ...
@undoc
class MagicHelpFormatter(argparse.RawDescriptionHelpFormatter):
    """A HelpFormatter with a couple of changes to meet our needs.
    """
    def add_usage(self, usage, actions, groups, prefix=...): # -> None:
        ...
    


class MagicArgumentParser(argparse.ArgumentParser):
    """ An ArgumentParser tweaked for use by IPython magics.
    """
    def __init__(self, prog=..., usage=..., description=..., epilog=..., parents=..., formatter_class=..., prefix_chars=..., argument_default=..., conflict_handler=..., add_help=...) -> None:
        ...
    
    def error(self, message):
        """ Raise a catchable error instead of exiting.
        """
        ...
    
    def parse_argstring(self, argstring):
        """ Split a string into an argument list and parse that argument list.
        """
        ...
    


def construct_parser(magic_func): # -> MagicArgumentParser:
    """ Construct an argument parser using the function decorations.
    """
    ...

def parse_argstring(magic_func, argstring):
    """ Parse the string of arguments for the given magic function.
    """
    ...

def real_name(magic_func):
    """ Find the real name of the magic.
    """
    ...

class ArgDecorator:
    """ Base class for decorators to add ArgumentParser information to a method.
    """
    def __call__(self, func):
        ...
    
    def add_to_parser(self, parser, group): # -> None:
        """ Add this object's information to the parser, if necessary.
        """
        ...
    


class magic_arguments(ArgDecorator):
    """ Mark the magic as having argparse arguments and possibly adjust the
    name.
    """
    def __init__(self, name=...) -> None:
        ...
    
    def __call__(self, func):
        ...
    


class ArgMethodWrapper(ArgDecorator):
    """
    Base class to define a wrapper for ArgumentParser method.

    Child class must define either `_method_name` or `add_to_parser`.

    """
    _method_name: str
    def __init__(self, *args, **kwds) -> None:
        ...
    
    def add_to_parser(self, parser, group): # -> None:
        """ Add this object's information to the parser.
        """
        ...
    


class argument(ArgMethodWrapper):
    """ Store arguments and keywords to pass to add_argument().

    Instances also serve to decorate command methods.
    """
    _method_name = ...


class defaults(ArgMethodWrapper):
    """ Store arguments and keywords to pass to set_defaults().

    Instances also serve to decorate command methods.
    """
    _method_name = ...


class argument_group(ArgMethodWrapper):
    """ Store arguments and keywords to pass to add_argument_group().

    Instances also serve to decorate command methods.
    """
    def add_to_parser(self, parser, group):
        """ Add this object's information to the parser.
        """
        ...
    


class kwds(ArgDecorator):
    """ Provide other keywords to the sub-parser constructor.
    """
    def __init__(self, **kwds) -> None:
        ...
    
    def __call__(self, func):
        ...
    


__all__ = ['magic_arguments', 'argument', 'argument_group', 'kwds', 'parse_argstring']
