"""
--------------------------------------------------------------------------------

    toolbox.py

--------------------------------------------------------------------------------
Copyright 2013-2024 Pierre Denis

This file is part of Lea.

Lea is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lea is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with Lea.  If not, see <http://www.gnu.org/licenses/>.
--------------------------------------------------------------------------------
"""

"""
The module toolbox provides general functions and constants needed by Lea classes 
"""

import sys
import csv
from functools import wraps

if sys.version_info[0] != 3 or sys.version_info[1] < 8:
    raise Exception("Python %s detected. Lea 4 requires Python 3.8+" % (sys.version_info,))

def make_tuple(v):
    """ returns a tuple with v as unique element
    """
    return (v,)

def min2(a, b):
    """ returns the minimum element between given a and b;
        note: this is slightly more efficient than using standard Python min function
    """
    if a <= b:
        return a
    return b

def max2(a, b):
    """ returns the maximum element between given a and b;
        note: this is slightly more efficient than using standard Python max function
    """
    if a >= b:
        return a
    return b

def gen_pairs(seq):
    """ generates as tuples all the pairs from the elements of given sequence seq
    """
    tuple1 = tuple(seq)
    length = len(tuple1)
    if length < 2:
        return
    if length == 2:
        yield tuple1
    else:
        (head, *tail) = tuple1
        for a in tail:
            yield (head, a)
        for pair in gen_pairs(tail):
            yield pair

numeric_types = (float, int, complex)

# import or define 'pairwise' function
if sys.version_info[0] == 3 and sys.version_info[1] >= 10:
    # Python 3.10+: 'pairwise' generator available natively
    from itertools import pairwise
else:
    # Python 3.8 or 3.9: define 'pairwise' generator
    from itertools import tee
    def pairwise(iterable):
        (a, b) = tee(iterable)
        next(b, None)
        return zip(a, b)

# import or define 'lcm' function
lcm = None
if sys.version_info[1] >= 9:
    # Python 3.9+: native multi-args lcm function
    from math import lcm
else:
    # Python 3.8: define multi-args 'lcm' function, using 2-args 'gcd' function
    from math import gcd
    def lcm(*integers):
        if len(integers) == 0:
             return 1
        ## Python 3 syntax: (integer1, *integers2) = integers
        integer1 = integers[0]
        integers2 = integers[1:]
        if len(integers2) == 0:
            return integer1
        lcm2 = lcm(*integers2)
        return integer1 * lcm2 // gcd(integer1, lcm2)

def indent(str_func, obj, width):
    """ returns a string representation of given object obj obtained
        by applying given function str_func and justifying on given
        width; the string is left-justified except if obj is a number
    """
    ## note that bool is a subtype of int, although it shall not be right-justified as a number
    if isinstance(obj, numeric_types) and not isinstance(obj, bool):
        return str_func(obj).rjust(width)
    return str_func(obj).ljust(width)

def memoized_method(f):
    """ returns a memoized version of the given instance method f;
        requires that the instance has a _caches_by_func attribute
        referring to a dictionary;
        can be used as a decorator
        note: not usable on functions and static methods
    """
    @wraps(f)
    def wrapper(obj, *args):
        # retrieve the cache for method f
        cache = obj._caches_by_func.get(f)
        if cache is None:
            # first call to obj.f(...) -> build a new cache for f
            cache = obj._caches_by_func[f] = {}
        elif args in cache:
            # obj.f(*args) already called in the past -> returns the cached result
            return cache[args]
        # first call to obj.f(*args) -> calls obj.f(*args) and store the result in the cache
        res = cache[args] = f(obj, *args)
        return res
    return wrapper

def str_to_bool(b_str):
    """ returns True  if b_str is '1', 't', 'true', 'y' or 'yes' (case-insensitive)
                False if b_str is '0', 'f', 'false', 'n' or 'no' (case-insensitive)
        raise ValueError exception in other cases
    """
    b_str = b_str.lower()
    if b_str in ('t', 'true', '1', 'y', 'yes'):
        return True
    if b_str in ('f', 'false', '0', 'n', 'no'):
        return False
    raise ValueError("invalid boolean literal '%s'" % (b_str,))

def read_csv_filename_counts(csv_filename, col_names=None, dialect='excel', **fmtparams):
    """ same as read_csv_file method, except that it takes a filename instead
        of an open file (i.e. the method opens itself the file for reading);
        see read_csv_file doc for more details
    """
    mode = 'r'
    with open(csv_filename, mode) as csv_file:
        return read_csv_file_counts(csv_file, col_names, dialect, **fmtparams)

def read_csv_file_counts(csv_file, col_names=None, dialect='excel', **fmtparams):
    """ returns a tuple (attr_names,data_freq) from the data read in the given CSV file
        * attr_names is a tuple with the attribute names found in the header row 
        * data_freq is a list of tuples (tuple_value,count) for each CSV row 
          with tuple_value containing read fields and count the positive integer
          giving the probability weight of this row;
        the arguments follow the same semantics as those of Python's csv.reader
        method, which supports different CSV formats
        see doc in http://docs.python.org/3.7/library/csv.html
        * if col_names is None, then the fields found in the first read row of the CSV
          file provide information on the attributes: each field is made up of a name,
          which shall be a valid identifier, followed by an optional 3-characters type
          code among  
            {b} -> boolean
            {i} -> integer
            {f} -> float
            {s} -> string
            {#} -> count   
          if the type code is missing for a given field, the type string is assumed for
          this field; for example, using the comma delimiter (default), the first row
          in the CSV file could be:
              name,age{i},height{f},married{b}
        * if col_names is not None, then col_names shall be a sequence of strings giving
          attribute information as described above, e.g.
              ('name','age{i}','height{f}','married{b}')
          it assumed that there is NO header row in the CSV file
        the type code defines the conversion to be applied to the fields read on the
        data lines; if the read value is empty, then it is converted to Python's None,
        except if the type is string, then, the value is the empty string; 
        if the read value is not empty and cannot be parsed for the expected type, then
        an exception is raised; for boolean type, the following values (case
        insensitive):
          '1', 't', 'true', 'y', 'yes' are interpreted as Python's True,
          '0', 'f', 'false', 'n', 'no' are interpreted as Python's False;
        the {#} code identifies a field that provides a count number of the row,
        representing the probability of the row or its frequency as a positive integer;
        such field is NOT included as attribute of the joint distribution; it is useful
        to define non-uniform probability distribution, as alternative to repeating the
        same row multiple times
    """
    # read the CSV file
    attr_names = []
    conv_functions = []
    count_attr_idx = None
    fields_per_row_iter = csv.reader(csv_file, dialect, **fmtparams)
    if col_names is None:
        # parse the header row
        col_names = next(fields_per_row_iter)
    # if col_names is not None, it is assumed that there is no header row in the CSV file
    for (col_idx, col_name) in enumerate(col_names):
        col_name = col_name.strip()
        if col_name.endswith('{#}'):
            if count_attr_idx is not None:
                raise ValueError("count column ('{#}') must be unique in CSV header line")
            count_attr_idx = col_idx
        else:
            has_suffix = True
            conv_function = None
            if col_name.endswith('{b}'):
                conv_function = str_to_bool
            elif col_name.endswith('{i}'):
                conv_function = int
            elif col_name.endswith('{f}'):
                conv_function = float
            elif not col_name.endswith('{s}'):
                has_suffix = False
            if has_suffix:
                attr_name = col_name[:-3].strip()
            else:
                attr_name = col_name
            attr_names.append(attr_name)
            conv_functions.append(conv_function)
    # parse the data rows
    fields_per_row = tuple(fields_per_row_iter)
    data_freq = []
    for fields in fields_per_row:
        if count_attr_idx is None:
            # no 'count' field: each read row has a count of 1 
            count = 1
        else:
            # 'count' field: extract the count value from the fields
            count = int(fields.pop(count_attr_idx))
        # conversion of read fields according to optional given types
        conv_fields = []
        for (field, conv_function) in zip(fields, conv_functions):
            if conv_function is None:
                conv_field = field
            else:
                if field == '':
                    # empty value translated as Python's None 
                    conv_field = None
                else:
                    conv_field = conv_function(field)
            conv_fields.append(conv_field)
        data_freq.append((tuple(conv_fields), count))
    return (attr_names, data_freq)

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    """ returns True iff float a and b are almost equal
    """
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def gen_all_slots(a_class, root_class=()):
    """ generates all slots (strings) of a_class, including those defined in its superclasses;
        if root_class is a class, then only slots of classes that are *strict* subclasses
        of root_class are yielded (i.e. slots of root_class itself are *not* yielded)
    """
    if a_class is object or a_class is root_class \
            or not issubclass(a_class, root_class):
        return
    for a_superclass in a_class.__bases__:
        for slot in gen_all_slots(a_superclass, root_class):
            yield slot
    for slot in a_class.__slots__:
        yield slot
