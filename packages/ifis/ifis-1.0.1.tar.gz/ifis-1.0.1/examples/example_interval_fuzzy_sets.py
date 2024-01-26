from simpful import *
from ifis.interval_fuzzy_sets import *
from ifis.interval_linguistic_variable import *

S_1 = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=0, c=3), function_end=Triangular_MF(a=0, b=0, c=4),
                       term='test1')
S_2 = IntervalFuzzySet(function_start=Triangular_MF(a=2, b=3, c=4), function_end=Triangular_MF(a=1, b=3, c=5),
                       term='test2')
S_3 = IntervalFuzzySet(function_start=Triangular_MF(a=4, b=6, c=6), function_end=Triangular_MF(a=3, b=6, c=6),
                       term='test3')

# IntervalLinguisticVariable([S_1, S_2, S_3], universe_of_discourse=[0, 10]).plot()

S_1a = IntervalFuzzySet(function_start=Triangular_MF(a=0, b=0, c=3), term='test1a')
S_2a = IntervalFuzzySet(function_start=Triangular_MF(a=2, b=3, c=4), term='test2a')
S_3a = IntervalFuzzySet(function_start=Triangular_MF(a=4, b=6, c=6), term='test3a')

IntervalLinguisticVariable([S_1a, S_2a, S_3a], universe_of_discourse=[0, 10]).plot()

print('S_1:\t', S_1)
print('S_2:\t', S_2)

print('S_1:\t', S_1a)
print('S_2:\t', S_2a)