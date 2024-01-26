import numpy as np
import simpful as sf
from simpful import Triangular_MF, Trapezoidal_MF
from ifis.interval_fuzzy_sets import IntervalFuzzySet

"""
Module with various implementations of aggregation functions
"""
def aMeanPower(memberships):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'MeanPower'
    This aggregation respect orders: Lexicographical 1, Lexicographical 2 and Xu Yager
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :return: lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() == 2:
        return [[np.sum(memberships, axis=0)][0][0] / 2, np.sqrt(np.sum([np.square(memberships)[:, 1]]) / 2)]
    elif memberships.__len__() > 2:
        memberships2 = np.concatenate(([[[np.sum(memberships[:2], axis=0)][0][0] / 2,
                                         np.sqrt(np.sum([np.square(memberships[:2])[:, 1]]) / 2)]],
                                       memberships[-(len(memberships) - 2):]), axis=0)
        return aMeanPower(memberships2)



def aMeanMax(memberships):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'MeanMax'
    This aggregation respect orders: Lexicographical 1, Lexicographical 2 and Xu Yager
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() >= 2:
        return [[np.sum(memberships, axis=0)][0][0] / len(memberships), np.max(memberships, axis=0)[1]]


def aProdMean(memberships):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'ProdMean'
    This aggregation respect orders: Lexicographical 1, Lexicographical 2 and Xu Yager
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() >= 2:
        return [np.prod(memberships, axis=0)[0], np.sum(memberships, axis=0)[1] / len(memberships)]


def aMinMax(memberships):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'MinMax'
    This aggregation respect orders: Lexicographical 1, Lexicographical 2 and Xu Yager
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() >= 2:
        return [np.min(memberships, axis=0)[0], np.max(memberships, axis=0)[1]]


def aMax(memberships):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'Max'
    This aggregation respect orders: Lexicographical 1, Lexicographical 2 and Xu Yager
    and comparability relations: possible and necessary
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() >= 2:
        return [np.max(memberships, axis=0)[0], np.max(memberships, axis=0)[1]]


def aMin(memberships):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'Min'
    This aggregation respect orders: Lexicographical 1, Lexicographical 2 and Xu Yager
    and comparability relations: possible and necessary
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() >= 2:
        return [np.min(memberships, axis=0)[0], np.min(memberships, axis=0)[1]]


def aGMean(memberships):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'GeometricMean'
    This aggregation respect orders: Lexicographical 1, Lexicographical 2 and Xu Yager
    and comparability relations: possible and necessary
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() >= 2:
        return np.power(np.prod([row[0] for row in memberships]), (1.0 / memberships.__len__()))


def aAlpha(memberships, alpha=0.5):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation alpha
    If param alpha equals 0.5 we get Mean aggregation
    This aggregation respect orders: Lexicographical 1, Lexicographical 2 and Xu Yager
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :param alpha: parameter to builds aggregation, default to 0.5
        :type alpha: float
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() == 2:
        return [alpha * memberships[0][0] + (1 - alpha) * memberships[1][0],
                alpha * memberships[0][1] + (1 - alpha) * memberships[1][1]]
    elif memberships.__len__() > 2:
        others = aAlpha(memberships[-(len(memberships) - 1):], alpha)
        return [alpha * memberships[0][0] + (1 - alpha) * others[0],
                alpha * memberships[0][1] + (1 - alpha) * others[1]]


def aW(memberships):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'W'
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() >= 2:
        s1 = 0
        s2 = 0
        s3 = 0
        s4 = 0
        s5 = 0
        for i in range(memberships.__len__()):
            s1 += memberships[i][0]
            s4 += memberships[i][1]
            s2 += memberships[i][1] * (memberships[i][1] - memberships[i][0])
            s5 += memberships[i][0] * (memberships[i][1] - memberships[i][0])
            s3 += memberships[i][1] - memberships[i][0]
        a = (s1 + s2) / (s3 + memberships.__len__())
        b = (s4 + s5) / (s3 + memberships.__len__())
        return [a, b]


def aA1(memberships):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'A1'
    This aggregation respect comparability relation: possible
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() == 2:
        ones = [1, 1]
        if memberships[0] == ones and memberships[1] == ones:
            return [1, 1]
        else:
            a = (memberships[1][0] * (memberships[0][0] + memberships[0][1]) / 2) / 2
            b = (memberships[1][1] + memberships[0][1]) / 2
            return [a, b]
    elif memberships.__len__() > 2:
        ones = [1, 1]
        if memberships[0] == ones and memberships[1] == ones:
            memberships.__delitem__(0)
            return aA1(memberships)
        else:
            a = (memberships[1][0] * (memberships[0][0] + memberships[0][1]) / 2) / 2
            b = (memberships[1][1] + memberships[0][1]) / 2
            memberships = memberships[1:]
            memberships[0] = [a, b]
            return aA1(memberships)


def aA2(memberships):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'A2'
    This aggregation respect comparability relation: possible
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() == 2:
        ones = [1, 1]
        if memberships[0] == ones and memberships[1] == ones:
            return [1, 1]
        else:
            a = (memberships[0][0] * (memberships[1][0] + memberships[1][1]) / 2) / 2
            b = (memberships[1][1] + memberships[0][1]) / 2
            return [a, b]
    elif memberships.__len__() > 2:
        ones = [1, 1]
        if memberships[0] == ones and memberships[1] == ones:
            memberships.__delitem__(0)
            return aA2(memberships)
        else:
            a = (memberships[0][0] * (memberships[1][0] + memberships[1][1]) / 2) / 2
            b = (memberships[1][1] + memberships[0][1]) / 2
            memberships = memberships[1:]
            memberships[0] = [a, b]
            return aA2(memberships)


def aA3(memberships, inside_aggregation="g"):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'A3'
    This aggregation respect comparability relation: possible
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :param inside_aggregation: aggregation inside this aggregation function, able to use aggregations are
            geometric mean(g) and power mean(p), default to 'g'(geometric mean)
        :type inside_aggregation: str
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() >= 2:
        ones = [1, 1]
        if memberships[0] == ones and memberships[1] == ones:
            return [1, 1]
        else:
            if inside_aggregation == 'g':
                b = np.power(np.prod([row[1] for row in memberships]), (1.0 / memberships.__len__()))
            else:
                b = np.power(
                    np.sum([np.power(row[1], memberships.__len__()) for row in memberships]) / memberships.__len__(),
                    (1 / memberships.__len__()))
            return [0, b]


def aA4(memberships, inside_aggregation="g"):
    """
    Function to aggregate memberships of each linguistic variable terms by aggregation 'A3'
    This aggregation respect comparability relation: possible
        :param memberships: list memberships of each linguistic variable terms
        :type memberships: list
        :param inside_aggregation: aggregation inside this aggregation function, able to use aggregations are
            geometric mean(g) and power mean(p), default to 'g'(geometric mean)
        :type inside_aggregation: str
        :return: list which contains lower and upper bound of interval after aggregation
        :rtype: list
    """
    if memberships.__len__() < 2:
        raise Exception(
            "ERROR: You can aggregate 2 or more intervals.")
    elif memberships.__len__() >= 2:
        zeros = [0, 0]
        if memberships[0] == zeros and memberships[1] == zeros:
            return [0, 0]
        else:
            if inside_aggregation == 'g':
                a = np.power(np.prod([row[0] for row in memberships]), (1.0 / memberships.__len__()))
            else:
                a = np.power(
                    np.sum([np.power(row[0], memberships.__len__()) for row in memberships]) / memberships.__len__(),
                    (1 / memberships.__len__()))
            return [a, 1]


class IntervalFuzzyAggregator(sf.FuzzyAggregator):
    """
    Creates a new interval fuzzy aggregation object based on the FuzzyAggregator object from the Simpful library.
    Aggregations available: A_Prod, A_MeanPower, A_Mean.
        :param verbose: toggles verbose mode, default to FALSE
        :type verbose: bool
    """

    def __init__(self, verbose=False):
        super().__init__(verbose=verbose)

    def add_variables(self, *args):
        """
        Adds variables and their IVFS to perform fuzzy aggregation.
            :param args: ''ifis.interval_fuzzy_sets.IntervalFuzzySet'' objects, whose 'term' argument is the name of
                the variable.
            :type args: IVFS objects
        """
        for v in args:
            if isinstance(v, IntervalFuzzySet):
                self._variables[v._term] = v
                if self.verbose: print("\033[2;35m * IVFS:", v._type, v._term, (
                    (v._points.tolist(), '|', v._points_end.tolist()) if v._type == "pointbased" else v))
            else:
                raise Exception("ERROR: please give as arguments only objects of interval fuzzy sets.")
        print("\033[2;38m")

    def set_variable(self, name, value):
        """
        Sets the interval value of a variable to be aggregated.
            :param name: name of the variables to be set
            :type name: str
            :param value: interval value to be set
            :type value: list
        """
        try:
            value = float(value)
            self._values[name] = value
            if self.verbose:
                print(" * Variable %s has value %f" % (name, value))
        except ValueError:
            raise Exception("ERROR: value for " + name + " is not integer or float: " + value)

    def aggregate(self, variables=None, aggregation_fun="product", aggregation_param=None):
        """
        The method aggregates the terms of linguistic variables according to their affiliation and membership functions
            :param aggregation_fun: name of the aggregation we want to use (A_MeanPower, A_GMean, A_MeanMax, A_ProdMean,
                A_MinMax, A_Min, A_Max, A_W, A_1, A_2, A_3, A_4, A_Alpha, A_Mean  are available)
            :type aggregation_fun: str
            :param aggregation_param: an optional parameter that is used in a specific aggregation that contains another
                aggregation inside
            :type aggregation_param: str, int
            :return:
            :rtype: list
        """
        # In development

        if variables == None:
            variables = list(set(self._variables.keys()))
        if self.verbose: print(" * Variables:", variables)
        if len(variables) > len(set(variables)):
            raise Exception(
                "ERROR: the specified list of variables to aggregate contains two or more repetitions, Interrupt.")

        memberships = []
        for v in variables:
            try:
                value = self._values[v]
                if self.verbose: print(" * name = value: %s = %s" % (v, value))
                if isinstance(value, tuple):
                    result = [self._variables[v].get_value(value[0]), self._variables[v].get_value(value[1])]
                else:
                    result = self._variables[v].get_value(value)
                if self.verbose: print(" * result", result)
                if self.verbose: print(" * Type of IVFS:", self._variables[v]._type)
                if hasattr(self._variables[v], "_funpointer_end"):
                    if isinstance(self._variables[v]._funpointer, Triangular_MF):
                        a = np.array([self._variables[v]._funpointer._a, self._variables[v]._funpointer._b,
                                      self._variables[v]._funpointer._c, self._variables[v]._funpointer_end._a,
                                      self._variables[v]._funpointer_end._b, self._variables[v]._funpointer_end._c])
                    elif isinstance(self._variables[v]._funpointer, Trapezoidal_MF):
                        a = np.array([self._variables[v]._funpointer._a, self._variables[v]._funpointer._b,
                                      self._variables[v]._funpointer._c, self._variables[v]._funpointer._d,
                                      self._variables[v]._funpointer_end._a, self._variables[v]._funpointer_end._b,
                                      self._variables[v]._funpointer_end._c, self._variables[v]._funpointer._d])
                        # TODO others functions
                    mi = np.min(a)
                    ma = np.max(a)
                    x = np.linspace(mi, ma, 100)
                    # print(type(x), x.astype(float))
                else:
                    a = np.array(range(len(self._variables[v]._points)))
                    b = np.array(range(len(self._variables[v]._points_end)))
                    # sample = np.array([[0.1, 0.3], [0.5, 0.7], [0.4, 1], [0, 1], [0, .4]])
                    # x = np.array(range(len(sample)))
                    # print("\033[2;34m This text is Bright Green  \n")
                    # print(Fore.YELLOW + ' ')
                    # print(type(self._variables[v]))
                    lower_ends = [self._variables[v].get_value(xx) for xx in a]
                    top_ends = [self._variables[v].get_value(xx)[1] for xx in b]
                    # print(a, lower_ends, "\n", b, top_ends)
                    # print(tabulate(lower_ends))
                    # print(Fore.RESET + " ")

                    # print("\t", type(result), self._variables[v])
                    # print("\t", result)
                memberships.append(result)
            except KeyError:
                raise Exception("ERROR: term " + v + " is not defined.")

        if self.verbose:
            print(" * Aggregation of the following values:", memberships)
            if callable(aggregation_fun):
                print(" * Aggregation function:", aggregation_fun.__name__)
            else:
                if aggregation_param is None:
                    print(" * Aggregation function:", aggregation_fun)
                else:
                    print(" * Aggregation function: %s(%s)" % (aggregation_fun, aggregation_param))

        if callable(aggregation_fun):
            return aggregation_fun(memberships)
        elif aggregation_fun == "A_Prod":
            return np.prod(memberships, axis=0)
        elif aggregation_fun == "A_MeanPower":
            return aMeanPower(memberships)
        elif aggregation_fun == "A_GMean":
            return aGMean(memberships)
        elif aggregation_fun == "A_MeanMax":
            return aMeanMax(memberships)
        elif aggregation_fun == "A_ProdMean":
            return aProdMean(memberships)
        elif aggregation_fun == "A_MinMax":
            return aMinMax(memberships)
        elif aggregation_fun == "A_Min":
            return aMin(memberships)
        elif aggregation_fun == "A_Max":
            return aMax(memberships)
        elif aggregation_fun == "A_W":
            return aW(memberships)
        elif aggregation_fun == "A_1":
            return aA1(memberships)
        elif aggregation_fun == "A_2":
            return aA2(memberships)
        elif aggregation_fun == "A_3":
            return aA3(memberships, aggregation_param)
        elif aggregation_fun == "A_4":
            return aA4(memberships, aggregation_param)
        elif aggregation_fun == "A_Alpha":
            return aAlpha(memberships, aggregation_param)
        elif aggregation_fun == "A_Mean":
            return np.sum(memberships, axis=0) / len(memberships)
        else:
            raise Exception(
                "ERROR: Please provide a pointer to a callable function or the name of an implemented aggregate function.")


if __name__ == '__main__':
    # Creating an Interval Fuzzy Aggregator object and toggling verbose mode
    ivA = IntervalFuzzyAggregator(verbose=True)

    # Defining several interval fuzzy sets for variables and setting their names
    IVFS1 = IntervalFuzzySet(function_start=sf.Triangular_MF(a=0, b=0, c=4),
                             function_end=sf.Triangular_MF(a=0, b=2, c=6),
                             term='test1')
    IVFS2 = IntervalFuzzySet(function_start=sf.Triangular_MF(a=2, b=3, c=4),
                             function_end=sf.Triangular_MF(a=1, b=3, c=5),
                             term='test2')
    IVFS3 = IntervalFuzzySet(function_start=sf.Triangular_MF(a=2, b=3, c=4),
                             function_end=sf.Triangular_MF(a=1, b=4, c=8),
                             term='test3')
    IVFS4 = IntervalFuzzySet(function_start=sf.Triangular_MF(a=0, b=0, c=4),
                             function_end=sf.Triangular_MF(a=0, b=2, c=6),
                             term='test4')
    IVFS5 = IntervalFuzzySet(function_start=sf.Triangular_MF(a=0, b=6, c=12),
                             function_end=sf.Triangular_MF(a=0, b=6, c=12),
                             term='test5')
    IVFS6 = IntervalFuzzySet(function_start=sf.Triangular_MF(a=0, b=7, c=14),
                             function_end=sf.Triangular_MF(a=0, b=7, c=14),
                             term='test6')

    # Adding interval fuzzy set objects to the Interval Fuzzy Aggregator
    ivA.add_variables(IVFS1, IVFS2, IVFS3, IVFS4, IVFS5, IVFS6)

    # Set numeric variable names
    ivA.set_variable("test1", 3)
    ivA.set_variable("test2", 2)
    ivA.set_variable("test3", 4)
    ivA.set_variable("test4", 5)
    ivA.set_variable("test5", 6)
    ivA.set_variable("test6", 7)
    print()

    # Execution of aggregation.
    # Aggregations available: A_Prod, A_MeanPower, A_Mean, A_GMean, A_MeanMax, A_ProdMean, A_MinMax, A_Min, A_Max, A_Alpha, A_W, A_1, A_2, A_3, A_4.
    # It accepts the name of the aggregation function and any aggregation parameters.
    result = ivA.aggregate(["test1", "test2"], aggregation_fun="A_Mean")
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")

    result = ivA.aggregate(["test1", "test2"], aggregation_fun="A_4", aggregation_param='p')
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")

    result = ivA.aggregate(["test5", "test6"], aggregation_fun="A_4", aggregation_param='p')
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")

    # Aggregation of three intervals
    result = ivA.aggregate(["test1", "test2", "test3"], aggregation_fun="A_MeanPower")
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")

    # Agregation MeanPower
    result = ivA.aggregate(["test1", "test2", "test3", "test4"], aggregation_fun="A_4", aggregation_param='p')
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")

    result = ivA.aggregate(["test5", "test6", "test3", "test4"], aggregation_fun="A_4", aggregation_param='p')
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")
