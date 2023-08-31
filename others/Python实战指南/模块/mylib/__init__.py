from .mode1 import __add,__sub,test_fun_a
from .mode2 import __mul,__div,test_fun_b

add=__add
sub=__sub
mul=__mul
div=__div

__all__ = 'add', 'sub','mul', 'div',test_fun_a(),test_fun_b()