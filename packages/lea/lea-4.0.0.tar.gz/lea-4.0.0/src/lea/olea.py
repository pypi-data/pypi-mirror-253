"""
--------------------------------------------------------------------------------

    olea.py

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
from .alea import get_prob_type


class Olea(Lea):
    """
    Olea is a Lea subclass, which instance represents a binomial distribution
    giving the number of successes among a number n of independent experiments,
    each having probability p of success
    """

    __slots__ = ('n', 'prob')

    def __init__(self, n, p, prob_type=None):
        Lea.__init__(self)
        self.n = n
        prob_type_func = get_prob_type(prob_type)
        self.prob = p if prob_type_func is None else prob_type_func(p)

    def _get_lea_children(self, restricted=False):
        return ()

    def _clone_by_type(self, clone_table):
        return Olea(self.n, self.prob, -1)

    def _gen_vp(self):
        n = self.n
        p = self.prob
        if p == 0:
            yield (0, 1 - p)
        elif p == 1:
            yield (n, p)
        else:
            pdq = p / (1 - p)
            pk = (1 - p) ** n
            for k in range(n + 1):
                yield (k, pk)
                pk *= (pdq * (n - k)) / (k + 1)

    def _gen_one_random_mc(self):
        for v in self.get_alea().gen_one_random_mc():
            yield v

    def _em_step(self, model_lea, cond_lea, obs_pmf_tuple, conversion_dict):
        if cond_lea is True:
            vps = obs_pmf_tuple
        else:
            vps = tuple((vx, px * (cond_lea.given(model_lea == vx)).p(True)) for (vx, px) in obs_pmf_tuple)
        n = self.n
        p = sum(px * vx / n for (vx, px) in vps) / sum(px for (_, px) in vps)
        return Olea(n, p, -1)


def binom(n, p, prob_type=None):
    """ returns an Olea instance representing a binomial
        distribution giving the number of successes among a number n of
        independent experiments, each having probability p of success;
        note: the binom method generalizes the bernoulli method:
          binom(1,p) is the same as bernoulli(p)
        prob_type argument allows converting the given probability p:
          -1: no conversion;
          None (default): default conversion, as set by Alea.set_prob_type;
          other: see doc of Alea.get_prob_type;
    """
    return Olea(n, p, prob_type)


__all__ = ("binom",)
