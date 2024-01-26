import numpy
import simpful as sf
from numpy import array
from scipy.interpolate import interp1d

"""
Module to manage and representing Interval-Valued Membership Functions
"""


class MF_object_2(object):
    """
    Class representing Interval-Valued Membership Function
    """

    def __init__(self):
        """
        Constructor method
        """
        pass

    def __call__(self, x):
        """
        Overriding the __call__ method
            :param x:
            :type x: tuple,int
            :return: membership x to define function
            :rtype: tuple, int
        """
        if type(x) is tuple:
            ret1 = self._execute(x[0])
            ret2 = self._execute(x[1])
            return min(1, max(0, ret1)), min(1, max(0, ret2))
        else:
            return sf.MF_object.__call__(self, x)


class Triangular_MF_2(MF_object_2):
    """
    Class representing Interval-Valued Triangular Membership Function
        :param a: y coordinate for point on start Interval-Valued Triangular Membership Function
        :type a: float
        :param b: y coordinate for point on top Interval-Valued Triangular Membership Function
        :type b: float
        :param c: y coordinate for point on end Interval-Valued Triangular Membership Function
        :type c: float
    """

    def __init__(self, a=0, b=0.5, c=1):
        """
        Constructor method
        """
        self._a = a
        self._b = b
        self._c = c
        if (a > b):
            raise Exception("Error in triangular fuzzy set: a=%.2f should be <= b=%.2f" % (a, b))
        elif (b > c):
            raise Exception("Error in triangular fuzzy set: b=%.2f should be <= c=%.2f" % (b, c))

    def _execute(self, x):
        """
        Return membership x to created function
            :param x: checking this membership to function
            :type x: float
            :return: membership x to define function
            :rtype: float
        """
        if x < self._b:
            if self._a != self._b:
                return (x - self._a) * (1 / (self._b - self._a))
            else:
                return 1
        else:
            if self._b != self._c:
                return 1 + (x - self._b) * (-1 / (self._c - self._b))
            else:
                return 1

    def __repr__(self):
        """
        Interval-Valued Triangular Membership Function string description
            :return: String description of membership function
            :rtype: str
        """
        return "<Triangular MF 2 (%f, %f, %f)>" % (self._a, self._b, self._c)


class Trapezoidal_MF_2(MF_object_2):
    """
    Class representing Interval-Valued Trapezoidal Membership Function
        :param a: y coordinate for point on start Interval-Valued Trapezoidal Membership Function
        :type a: float
        :param b: y coordinate for point on first point of top edge Interval-Valued Trapezoidal Membership Function
        :type b: float
        :param c: y coordinate for point on second point of top edge Interval-Valued Trapezoidal Membership Function
        :type c: float
        :param d: y coordinate for point on end Interval-Valued Trapezoidal Membership Function
        :type d: float
    """

    def __init__(self, a=0, b=0.25, c=0.75, d=1):
        """
        Constructor method for Interval-Valued Trapezoidal Membership Function
        """
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def _execute(self, x):
        """
        Return membership x to created function
            :param x: checking this membership to function
            :type x: float
            :return: membership x to define function
            :rtype: float
        """
        if x < self._b:
            if self._a != self._b:
                return (x - self._a) * (1 / (self._b - self._a))
            else:
                return 1
        elif x >= self._b and x <= self._c:
            return 1
        else:
            if self._c != self._d:
                return 1 + (x - self._c) * (-1 / (self._d - self._c))
            else:
                return 1

    def __repr__(self):
        """
        Interval-Valued Trapezoidal Membership Function string description
            :return: description of membership function
            :rtype: str
        """
        return "<Trapezoidal MF 2 (%f, %f, %f, %f)>" % (self._a, self._b, self._c, self._d)


class IntervalFuzzySet(sf.FuzzySet):
    """
    Class representation Interval-Valued Fuzzy Set (IVFS).
        :param function_start: start function to define a IVFS. Supports pre-implemented membership functions
            Trapezoidal_MF_2, Triangular_MF_2 or user-defined functions, defaults to None
        :type function_start: MF_object_2
        :param function_end: end function to define a IVFS. Supports pre-implemented membership functions
            Trapezoidal_MF_2, Triangular_MF_2 or user-defined functions, defaults to None
        :type function_end: MF_object_2
        :param points_start: list of start points to define a IVFS. Each point is defined as a list of two coordinates in the
            universe of discourse/membership degree space, defaults to None
        :type points_start: MF_object_2
        :param points_end: list of end points to define a IVFS. Each point is defined as a list of two coordinates in the
            universe of discourse/membership degree space, defaults to None
        :type points_end: MF_object_2
        :param term: string representing the linguistic term to be associated to the Interval Valued Fuzzy Set
        :type term: str
    """

    def __init__(self, function_start=None, function_end=None, points_start=None, points_end=None, term=""):
        """
        Constructor method for IVFS
        """
        if function_start is not None:
            super().__init__(function=function_start, term=term)
            if function_end is not None:
                self._type_end = "function"
                self._funpointer_end = function_end
            else:
                self._type_end = None

        elif points_start is not None:
            super().__init__(points=points_start, term=term)

            if points_end is not None:
                if len(points_end) < 2:
                    raise Exception("ERROR: more than one point required")
                # if term == "":
                #    raise Exception("ERROR: please specify a linguistic term")
                for p in points_end:
                    if len(p) > 2: raise Exception(
                        "ERROR: one fuzzy set named \"" + self._term + "\" has more than two coordinates.")
                self._type = "pointbased"
                # self._high_quality_interpolate = high_quality_interpolate
                self._points_end = array(points_end)

                # Check boundary!!!
        elif function_start is not None and function_end is None:
            self._type_end = None
        else:
            self._type_end = None

    def get_value_fast_start(self, v):
        return super().get_value_fast(v)

    def get_value_fast_end(self, v):
        x = self._points_end.T[0]
        y = self._points_end.T[1]
        N = len(x)
        if v < x[0]: return self.boundary_values[0]  # fallback for values outside the Universe of the discourse
        for i in range(N - 1):
            if (x[i] <= v) and (v <= x[i + 1]):
                return self._fast_interpolate(x[i], y[i], x[i + 1], y[i + 1], v)
        return self.boundary_values[1]  # fallback for values outside the Universe of the discourse

    def get_value_slow_start(self, v):
        return super().get_value_slow(self, v)

    def get_value_slow_end(self, v):
        f = interp1d(self._points_end.T[0], self._points_end.T[1],
                     bounds_error=False, fill_value=(self.boundary_values[0], self.boundary_values[1]))
        result = f(v)
        return (result)

    def get_value_cut(self, v, cut):
        """
        Function for return the membership value of v to this IVFS, capped to the cut value.
            :param v: element of the universe of discourse
            :param cut: alpha cut of the IVFS
            :rtype: float
        """
        if type(cut) is numpy.ndarray and cut.size > 1:
            return min(cut[0], self.get_value(v)[0]), min(cut[1], self.get_value(v)[1])
        elif type(cut) is tuple and len(cut) > 1:
            return min(cut[0], self.get_value(v)), min(cut[1], self.get_value(v))
        else:
            return min(cut, self.get_value(v))

    def get_value_cut_start(self, v, cut):
        return min(cut[0], self.get_value_start(v))

    def get_value_cut_end(self, v, cut):
        return min(cut[1], self.get_value_end(v))

    def get_value_start(self, v):
        if self._type == "function":
            return self._funpointer(v)

    def get_value_end(self, v):
        if self._type_end == "function":
            return self._funpointer_end(v)
        else:
            return self._funpointer(v)

    def get_value(self, v):
        """
        Return the membership end value of v to this IVFS
            :param v: element of the universe of discourse
            :return: The membership end value of v to this IVFS
            :rtype: tuple
        """
        if self._type == "function" and self._type_end == "function":
            return [self._funpointer(v), self._funpointer_end(v)]
        elif self._type == "function" and self._type_end is None:
            return self._funpointer(v)
        elif self._high_quality_interpolate:
            return self.get_value_slow_start(v), self.get_value_slow_end(v)
        else:
            return self.get_value_fast_start(v), self.get_value_fast_end(v)

    def get_type_start(self):
        return self._type

    def get_type_end(self):
        return self._type_end

    def __repr__(self):
        if self._type_end is None:
            return "<Fuzzy set (fun1:%s), term='%s'>" % (self._funpointer, self._term)
        else:
            return "<Interval Fuzzy set (fun1:%s, fun2:%s), term='%s'>" % (
                self._funpointer, self._funpointer_end, self._term)

    def set_params(self):
        print("Attention: this is a virtual method for setting parameters of pre-baked interval fuzzy sets.")

    def set_points_interval(self, points_start, points_end):
        """
        Changes points of the point-based IVFS.
            :param points_start: a list of points to define lower bound of IVFS. Each point is defined as a list of two
                coordinates in the universe of discourse/membership degree space.
            :type points_start: list
            :param points_end: a list of points to define upper bound of IVFS. Each point is defined as a list of two
                coordinates in the universe of discourse/membership degree space.
            :type points_end: list
        """
        if len(points_start) < 2 or len(points_end < 2):
            raise Exception("ERROR: more than one point required")
        if self._type == "function":
            print(
                "WARNING: the fuzzy set named \"" + self._term + "\" was converted from function-based to point-based.")
        for p in points_start:
            if len(p) > 2: raise Exception("ERROR: one point in \"" + self._term + "\" has more than two coordinates.")
        self._type = "pointbased"
        self._high_quality_interpolate = False
        self._points = array(points_start)
        self._points_end = array(points_end)
        self.boundary_values = [self._points.T[1][0], self._points.T[1][-1]]


if __name__ == '__main__':
    S_1 = IntervalFuzzySet(function_start=sf.Triangular_MF(a=0, b=0, c=4), function_end=sf.Triangular_MF(a=0, b=2, c=6),
                           term='poor')
    sf.LinguisticVariable([S_1], universe_of_discourse=[0, 10]).plot()
    print('S_1:\t', S_1)
