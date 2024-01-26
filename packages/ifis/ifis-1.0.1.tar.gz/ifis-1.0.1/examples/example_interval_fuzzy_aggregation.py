import simpful as sf
from numpy import prod

from ifis.interval_aggregations import IntervalFuzzyAggregator
from ifis.interval_fuzzy_sets import IntervalFuzzySet


def aProduct(memberships):
    return prod(memberships, axis=0)


if __name__ == "__main__":
    ivA = IntervalFuzzyAggregator(verbose=True)

    IVFS1 = IntervalFuzzySet(function_start=sf.Triangular_MF(a=0, b=0, c=4),
                             function_end=sf.Triangular_MF(a=0, b=2, c=6),
                             term='test1')
    IVFS2 = IntervalFuzzySet(function_start=sf.Triangular_MF(a=2, b=3, c=4),
                             function_end=sf.Triangular_MF(a=1, b=3, c=5),
                             term='test2')
    IVFS3 = IntervalFuzzySet(function_start=sf.Triangular_MF(a=2, b=3, c=4),
                             function_end=sf.Triangular_MF(a=1, b=3, c=5),
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

    ivA.add_variables(IVFS1, IVFS2, IVFS3, IVFS4, IVFS5, IVFS6)

    ivA.set_variable("test1", 3)
    ivA.set_variable("test2", 2)
    ivA.set_variable("test3", 4)
    ivA.set_variable("test4", 5)
    ivA.set_variable("test5", 6)
    ivA.set_variable("test6", 7)
    print()

    result = ivA.aggregate(["test1", "test2"], aggregation_fun="A_Prod")
    print("Result:", result, end="\n\n")

    result = ivA.aggregate(["test1", "test2", "test3"], aggregation_fun="A_Mean")
    print("Result:", result, end="\n\n")

    result = ivA.aggregate(["test1", "test2", "test3", "test4"], aggregation_fun=aProduct)
    print("Result:", result, end="\n\n")

    result = ivA.aggregate(["test1", "test2"], aggregation_fun="A_4", aggregation_param='p')
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")

    result = ivA.aggregate(["test5", "test6"], aggregation_fun="A_4", aggregation_param='p')
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")

    result = ivA.aggregate(["test1", "test2"], aggregation_fun="A_4", aggregation_param='g')
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")

    result = ivA.aggregate(["test5", "test6"], aggregation_fun="A_4", aggregation_param='g')
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")

    result = ivA.aggregate(["test1", "test2", "test3", "test4"], aggregation_fun="A_3", aggregation_param='p')
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")

    result = ivA.aggregate(["test5", "test6", "test3", "test4"], aggregation_fun="A_3", aggregation_param='g')
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")

    result = ivA.aggregate(["test5", "test6", "test3", "test4"], aggregation_fun="A_Alpha", aggregation_param=0.5)
    print("\033[2;34mResult:", result, end="\n\n")
    print("\033[2;38m")