"""
--------------------------------------------------------------------------------

    alea.py

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

from .lea import Lea
from .exceptions import LeaError
from .ext_fraction import ExtFraction
from .ext_decimal import ExtDecimal
from .toolbox import memoized_method, make_tuple, read_csv_file_counts, read_csv_filename_counts, indent
from fractions import Fraction
from decimal import Decimal
from random import random
from math import log2
from bisect import bisect_left, bisect_right
import itertools
from math import factorial
from operator import truediv
from collections import defaultdict, OrderedDict

# try to import optional modules:
# - Matplotlib
try:
    import matplotlib.pyplot as plt
    # matplotlib module installed
except ImportError:
    # matplotlib module not installed
    plt = None
# - SymPy
try:
    import sympy
    # sympy module installed
except ImportError:
    # sympy module not installed
    sympy = None
# - NumPy
try:
    # see usage of np_bool_type in Alea._p method
    from numpy import bool_ as np_bool_type
    # NumPy module installed
except ImportError:
    # NumPy module not installed
    np_bool_type = ()


class Alea(Lea):
    """
    Alea is a Lea subclass, which instance is defined by explicit probability distribution data.
    An Alea instance is defined by given value-probability pairs, that is an explicit probability
    mass function (pmf). The probabilities can be expressed as any object with arithmetic semantic.
    The main candidates are float, fraction or symbolic expressions.
    An Alea instance is an "elementary pex", as defined in the paper on Statues algorithm
    (see http://arxiv.org/abs/1806.09997).
    """

    __slots__ = ('_vs', '_ps', '_cumul', '_inv_cumul', '_random_iter', '_caches_by_func')

    # class or function used by default to convert each probability given in
    # an Alea constructor method; if None and if no prob_type arg is
    # specified in the constructor, then each probability is stored as-is
    _prob_type = None

    # function used to simplify symbolic probability expressions to be
    # displayed (see _simplify and Alea.__init__ methods)
    # setting it to None disables any symbolic simplification
    _symbolic_simplify_function = sympy and staticmethod(sympy.simplify)

    # dictionary used in _downcast method
    __downcast_class = {Fraction: ExtFraction,
                        Decimal: ExtDecimal}

    @staticmethod
    def _create_prob_symbol(arg):
        """ static method, if given arg is a string, then
               returns a sympy Symbol, having arg as name, possibly embedded
               in parentheses if arg is not a valid identifier;
            otherwise,
               returns arg as-is (which could incidentally be a sympy Symbol)
        """
        if isinstance(arg, str):
            if not arg.isidentifier():
                arg = "(%s)" % (arg,)
            return sympy.Symbol(arg)
        return arg

    @staticmethod
    def _create_prob_obj(arg):
        """ static method, returns a probability object corresponding to the
            given arg:
            if arg is not a string, then it is returned as-is;
            if arg is a string, then it is tried to be interpreted as
            ExtDecimal, ExtFraction or sympy symbol, in that order;
            the object of the first successful type is returned;
            note: ExtDecimal allows for '%' suffixes
        """
        if not isinstance(arg, str):
            return arg
        # arg is a string, convert it into an object representing a number
        try:
            return ExtDecimal(arg)
        except Exception:
            pass
        try:
            return ExtFraction(arg)
        except Exception:
            pass
        if sympy is None:
            raise LeaError(
                "probability expression '%s' requires the sympy module, which does not seem to be installed" \
                % (arg,))
        return Alea._create_prob_symbol(arg)

    @staticmethod
    def _simplify(v, to_class=None):
        """ static method, tries to simplify the given value v
            if given v is a sympy Expr, then
                returns the simplified probability using
                    Alea._symbolic_simplify_function
            otherwise, if to_class is int, then
                returns v converted to float
            otherwise, if to_class is not None, then
                returns v converted to to_class
            otherwise,
                returns v unchanged
        """
        if Alea._symbolic_simplify_function is not None and isinstance(v, sympy.Expr):
            return Alea._symbolic_simplify_function(v)
        if to_class is not None:
            if to_class is int:
                return float(v)
            return to_class(v)
        return v

    def __init__(self, vs, ps, normalization=True, prob_type=-1):
        """ initializes Alea instance's attributes
            vs is a sequence of values
            ps is a sequence of probabilities (same length and order as ps)
            if normalization argument is True (default), then probabilities ps are
            updated before being stored to ensure that their sum equals 1:
            * if one probability is None, then it is replaced by
               1 - sum(not None elements of ps)
            * otherwise, each probability p is replaced by p / sum(ps)
              (in such case, it's not mandatory to have true probabilities for ps
               elements; these could be simple counters for example)
            if prob_type is different from -1, then the given probabilities ps
            are converted using prob_type, as documented in Alea.set_prob_type;
            requires that there is maximum one None probability if normalization;
            requires that vs and ps have same length
        """
        Lea.__init__(self)
        # for an Alea instance, the alea cache is itself
        self._alea = self
        self._vs = tuple(vs)
        prob_type_func = get_prob_type(prob_type)
        if prob_type_func is not None:
            ps = (None if p is None else prob_type_func(p) for p in ps)
        if normalization:
            ps = tuple(ps)
            nb_none = ps.count(None)
            if nb_none > 1:
                raise LeaError("for normalization, no more than one single probability can be None")
            if nb_none == 1:
                p_sum = Alea._simplify(sum(p for p in ps if p is not None))
                Alea._check_prob(p_sum)
                idx_none = ps.index(None)
                ps = ps[:idx_none] + (1 - p_sum,) + ps[idx_none + 1:]
            else:
                p_sum = Alea._simplify(sum(ps))
                ps = (truediv(p, p_sum) for p in ps)
            if Alea._symbolic_simplify_function is not None and isinstance(p_sum, sympy.Expr):
                ps = (Alea._symbolic_simplify_function(p) for p in ps)
        self._ps = tuple(ps)
        if len(self._vs) != len(self._ps):
            raise LeaError(
                "number of values (%d) different from number of probabilities (%d)" % (len(self._vs), len(self._ps)))
        self._cumul = [0]
        self._inv_cumul = []
        self._random_iter = self._create_random_iter()
        self._caches_by_func = {}

    # constructor methods
    # -------------------

    # call tree of Alea constructor methods ([S] means function or static method):
    #
    #   __init__
    #    <-- coerce [S]
    #    <-- pmf [S]
    #         <-- vals [S]
    #              <-- read_pandas_df [S]
    #         <-- interval [S]
    #         <-- read_csv_file [S]
    #         <-- _selections
    #              <-- draw_sorted_with_replacement
    #              <-- draw_sorted_without_replacement
    #    <-- _pmf_ordered [S]
    #         <-- pmf [S]
    #              <-- ... (see above)
    #         <-- draw_without_replacement
    #              <-- draw_sorted_without_replacement
    #    <-- _binary_distribution [S]
    #         <-- event [S]
    #         <-- bernoulli [S]

    def new(self, n=None, prob_type=-1, sorting=False, normalization=False):
        """ returns a new Alea instance, which represents the same probability
            distribution as self but for another event, independent from the
            event represented by self;
            * if n is not None,
               then a tuple containing n new independent Alea instances is returned
            * if prob_type is -1,
               then the returned Alea instance is a shallow copy of self
                    (values and probabilities data are shared);
               otherwise, the returned Alea instance has shared values data
                    but has new probabilities converted according to prob_type
                    (see doc of Alea.set_prob_type);
            * sorting allows sorting the value of the returned Alea instance
              (see pmf method);
            * normalization (default: False): if True, then each probability is divided
              by the sum of all probabilities
            note that the present method overloads Lea.new to be more efficient;
        """
        if sorting:
            # for sorting, relay to Lea.new, which is less efficient but handles the case correctly
            return Lea.new(self, prob_type=prob_type, sorting=True)
        new_alea = Alea(self._vs, self._ps, normalization=normalization, prob_type=prob_type)
        if prob_type == -1:
            ## note that the new Alea instance shares the immutable _vs and _ps attributes of self
            ## it can share also the mutable _cumul and _inv_cumul attributes of self (lists)
            new_alea._cumul = self._cumul
            new_alea._inv_cumul = self._inv_cumul
        if n is not None:
            return tuple(new_alea.new() for _ in range(n))
        return new_alea

    @staticmethod
    def _check_not_empty(arg):
        """ static method, verifies that the given arg is not empty;
            otherwise, raises an exception
        """
        if len(arg) == 0:
            raise LeaError("cannot build a probability distribution with no value - maybe due to impossible evidence")

    @staticmethod
    def _pmf_ordered(vps, prob_type=-1, normalization=True, check=True):
        """ static method, returns an Alea instance representing a distribution
            for the given sequence of (val,freq) tuples, where freq is a natural
            number so that each value is taken with the given frequency;
            the values will be stored and displayed in the given order (no sort);
            the method admits 2 optional boolean argument (kwargs):
            * check (default: True): if True and if a value occurs multiple
            times, then an exception is raised;
            requires that each value has a unique occurrence;
            requires at least one value_freqs argument;
        """
        (vs, ps) = zip(*vps)
        Alea._check_not_empty(vs)
        # check duplicates
        if check and len(frozenset(vs)) < len(vs):
            raise LeaError("duplicate values are not allowed for ordered=True")
        return Alea(vs, ps, normalization=normalization, prob_type=prob_type)

    @staticmethod
    def _check_prob(p):
        """ static method checking that given p is a valid probability value,
            i.e. in the range [0,1];
            if comparisons are infeasible on p, then p is assumed to be a
            symbolic probability and is considered valid;
            raises Lea.Error exception if invalid
        """
        try:
            is_valid = 0 <= p <= 1
        except Exception:
            # comparisons are infeasible: we assume that p is a symbolic
            # probability, the range check cannot be enforced
            is_valid = True
        if not is_valid:
            raise LeaError("invalid probability value %s" % (p,))

    @staticmethod
    def _binary_distribution(v1, v2, p2, prob_type=None):
        """ static method, returns an Alea instance representing a boolean
            probability distribution giving v1 with probability 1-p2
            and v2 with probability p2;
            prob_type argument allows converting the probabilities p2 and 1-p2:
              -1: no conversion;
              None (default): default conversion, as set by Alea.set_prob_type;
              other: see doc of get_prob_type;
        """
        prob_type_func = get_prob_type(prob_type)
        if prob_type_func is not None:
            p2 = prob_type_func(p2)
        Alea._check_prob(p2)
        if p2 == 1:
            ## note: do not replace p2 by 1, in order to keep the given type
            (vs, ps) = ((v2,), (p2,))
        elif p2 == 0:
            ## note: do not replace 1-p2 by 1, in order to keep the given type
            (vs, ps) = ((v1,), (1 - p2,))
        else:
            (vs, ps) = ((v1, v2), (1 - p2, p2))
        return Alea(vs, ps, normalization=False, prob_type=-1)

    def is_uniform(self):
        """ returns True  if the probability distribution is uniform,
                    False otherwise
        """
        p0 = self._ps[0]
        return all(p == p0 for p in self._ps)

    def _selections(self, n, gen_selector):
        """ returns a new Alea instance representing a probability distribution of
            the n-length tuples yielded by the given combinatorial generator
            gen_selector, applied on the values of self distribution;
            the order of the elements of each built tuple is irrelevant: each tuple
            represents any permutation of its elements; the actual order of the
            elements of each tuple shall be the one defined by gen_selector;
            assumes that n >= 0;
            the efficient combinatorial algorithm is due to Paul Moore
        """
        # First of all, get the values and weights for the distribution
        vps = dict(self._gen_raw_vps())
        # The total number of permutations of N samples is N!
        permutations = factorial(n)
        # We will calculate the frequency table for the result
        freq_table = []
        # Use gen_selector to get the list of outcomes.
        # as itertools guarantees to give sorted output for sorted input,
        # giving the sorted sequence self._vs ensures our outputs are sorted
        for outcome in gen_selector(self._vs, n):
            # We calculate the weight in 2 stages.
            # First we calculate the weight as if all values were equally
            # likely - in that case, the weight is N!/a!b!c!... where
            # a, b, c... are the sizes of each group of equal values
            weight = permutations
            # We run through the set counting and dividing as we go
            run_len = 0
            prev_roll = None
            for roll in outcome:
                if roll != prev_roll:
                    prev_roll = roll
                    run_len = 0
                run_len += 1
                if run_len > 1:
                    weight //= run_len
            # Now we take into account the relative weights of the values, by
            # multiplying the weight by the product of the weights of the
            # individual elements selected
            for roll in outcome:
                weight *= vps[roll]
            freq_table.append((outcome, weight))
        return pmf(freq_table)

    def draw_sorted_with_replacement(self, n):
        """ returns a new Alea instance representing the probability distribution
            of drawing n elements from self WITH replacement, whatever the order
            of drawing these elements; the returned values are tuples with n
            elements sorted by increasing order;
            assumes that n >= 0;
            the efficient combinatorial algorithm is due to Paul Moore;
        """
        return self._selections(n, itertools.combinations_with_replacement)

    def draw_sorted_without_replacement(self, n):
        """ returns a new Alea instance representing the probability distribution
            of drawing n elements from self WITHOUT replacement, whatever the order
            of drawing these elements; the returned values are tuples with n
            elements sorted by increasing order;
            assumes that 0 <= n <= number of values of self;
            note: if the probability distribution of self is uniform,
            then the results is produced in an efficient way, thanks to the
            combinatorial algorithm of Paul Moore
        """
        if self.is_uniform():
            # the probability distribution is uniform,
            # the efficient algorithm of Paul Moore can be used
            return self._selections(n, itertools.combinations)
        # the probability distribution is not uniform,
        # we use the general algorithm less efficient:
        # make first a draw unsorted then sort (the sort makes the
        # required probability additions between permutations)
        return self.draw_without_replacement(n).map(lambda vs: tuple(sorted(vs))).get_alea()

    def draw_with_replacement(self, n):
        """ returns a new Alea instance representing the probability distribution
            of drawing n elements from self WITH replacement, taking the order
            of drawing into account; the returned values are tuples with n elements
            put in the order of their drawing;
            assumes that n >= 0
        """
        if n == 0:
            return coerce((), prob_type=self._ps[0].__class__)
        return self.map(make_tuple).times(n)

    def draw_without_replacement(self, n):
        """ returns a new Alea instance representing the probability distribution
            of drawing n elements from self WITHOUT replacement, taking the order
            of drawing into account; the returned values are tuples with n elements
            put in the order of their drawing;
            assumes that n >= 0;
            requires that n <= number of values of self, otherwise an exception
            is raised
        """
        if n == 0:
            return coerce((), prob_type=self._ps[0].__class__)
        if len(self._vs) == 1:
            if n > 1:
                raise LeaError("number of values to draw exceeds the number of possible values")
            return coerce((self._vs[0],), prob_type=self._ps[0].__class__)
        alea2s = tuple(Alea._pmf_ordered(tuple((v0, p0) for (v0, p0) in self._gen_raw_vps() if v0 != v),
                                         check=False).draw_without_replacement(n - 1) for v in self._vs)
        vps = []
        for (v, p, alea2) in zip(self._vs, self._ps, alea2s):
            for (vt, pt) in alea2._gen_raw_vps():
                vps.append(((v,) + vt, p * pt))
        return Alea._pmf_ordered(vps, check=False)

    _DISPLAY_KINDS = (None, '/', '.', '%', '-', '/-', '.-', '%-')
    _display_kind = None
    _display_nb_decimals = None
    _display_chart_size = None
    _display_tabular = None
    _display_one_line = None

    def as_string(self, kind=None, nb_decimals=None, chart_size=None, tabular=None, one_line=None):
        """ returns a string representation of probability distribution self;
            it contains by default one line per distinct value, separated by a newline
            character; each line contains the string representation of a value with its
            probability in a format depending of given kind, which is either None
            (default) or a string among
                '/', '.', '%', '-', '/-', '.-', '%-';
            the probabilities are displayed as
            - if kind is None   : as they are stored
            - if kind[0] is '/' : rational numbers "n/d" or "0" or "1"
            - if kind[0] is '.' : decimals with given nb_decimals digits
            - if kind[0] is '%' : percentage decimals with given nb_decimals digits
            - if kind[0] is '-' : histogram bar made up of repeated '-', such that
                                  a bar length of chart_size represents a probability 1
            if kind[1] is '-', the histogram bars with '-' are appended after
                               numerical representation of probabilities;
            if the probability distribution has been created with ordered=True, then
            the values are ordered in the order of their definition, otherwise, if an
            order relationship is defined on values, then the values are sorted by
            increasing order; otherwise, an arbitrary order is used;
            if tabular is True and if values are tuples of same length, then these are
            represented in a tabular format (fixed column width); in the specific cases
            of named tuple, a header line is prepended with the field names;
            if one_line is True, then the values and probabilities are displayed on one
            single line, separated by commas;
            if some arguments are None or not specified, then they take the default values
            specified by call to set_display_options function
        """
        if kind is None:
            if Alea._display_kind is None:
                if all(isinstance(p, Fraction) for p in self._ps):
                    # if probabilities expressed as fractions, force '/' kind to keep same denominotor
                    kind = '/'
            else:
                kind = Alea._display_kind
        if nb_decimals is None:
            nb_decimals = Alea._display_nb_decimals
        if chart_size is None:
            chart_size = Alea._display_chart_size
        if tabular is None:
            tabular = Alea._display_tabular
        if one_line is None:
            one_line = Alea._display_one_line
        if kind not in Alea._DISPLAY_KINDS:
            raise LeaError("invalid display format '%s'; should be among %s" % (kind, Alea._DISPLAY_KINDS))
        if self._val is self:
            # self is not bound (default)
            vs = self._vs
            ps = self._ps
        else:
            # self is explicitly bound - see observe(...) method or .calc(bindings=...)
            vs = (self._val,)
            ps = (1,)
        v0 = vs[0]
        if one_line:
            header = "{ "
            footer = " }"
            sep = ", "
            lines_iter_0 = ("%s: "% (v,) for v in vs)
        else:
            header = ""
            footer = ""
            sep = '\n'
            lines_iter_0 = None
            if tabular and isinstance(v0, tuple):
                v0_class = v0.__class__
                v0_length = len(v0)
                if all((v.__class__ is v0_class and len(v) == v0_length) for v in vs):
                    # values are tuples of same length: perform a tabular display, where column widths
                    # depend on the longest elements
                    repr_vs = tuple(tuple(repr(e) for e in v) for v in vs)
                    if hasattr(v0_class, '_fields'):
                        # values are named tuples, of the same class: prepend the field names tuple for header
                        repr_vs = (v0_class._fields,) + repr_vs
                    # determine max required length per column
                    max_length_per_pos = tuple(max(len(e) for e in a) for a in zip(*repr_vs))
                    if not one_line and hasattr(v0_class, '_fields'):
                        header = " %s\n" % ', '.join(indent(str, e, s)
                                                     for (e, s) in zip(v0._fields, max_length_per_pos))
                    lines_iter_0 = ('(%s)' % ', '.join(indent(repr, e, s)
                                                     for (e, s) in zip(v, max_length_per_pos))
                                                     for v in vs)
            if lines_iter_0 is None:
                # general, non-tabular, display
                vm = max(len(str(v)) for v in vs)
                lines_iter_0 = (indent(str, v, vm) for v in vs)
            lines_iter_0 = ("%s : "%(v,) for v in lines_iter_0)
        body = None
        if kind is not None:
            lines = tuple(lines_iter_0)
            prob_representation = kind[0]
            with_histo = kind[-1] == '-'
            try:
                if prob_representation == '/':
                    (pnums, pdenom) = ExtFraction.convert_to_same_denom(tuple(Fraction(p) for p in ps))
                    p_strings = tuple(str(pnum) for pnum in pnums)
                    if one_line:
                        pnum_size_max = 0
                    else:
                        pnum_size_max = len(str(max(pnum for pnum in pnums)))
                    if pdenom == 1:
                        den = ''
                    else:
                        den = '/%d' % pdenom
                    lines_iter = (line + p_string.rjust(pnum_size_max) + den
                                  for (line, p_string) in zip(lines, p_strings))
                elif prob_representation == '.':
                    fmt = "%%s%%.%df" % (nb_decimals,)
                    lines_iter = (fmt % (line, p) for (line, p) in zip(lines, ps))
                elif prob_representation == '%':
                    fmt = "%%s%%%d.%df %%%%" % (4 + nb_decimals, nb_decimals)
                    lines_iter = (fmt % (line, 100 * p) for (line, p) in zip(lines, ps))
                if with_histo:
                    lines_iter = (line + ' ' + int(0.5 + (p) * chart_size) * '-'
                                  for (line, p) in zip(lines_iter, ps))
                body = sep.join(lines_iter)
            except Exception:
                # failed formatting: sympy expression assumed in probability
                lines_iter_0 = iter(lines)
        if body is None:
            # kind is None or sympy expression encountered:
            # use simplest, default, representation
            body = sep.join(line + str(p) for (line, p) in zip(lines_iter_0, ps))
        return header + body + footer

    def as_float(self, nb_decimals=6):
        """ returns a string representation of probability distribution self;
            it contains one line per distinct value, separated by a newline character;
            each line contains the string representation of a value with its
            probability expressed as decimal with given nb_decimals digits;
            if an order relationship is defined on values, then the values are sorted by
            increasing order; otherwise, an arbitrary order is used;
        """
        return self.as_string('.', nb_decimals)

    def as_pct(self, nb_decimals=2):
        """ returns a string representation of probability distribution self;
            it contains one line per distinct value, separated by a newline character;
            each line contains the string representation of a value with its
            probability expressed as percentage with given nb_decimals digits;
            if an order relationship is defined on values, then the values are sorted by
            increasing order; otherwise, an arbitrary order is used;
        """
        return self.as_string('%', nb_decimals)

    def histo(self, size=100):
        """ returns a string representation of probability distribution self;
            it contains one line per distinct value, separated by a newline character;
            each line contains the string representation of a value with its
            probability expressed as a histogram bar made up of repeated '-',
            such that a bar length of given size represents a probability 1;
            if an order relationship is defined on values, then the values are sorted by
            increasing order; otherwise, an arbitrary order is used;
        """
        return self.as_string('-', chart_size=size)

    def plot(self, title=None, fname=None, savefig_args={}, **bar_args):
        """ produces a matplotlib bar chart representing the probability distribution self
            with the given title (if not None); the bar chart may be customized by using
            named arguments bar_args, which are relayed to matplotlib.pyplot.bar function
            (see doc in http://matplotlib.org/api/pyplot_api.html);
            * if fname is None, then the chart is displayed on screen, in a matplotlib window;
              the previous chart, if any, is erased
            * otherwise, the chart is saved in a file specified by given fname as specified
              by matplotlib.pyplot.savefig; the file format may be customized by using
              savefig_args argument, which is a dictionary relayed to matplotlib.pyplot.savefig
              function and containing named arguments expected by this function;
              example:
               flip.plot(fname='flip.png',savefig_args=dict(bbox_inches='tight'),color='green')
            the method requires matplotlib package; an exception is raised if it is not installed
        """
        # try to import matplotlib package, required by plot() method
        if plt is None:
            raise LeaError("the plot() method requires the matplotlib package")
        # switch on interactive mode, so the control is back to console as soon as a chart is displayed
        plt.ion()
        if fname is None:
            # no file specified: erase the current chart, if any
            plt.clf()
        else:
            # file specified: switch off interactive mode
            plt.ioff()
        plt.bar(range(len(self._vs)), self._ps, tick_label=self._vs, align='center', **bar_args)
        plt.ylabel('Probability')
        if title is not None:
            plt.title(title)
        if fname is None:
            # no file specified: display the chart on screen
            plt.show()
        else:
            # file specified: save chart on file, using given parameters and switch back interactive mode
            plt.savefig(fname, **savefig_args)
            # TODO: needed?
            plt.ion()

    def support(self):
        """ returns a tuple with values of self
            the sequence follows the increasing order defined on values;
            if order is undefined (e.g. complex numbers), then the order is
            arbitrary but fixed from call to call
        """
        return self._vs

    def ps(self):
        """ returns a tuple with probability of self
            the sequence follows the increasing order defined on values;
            if order is undefined (e.g. complex numbers), then the order is
            arbitrary but fixed from call to call
        """
        return tuple(Alea._downcast(p) for p in self._ps)

    def pmf_tuple(self):
        """ returns, after evaluation of the probability distribution self, the probability
            mass function of self, as a tuple with tuples (v,P(v));
            the sequence follows the order defined on values
        """
        return tuple(self._gen_vps())

    def pmf_dict(self):
        """ returns, after evaluation of the probability distribution self, the probability
            mass function of self, as an OrderedDict with v : P(v)) pairs;
            the sequence follows the order defined on values
        """
        return OrderedDict(self._gen_vps())

    def cdf_tuple(self):
        """ returns, after evaluation of the probability distribution self, the cumulative
            distribution function of self, as a tuple with tuples (v,P(x<=v));
            the sequence follows the order defined on values;
        """
        return tuple((v, Alea._downcast(p)) for (v, p) in zip(self._vs, self.cumul()[1:]))

    def cdf_dict(self):
        """ returns, after evaluation of the probability distribution self, the cumulative
            distribution function of self, as an OrderedDict with v : P(x<=v)) pairs;
            the sequence follows the order defined on values
        """
        return OrderedDict((v, Alea._downcast(p)) for (v, p) in zip(self._vs, self.cumul()[1:]))

    def _get_lea_children(self, restricted=False):
        """ see Lea._get_lea_children
        """
        # Alea instance has no children
        return ()

    def _clone_by_type(self, clone_table):
        """ see Lea._clone_by_type
        """
        # note that the new Alea instance shares the immutable _vs and _ps attributes of self
        return Alea(self._vs, self._ps, normalization=False, prob_type=-1)

    def _gen_vp(self):
        """ see Lea._gen_vp
        """
        return zip(self._vs, self._ps)

    def _gen_one_random_mc(self):
        """ see Lea._gen_one_random_mc
        """
        yield self.random_val()

    def _em_step(self, model_lea, cond_lea, obs_pmf_tuple, conversion_dict):
        """ see Lea._em_step
        """
        if cond_lea is True:
            return pmf(dict((v, sum(px * ((self == v).given(model_lea == vx))._p(True)
                                    for (vx, px) in obs_pmf_tuple))
                            for v in self.support()))
        return pmf(dict((v, sum(px * (((self == v) & cond_lea).given(model_lea == vx))._p(True)
                                for (vx, px) in obs_pmf_tuple))
                        for v in self.support()))

    def is_bindable(self, v):
        """ see Lea.is_bindable
        """
        return self._val is self and v in self._vs

    def observe(self, v):
        """ (re)bind self with given value v;
            requires that self is an Alea instance (i.e. independent of other Lea instances);
            requires that v is present in the domain of self
        """
        if v not in self._vs:
            raise LeaError("impossible to bind %s with '%s' because it is out of domain" % (self._id(), v))
        self._val = v

    def free(self, check=True):
        """ unbind self;
            requires that self is an Alea instance (i.e. independent of other Lea instances);
            if check is True, then requires that self is bound
        """
        if check and not self.is_bound():
            raise LeaError("%s already unbound" % (self._id(),))
        self._val = self

    def _p(self, val, check_val_type=False):
        """ returns the probability p of the given value val;
            if check_val_type is True, then raises an exception if some value
            in the distribution has a type incompatible with val's
        """
        p1 = None
        if check_val_type:
            err_val = self  # dummy value
            type_to_check = type(val)
        for (v, p) in self._gen_vp():
            # check that all values have a common ancestor with val's type;
            # to avoid spurious error when using numpy, the numpy's bool_ is considered compatible with Python's bool
            if check_val_type and not isinstance(v, type_to_check) \
                    and not (type_to_check is bool and isinstance(v, np_bool_type)):
                err_val = v
            if p1 is None and v == val:
                p1 = p
        if check_val_type and err_val is not self:
            raise LeaError(
                "found <%s> value although <%s> is expected" % (type(err_val).__name__, type_to_check.__name__))
        if p1 is None:
            # val is absent from self: the probability is null, casted in the type of the last probability found
            p1 = 0 * p
        return p1

    def cumul(self):
        """ returns a list with the probabilities p that self <= value ;
            there is one element more than number of values; the first element is 0, then
            the sequence follows the order defined on values; if an order relationship is defined
            on values, then the tuples follows their increasing order; otherwise, an arbitrary
            order is used, fixed from call to call;
            Note: the returned list is cached
        """
        if len(self._cumul) == 1:
            cumul_list = self._cumul
            p_sum = 0
            for p in self._ps:
                p_sum += p
                cumul_list.append(p_sum)
        return self._cumul

    def inv_cumul(self):
        """ returns a tuple with the probabilities p that self >= value ;
            there is one element more than number of values; the first element is 0, then
            the sequence follows the order defined on values; if an order relationship is defined
            on values, then the tuples follows their increasing order; otherwise, an arbitrary
            order is used, fixed from call to call;
            Note: the returned list is cached
        """
        if len(self._inv_cumul) == 0:
            inv_cumul_list = self._inv_cumul
            p_sum = 1
            for p in self._ps:
                inv_cumul_list.append(p_sum)
                p_sum -= p
            inv_cumul_list.append(0)
        return self._inv_cumul

    def random_val(self):
        """ returns a random value among the values of self, according to their probabilities
        """
        return next(self._random_iter)

    def _create_random_iter(self):
        """ generates an infinite sequence of random values among the values of self,
            according to their probabilities
        """
        try:
            probs = tuple(map(float, self.cumul()[1:]))
        except Exception:
            raise LeaError("random sampling impossible because given probabilities cannot be converted to float")
        vs = self._vs
        while True:
            yield vs[bisect_right(probs, random())]

    def random_draw(self, n=None, sorted=False):
        """ if n is None, returns a tuple with all the values of the distribution,
            in a random order respecting the probabilities;
            (the higher probability of a value, the more likely the value will be in the
             beginning of the sequence);
            if n > 0, then only n different values will be drawn;
            if sorted is True, then the returned tuple is sorted
        """
        if n is None:
            n = len(self._vs)
        elif n < 0:
            raise LeaError("random_draw method requires a positive integer")
        if n == 0:
            return ()
        lea1 = self
        res = []
        while True:
            lea1 = lea1.get_alea(sorting=False)
            x = lea1.random()
            res.append(x)
            n -= 1
            if n == 0:
                break
            lea1 = lea1.given(lea1 != x)
        if sorted:
            res.sort()
        return tuple(res)

    @memoized_method
    def p_cumul(self, val):
        """ returns, as an integer, the probability that self <= val;
            note that it is not required that val is in the support of self
        """
        return self.cumul()[bisect_right(self._vs, val)]

    @memoized_method
    def p_inv_cumul(self, val):
        """ returns, as an integer, the probability that self >= val;
            note that it is not required that val is in the support of self
        """
        return self.inv_cumul()[bisect_left(self._vs, val)]

    @staticmethod
    def fast_extremum(cumul_func, *alea_args):
        """ static method, returns a new Alea instance giving the probabilities
            to have the extremum value (min or max) of each combination of the
            given Alea args;
            cumul_func is the cumul function that determines whether max or min is
            used : respectively, Alea.p_cumul or Alea.p_inv_cumul;
            the method uses an efficient algorithm (linear complexity), which is
            due to Nicky van Foreest
        """
        if len(alea_args) == 1:
            return alea_args[0]
        if len(alea_args) == 2:
            (alea_arg1, alea_arg2) = alea_args
            pmf_dict = defaultdict(int)
            for (v, p) in alea_arg1._gen_raw_vps():
                p1 = cumul_func(alea_arg2, v)
                if p1 != 0:
                    pmf_dict[v] = p * p1
            for (v, p) in alea_arg2._gen_raw_vps():
                p1 = cumul_func(alea_arg1, v) - alea_arg1._p(v)
                if p1 != 0:
                    pmf_dict[v] += p1 * p
            return pmf(pmf_dict)
        return Alea.fast_extremum(cumul_func, alea_args[0], Alea.fast_extremum(cumul_func, *alea_args[1:]))

    @staticmethod
    def _downcast(x):
        """ static method, returns x or an object equivalent to x, more convenient to display:
             Fraction -> ExtFraction,
             Decimal  -> ExtDecimal
        """
        downcast_class = Alea.__downcast_class.get(x.__class__)
        if downcast_class is None:
            return x
        return downcast_class(x)

    def p_sum(self):
        """ returns the sum of all probabilities of self;
            the result is expressed in the probability type used in self,
            possibly downcasted for convenience (Fraction -> ExtFraction,
            Decimal -> ExtDecimal);
            note: the result is supposed to be 1 (expressed in some type);
            BUT it could be different:
            - due to float rounding-errors
            - due to an explicit normalization=False argument;
        """
        ## note that the following expression is NOK for unorderable types (e.g. complex)
        ##   self.p_cumul(self._vs[-1])
        return Alea._downcast(Alea._simplify(sum(self._ps)))

    def P(self):
        """ returns the probability that self is True;
            the probability is expressed in the probability type used in self,
            possibly downcasted for convenience (Fraction -> ExtFraction,
            Decimal -> ExtDecimal);
            raises an exception if some value in the distribution is not boolean
            (note that this is NOT the case with self.p(True));
        """
        p = self._p(True, check_val_type=True)
        if Alea._display_kind is not None:
            prob_representation = Alea._display_kind[0]
            try:
                if prob_representation in '.%':
                    return ExtDecimal.coerce(p, (prob_representation=='%'))
                if prob_representation == '/':
                    return ExtFraction.coerce(p)
            except Exception:
                # conversion has failed: sympy expression assumed
                return p
        return Alea._downcast(p)

    def Pf(self):
        """ returns the probability that self is True;
            the probability is expressed as a float between 0.0 and 1.0;
            raises an exception if the probability type is no convertible to float;
            raises an exception if some value in the distribution is not boolean;
            (this is NOT the case with self.p(True));
        """
        return float(self._p(True, check_val_type=True))

    def _mean(self):
        """ same as mean method but without conversion nor simplification
        """
        res = None
        v0 = None
        for (v, p) in self._gen_raw_vps():
            if v0 is None:
                v0 = v
            elif res is None:
                res = p * (v - v0)
            else:
                res += p * (v - v0)
        if res is not None:
            v0 += res
        return v0

    def mean(self):
        """ returns the mean value of the probability distribution, which is the
            probability weighted sum of the values;
            requires that
            1 - the values can be subtracted together,
            2 - the differences of values can be multiplied by integers,
            3 - the differences of values multiplied by integers can be
                added to the values,
            4 - the sum of values calculated in 3 can be divided by a float
                or an integer;
            if any of these conditions is not met, then the result depends on the
            value class implementation (likely, raised exception);
        """
        return Alea._downcast(Alea._simplify(self._mean(), self._vs[0].__class__))

    def mean_f(self):
        """ same as mean method but with conversion to float or simplification of symbolic expression;
        """
        return Alea._simplify(self._mean(), float)

    def _var(self):
        """ same as var method but without conversion nor simplification
        """
        res = 0
        m = self._mean()
        for (v, p) in self._gen_raw_vps():
            res += p * (v - m) ** 2
        return res

    def var(self):
        """ returns the variance of the probability distribution;
            requires that
            1 - the requirements of the mean() method are met,
            2 - the values can be subtracted to the mean value,
            3 - the differences between values and the mean value can be squared;
            if any of these conditions is not met, then the result depends on the
            value implementation (likely, raised exception)
        """
        return Alea._downcast(Alea._simplify(self._var(), self._vs[0].__class__))

    def var_f(self):
        """ same as var method but with conversion to float or simplification of symbolic expression;
        """
        return Alea._simplify(self._var(), float)

    def _std(self):
        """ same as std method but without conversion nor simplification
        """
        var = self._var()
        sqrt_exp = var.__class__(0.5)
        return var ** sqrt_exp

    def std(self):
        """ returns the standard deviation of the probability distribution
            requires that the requirements of the var method are met;
        """
        return Alea._downcast(Alea._simplify(self._std(), self._vs[0].__class__))

    def std_f(self):
        """ same as std method but with conversion to float or simplification
            of symbolic expression;
        """
        return Alea._simplify(self._std(), float)

    def mode(self):
        """ returns a tuple with the value(s) of the probability distribution
            having the highest probability;
        """
        max_p = max(self._ps)
        return tuple(v for (v, p) in self._gen_raw_vps() if p == max_p)

    def information_of(self, val):
        """ returns a float number representing the information of given val,
            expressed in bits:
               log2(P(self==val))
            assuming that probability of val is (convertible to) float;
            if probability of val is a sympy expression, then the returned
            object is the information of val as a sympy expression;
            raises an exception if given val is impossible;
            raises an exception if probability of given val is neither;
            convertible to float nor a sympy expression
        """
        p = self._p(val)
        try:
            if p == 0:
                raise LeaError("no information from impossible value")
            return -log2(p)
        except TypeError:
            try:
                return -sympy.log(p, 2)
            except Exception:
                raise LeaError("cannot calculate logarithm of %s" % (p,))

    def information(self):
        """ returns the information of self being true, expressed in bits
            assuming that self is a boolean distribution;
            the returned type is a float or a sympy expression (see doc of
            Alea.entropy);
            raises an exception if self is certainly false;
        """
        return self.information_of(True)

    def entropy(self):
        """ returns the entropy of self in bits;
            if all probabilities are (convertible to) float, then the entropy
            is returned as a float;
            if any probability is a sympy expression, then the entropy is
            returned as a sympy expression;
            raises an exception if some probabilities are neither convertible
            to float nor a sympy expression;
        """
        res = 0
        try:
            for (_, p) in self._gen_raw_vps():
                if p > 0:
                    res -= p * log2(p)
            return res
        except TypeError:
            # sympy exception assumed: no ceiling
            try:
                for (_, p) in self._gen_raw_vps():
                    res -= p * sympy.log(p)
                return res / sympy.log(2)
            except Exception:
                raise LeaError("cannot calculate logarithm on given probability types")

    def rel_entropy(self):
        """ returns the relative entropy of self;
            if all probabilities are (convertible to) float, then the relative
            entropy is returned as a float between 0.0 and 1.0;
            if any probability is a sympy expression, then the relative entropy
            is returned as a sympy expression;
            raises an exception if some probabilities are neither convertible
            to float nor a sympy expression;
        """
        n = len(self._vs)
        if n == 1:
            return 0.0
        entropy = self.entropy()
        try:
            return min(1.0, entropy / log2(n))
        except TypeError:
            # sympy exception assumed: no ceiling
            return entropy / sympy.log(n, 2)

    def cross_entropy(self, lea1):
        """ static method, returns the cross-entropy between self and given lea1;
            the logarithm base is 2;
            requires that all values of lea1's support have a non-null probability in self;
            notes:
            - the cross-entropy is non-commutative;
            - the cross-entropy should always be greater than the entropy of first argument,
              the equality being reached if both arguments have same pmf; this is guaranteed
              by the implementation, even in case of rounding errors;
            - if self is interpreted as frequencies of observed data having N as total number
              of samples, then the cross-entropy is linked to (negative) log-likelihood by
                log-likelihood = - N * cross-entropy
              using logarithm in base 2 (for other base, use the right factor)
        """
        lea1_pmf_dict = coerce(lea1).pmf_dict()
        try:
            ce = -sum(px * log2(lea1_pmf_dict[vx]) for (vx, px) in self._gen_vps() if px > 0)
        except KeyError as key_error:
            raise LeaError("observed value '%s' is not produced by given model" % (key_error.args[0],))
        except ValueError:
            raise LeaError("some observed value has null probability in given model")
        except Exception:
            # sympy exception assumed due to log function or test px > 0:
            # retry using sympy log funtion and without test clause
            ce = -sum(px * sympy.log(lea1_pmf_dict[vx]) for (vx, px) in self._gen_vps()) / sympy.log(2)
        try:
            return max(ce, self.entropy())
        except TypeError:
            # sympy exception assumed: no ceiling
            return ce

    def redundancy(self):
        """ returns the redundancy of self;
            if all probabilities are (convertible to) float, then the
            redundancy is returned as a float between 0.0 and 1.0;
            if any probability is a sympy expression, then the redundancy
            is returned as a sympy expression;
            raises an exception if some probabilities are neither convertible
            to float nor a sympy expression;
        """
        return 1.0 - self.rel_entropy()

    def internal(self, with_names=False, full=False, _indent='', _refs=None,
                 _client_name_by_obj_dict=None):
        """ returns a string representing the inner definition of self;
            if the same lea child appears multiple times, it is expanded only
            on the first occurrence, the other ones being marked with
            reference id;
            if full is False (default), then only the first element of Alea
            instances is displayed, otherwise all elements are displayed;
            the other arguments are used only for recursive calls made in
            Lea.internal method, they can be ignored for a normal usage;
            if there is some active evidence context, the returned string
            shows, instead of self's, the internals of a new Ilea instance
            embedding self and conditioned by the evidence context;
        """
        if with_names and _client_name_by_obj_dict is None \
                      and Lea._client_obj_by_name_dict is not None:
            _client_name_by_obj_dict = {self: name
                                        for (name, obj) in Lea._client_obj_by_name_dict.items()
                                        if obj is self}
        if _refs is None:
            _refs = set()
            lea1 = self._get_lea_to_evaluate()
            if lea1 is not self:
                return lea1.internal(with_names, full, _indent, _refs, _client_name_by_obj_dict)
        if self in _refs:
            return self._name(_client_name_by_obj_dict, "*")
        _refs.add(self)
        vps = tuple(self._gen_raw_vps())
        res = "%s: { %r: %s" % ((self._name(_client_name_by_obj_dict),) + vps[0])
        if len(vps) >= 2:
            res += ', '
            if full:
                res += ', '.join("%r: %s"%vp for vp in (vps[1:]))
            else:
                res += '...'
        res += ' }'
        return res

# public functions

def coerce(value, prob_type=-1):
    """ returns a Lea instance corresponding to the given value:
        if the value is a Lea instance, then it is returned as-is
        otherwise, a new Alea instance is returned, with given value
        as unique value, with a probability of 1.
        if prob_type is -1,
           then the returned Alea instance has integer 1 as probability;
           otherwise, the returned Alea instance has probability 1
           converted according to prob_type (see doc of Alea.set_prob_type)
    """
    if isinstance(value, Lea):
        return value
    # build a singleton value, with probability 1
    ## note: do not put something else than 1, as an integer,
    ## which is the highest arithmetic class in class hierarchy
    return Alea((value,), (1,), normalization=False, prob_type=prob_type)

def event(p, prob_type=None):
    """ returns an Alea instance representing a boolean probability distribution
        giving True with probability p and False with probability 1-p;
        prob_type argument allows converting the given probability p:
          -1: no conversion;
          None (default): default conversion, as set by Alea.set_prob_type;
          other: see doc of get_prob_type;
    """
    return Alea._binary_distribution(False, True, p, prob_type)

def pmf(arg, prob_type=None, ordered=False, sorting=None, normalization=True, check=None):
    """ returns an Alea instance representing a probability distribution for
        a probability mass function specified by the given arg, which is
          either a dictionary { v1:p1, ... , vn:pn }
          or an iterable of pairs (v1,p1), ... , (vn,pn)
        pi is the probability of occurrence of vi or a number proportional
        to it (see normalization argument below);
        in the iterable case, if the same value v occurs multiple times,
        then the associated p are summed together;
        * prob_type argument allows converting the given probabilities:
          -1: no conversion;
          None (default): default conversion, as set by Alea.set_prob_type;
          other: see doc of get_prob_type;
        the method admits three other optional boolean argument (in kwargs):
        * ordered (default:False): if ordered is True, then the values for
        displaying the distribution or getting the values will follow the
        given order (requires that the arg is an iterable or a
        collections.OrderedDict);
        * sorting (default:not ordered): if True, then the values for displaying
        the distribution or getting the values will be sorted if possible
        (i.e. no exception on sort); otherwise, the order of values is
        unspecified unless ordered=True;
        * normalization (default:True): if True, then each element
        of the given ps is divided by the sum of all ps before being stored
        (in such case, it's not mandatory to have true probabilities for ps
        elements; these could be simple counters, for example);
        requires that all the given values vi are hashable;
        requires that prob_dict is not empty;
        requires that ordered and sorting are not set to True together
    """
    if sorting is None:
        sorting = not ordered
    elif ordered and sorting:
        raise LeaError("ordered and sorting arguments cannot be set to True together")
    if isinstance(arg, dict):
        prob_dict = arg
        if ordered and not isinstance(prob_dict, OrderedDict):
            raise LeaError("ordered=True requires to provide an OrderedDict")
        Alea._check_not_empty(prob_dict)
    else:
        vps = arg
        if ordered:
            if check is None:
                check = True
            return Alea._pmf_ordered(vps, prob_type=prob_type, normalization=normalization, check=check)
        prob_dict = defaultdict(int)
        prob_type_func = get_prob_type(prob_type)
        if prob_type_func is None:
            # no probability conversion required
            for (v, p) in vps:
                prob_dict[v] += p
        else:
            # probability conversion required
            for (v, p) in vps:
                prob_dict[v] += prob_type_func(p)
        ## note: since probability conversions have been done (if required),
        ## putting prob_type=-1 avoids unnecessary conversion in the subsequent calls
        prob_type = -1
    Alea._check_not_empty(prob_dict)
    vps = prob_dict.items()
    if sorting:
        vps = list(vps)
        try:
            vps.sort()
        except Exception:
            # no ordering relationship on values (e.g. complex numbers)
            pass
    prob_type_func = get_prob_type(prob_type)
    if prob_type_func is not None:
        ## the 'p and ...' below returns None if p is None
        ## this allows for one undefined probability value, to be calculated by complement to 1
        vps = ((v, p and prob_type_func(p)) for (v, p) in vps)
    return Alea(*zip(*vps), normalization=normalization, prob_type=-1)

def vals(*values, prob_type=None, ordered=False, sorting=None, normalization=True, check=True):
    """ returns an Alea instance representing a distribution for the given
        values, so that each value occurrence is taken as equiprobable;
        if each value occurs exactly once, then the probability distribution
        is uniform, i.e. the probability of each value is equal to 1 / #values;
        otherwise, the probability of each value is equal to its frequency in
        the sequence; the optional arguments are: prob_type, ordered,
        sorting, normalization, check;
        see doc of pmf static method;
        requires at least one vals argument
    """
    return pmf(((val, 1) for val in values), prob_type=prob_type, sorting=sorting, ordered=ordered,
                                             normalization=normalization, check=check)

def bernoulli(p, prob_type=None):
    """ returns an Alea instance representing a Bernoulli distribution giving 1
        with probability p and 0 with probability 1-p;
        prob_type argument allows converting the given probability p:
          -1: no conversion;
          None (default): default conversion, as set by Alea.set_prob_type;
          other: see doc of get_prob_type;
    """
    return Alea._binary_distribution(0, 1, p, prob_type)

def interval(from_val, to_val, prob_type=None):
    """ returns an Alea instance representing a uniform probability distribution
        for all the integers in the interval [from_val, to_val]
        the given prob_type, if not None, allows using a probability type different
        from the default one (float or any one set by Alea.set_prob_type)
        - see doc of set_prob_type
    """
    return vals(*range(from_val, to_val + 1), prob_type=prob_type)

def set_prob_type(prob_type):
    """ change the representation of probability values for newly created Lea
        instances, according to the given prob_type;
        if prob_type is a callable object, then it is set as such;
        otherwise, the given prob_type is a code interpreted as follows:
        - 'f' -> float (instance of Python's float) - default
        - 'd' -> decimal (instance of Python's decimal.Decimal)
        - 'r' -> rational (instance of Python's fractions.Fraction)
        - 's' -> symbolic (instance of a sympy Symbol)
                 - see Alea._create_prob_symbol method
        - 'x' -> any: if probability given in a string, then determines
                 the type from it (decimal, rational or symbol) and
                 convert into it;
                 otherwise, takes the object as-is
                 - see Alea._create_prob_obj method
        requires that a prob_type is a callable or a code among the ones
        given above
    """
    if prob_type is None or prob_type == -1:
        raise LeaError("Alea.set_prob_type does not allow %s as argument" % (prob_type,))
    Alea._prob_type = get_prob_type(prob_type)

def read_csv_file(csv_file, col_names=None, dialect='excel', prob_type=None, sorting=True,
                  ordered=False, normalization=True, create_vars=False, **fmtparams):
    """ returns an Alea instance representing the joint probability distribution
        of the data read in the given CSV file;
        if csv_file is a string, then it is interpreted as a filename,
        otherwise, csv_file is interpreted as a file object ready to be read;
        the arguments follow the same semantics as those of Python's csv.reader
        method, which supports different CSV formats;
        see doc in http://docs.python.org/3/library/csv.html
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
              name,age{i},heigth{f},married{b}
        * if col_names is not None, then col_names shall be a sequence of strings giving
          attribute information as described above, e.g.
              ('name','age{i}','heigth{f}','married{b}')
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
        same row multiple times;
        if create_vars is True (default: False), then variables named as column names are
        created in the dictionary passed to last call to lea.declare_namespace, typically
        by the call lea.declare_namespace(globals())
    """
    if isinstance(csv_file, str):
        (attr_names, vps) = read_csv_filename_counts(csv_file, col_names, dialect, **fmtparams)
    else:
        (attr_names, vps) = read_csv_file_counts(csv_file, col_names, dialect, **fmtparams)
    return pmf(vps, prob_type=prob_type, sorting=sorting, ordered=ordered, normalization=normalization)\
           .as_joint(*attr_names, create_vars=create_vars)

def read_pandas_df(dataframe, index_col_name=None, create_vars=False, **kwargs):
    """ returns an Alea instance representing the joint probability
        distribution from the given pandas dataframe;
        the attribute names of the distribution are those of the column of the
        given dataframe; the first field in each item of the dataframe is assumed
        to be the index; its treatment depends on given index_col_name:
        if index_col_name is None, then this index field is ignored;
        otherwise, it is put in the joint distribution with index_col_name as
        attribute name;
        if create_vars is True (default: False), then variables named as the
        dataframe's attribute names are created in the dictionary passed to last call
        to lea.declare_namespace, typically by the call lea.declare_namespace(globals())
    """
    # TODO: retrieve index_col in df, if not 0
    attr_names = tuple(dataframe.columns)
    if index_col_name is None:
        values_iter = (t[1:] for t in dataframe.itertuples())
        attr_names = dataframe.columns
    else:
        values_iter = dataframe.itertuples()
        attr_names = (index_col_name,) + attr_names
    return vals(*values_iter, **kwargs).as_joint(*attr_names, create_vars=create_vars)

def get_prob_type(prob_type):
    """ returns the class or function associated to given code, this
        class or function is applied to convert each probability given
        in an Alea constructor method;
        if prob_type is -1, then None is returned;
        if prob_type is a callable object, then it is returned as-is;
        if prob_type is None, then current prob_type configured by
           Alea.set_prob_type is returned;
        otherwise, the given prob_type is a code interpreted as follows:
        - 'f' -> float (instance of Python's float)
        - 'd' -> decimal (instance of Python's decimal.Decimal)
        - 'r' -> rational (instance of Python's fractions.Fraction)
        - 's' -> symbolic (instance of a sympy Symbol)
                 - see Alea._create_prob_symbol method
        - 'x' -> any: if probability given in a string, then determines
                 the type from it (decimal, rational or symbol) and
                 converts into that type;
                 otherwise, takes the object as-is
                 - see Alea._create_prob_obj method
        requires that prob_type is -1 or None or a callable or a code
        among the ones given above
    """
    if prob_type is None:
        return Alea._prob_type
    if prob_type == -1:
        return None
    if not isinstance(prob_type, str):
        if not callable(prob_type):
            raise LeaError("given prob_type '%s' is not a probability type code and it is not callable" % (prob_type,))
        return prob_type
    if prob_type == 'f':
        return float
    if prob_type == 'r':
        return Fraction
    if prob_type == 'd':
        return Decimal
    if prob_type == 's':
        if sympy is None:
            raise LeaError("prob_type 's' requires the installation of SymPy module")
        return Alea._create_prob_symbol
    if prob_type == 'x':
        return Alea._create_prob_obj
    raise LeaError("unknown probability type code '%s', should be 'f', 'd', 'r', 's' or 'x'" % (prob_type,))

def set_display_options(kind=-1, nb_decimals=-1, chart_size=-1, tabular=-1, one_line=-1):
    """ set default option values used for displaying probability distribution;
        see as_string method for a definition of each of the arguments;
        if some arguments are -1 or are not specified in the call, then these remain unchanged;
        if some arguments are None, then the corresponding options se are reset with following
        default values:
        * kind = None
        * nb_decimals = 6
        * chart_size = 100
        * tabular = True
        * one_line = False
    """
    if kind != -1:
        if kind is not None and kind not in Alea._DISPLAY_KINDS:
            raise LeaError("invalid display format '%s'; should be among %s" % (kind, Alea._DISPLAY_KINDS))
        Alea._display_kind = kind
    if nb_decimals != -1:
        Alea._display_nb_decimals = 6 if nb_decimals is None else nb_decimals
        ExtDecimal._display_nb_decimals = Alea._display_nb_decimals
    if chart_size != -1:
        Alea._display_chart_size = 100 if chart_size is None else chart_size
    if tabular != -1:
        Alea._display_tabular = True if tabular is None else tabular
    if one_line != -1:
        Alea._display_one_line = False if one_line is None else one_line


# set display options default values
set_display_options(None, None, None, None, None)


__all__ = ("coerce", "event", "pmf", "vals", "bernoulli", "interval", "set_prob_type",
           "read_csv_file", "read_pandas_df", "set_display_options")
