import simpful as sf
import re
from simpful.fuzzy_sets import MF_object
from numpy import array, linspace
from .interval_rule_parsing import interval_recursive_parse, interval_preparse, interval_postparse
from collections import defaultdict


class IntervalFuzzySystem(sf.FuzzySystem):
    """
    Class which creates a new interval valued fuzzy system (IVFS).
        :param type_system: change type of system able to check 1 and 2 (2 is for special case of intervals when lower
            and upper bound of intervals is the same), default to 1
        :type type_system: int
        :param show_banner: toggles display of banner, default to True
        :type show_banner: bool
        :param sanitize_input: sanitize variables names to eliminate non-accepted characters (under development).
        :param verbose: toggles verbose mode, default to False
        :type verbose: bool
        :param operators: specifying interval fuzzy operators to be used instead of defaults. Currently supported operators: 'AND_PRODUCT'.
        :type operators: list
    """

    def __init__(self, type_system=1, operators=None, show_banner=False, show_banner_ifis=True, sanitize_input=False, verbose=True):
        super(IntervalFuzzySystem, self).__init__(operators, show_banner, sanitize_input, verbose)
        self._type_system = type_system
        if show_banner_ifis:
            self._banner()

    def _banner(self):
        import pkg_resources
        vrs = pkg_resources.get_distribution('simpful').version
        print(" IFIS (Interval-Valued Fuzzy Inference System) v.1.0.1")
        print(" Created by Piotr Grochowalski (pgrochowalski@ur.edu.pl)")
        print()
        print(" Simpful v%s " % vrs)
        print(" Created by Marco S. Nobile (m.s.nobile@tue.nl)")
        print(" and Simone Spolaor (simone.spolaor@unimib.it)")
        print()

    def set_variable(self, name, value, verbose=False):
        """
        Sets the interval value of a linguistic variable.
            :param name: name of the linguistic variables to be set
            :type name: str
            :param value: interval value to be set
            :type value: tuple
            :param verbose: toggles verbose mode, default to False
            :type verbose: bool
        """
        if type(value) is tuple:
            if self._sanitize_input: name = self._sanitize(name)
            try:
                value = float(value[0]), float(value[1])
                self._variables[name] = value
                if verbose: print(" * Variable %s set to %f" % (name, value))
            except ValueError:
                raise Exception(
                    "ERROR: specified value for " + name + " is not an interval of integer or float numbers: " + value)
        else:
            super().set_variable(name, value, verbose)

    def add_rules(self, rules, verbose=False):
        """
        Adds new interval valued fuzzy rules (IVFR) to the IVFS.
            :param rules: list of interval valued fuzzy rules to be added. Rules must be specified as strings
            :type rules: list of str
            :param verbose: toggles verbose mode
            :type verbose: bool
        """
        for rule in rules:

            # optional: remove invalid symbols
            if self._sanitize_input: rule = self._sanitize(rule)

            parsed_antecedent = interval_recursive_parse(interval_preparse(rule), verbose=verbose,
                                                         operators=self._operators)
            parsed_consequent = interval_postparse(rule, verbose=verbose)
            self._rules.append([parsed_antecedent, parsed_consequent])
            if verbose:
                print(" * Added rule IF", parsed_antecedent, "THEN", parsed_consequent)
                print()
        if verbose: print(" * %d rules successfully added" % len(rules))

    def mediate_interval(self, outputs, antecedent, results, ignore_errors=False, ignore_warnings=False, verbose=False):
        """
        Function calculate Sugeno method of IVFS.
        """
        final_result = {}

        list_crisp_values = [x[0] for x in self._crispvalues.items()]
        list_output_funs = [x[0] for x in self._outputfunctions.items()]

        for output in outputs:
            if verbose:
                print(" * Processing output for variable '%s'" % output)
                print("   whose universe of discourse is:", self._lvs[output].get_universe_of_discourse())
                print("   contains the following fuzzy sets:", self._lvs[output]._FSlist)

            num_start = 0
            den_start = 0
            num_end = 0
            den_end = 0

            for (ant, res) in zip(antecedent, results):
                outname = res[0]
                outterm = res[1]
                crisp = True
                if outname == output:
                    if outterm not in list_crisp_values:
                        crisp = False
                        if outterm not in list_output_funs:
                            raise Exception("ERROR: one rule calculates an output named '"
                                            + outterm
                                            + "', but I cannot find it among the output terms.\n"
                                            + " --- PROBLEMATIC RULE:\n"
                                            + "IF " + str(ant) + " THEN " + str(res))
                    if crisp:
                        crispvalue = self._crispvalues[outterm]
                        crispvalue_start = self._crispvalues[outterm]
                        crispvalue_end = self._crispvalues[outterm]
                    elif isinstance(self._outputfunctions[outterm], MF_object):
                        raise Exception(
                            "ERROR in consequent of rule %s.\nSugeno reasoning does not support output fuzzy sets." % (
                                    "IF " + str(ant) + " THEN " + str(res)))
                    else:
                        if self._type_system == 1:
                            string_to_evaluate = self._outputfunctions[outterm]
                        elif self._type_system == 2:
                            string_to_evaluate_start = self._outputfunctions[outterm]
                            string_to_evaluate_end = self._outputfunctions[outterm]

                        for k, v in self._variables.items():
                            # old version
                            # string_to_evaluate = string_to_evaluate.replace(k,str(v))

                            # match a variable name preceeded or followed by non-alphanumeric and _ characters
                            # substitute it with its numerical value
                            if self._type_system == 2 and type(v) is tuple:
                                string_to_evaluate_start = re.sub(r"(?P<front>\W|^)" + k + r"(?P<end>\W|$)",
                                                                  r"\g<front>" + str(v[0]) + r"\g<end>",
                                                                  string_to_evaluate_start)
                                string_to_evaluate_end = re.sub(r"(?P<front>\W|^)" + k + r"(?P<end>\W|$)",
                                                                r"\g<front>" + str(v[1]) + r"\g<end>",
                                                                string_to_evaluate_end)
                            else:
                                string_to_evaluate = re.sub(r"(?P<front>\W|^)" + k + r"(?P<end>\W|$)",
                                                            r"\g<front>" + str(v) + r"\g<end>", string_to_evaluate)

                        if self._type_system == 2:
                            crispvalue_start = eval(string_to_evaluate_start)
                            crispvalue_end = eval(string_to_evaluate_end)
                        else:
                            crispvalue = eval(string_to_evaluate)

                    try:
                        value = ant.evaluate_interval(self)
                    except RuntimeError:
                        raise Exception("ERROR: one rule could not be evaluated\n"
                                        + " --- PROBLEMATIC RULE:\n"
                                        + "IF " + str(ant) + " THEN " + str(res) + "\n")

                    if self._type_system == 2:
                        temp_start = value[0] * crispvalue_start
                        num_start += temp_start
                        den_start += value[0]

                        temp_end = value[1] * crispvalue_end
                        num_end += temp_end
                        den_end += value[1]
                    else:
                        temp_start = value[0] * crispvalue
                        num_start += temp_start
                        den_start += value[0]

                        temp_end = value[1] * crispvalue
                        num_end += temp_end
                        den_end += value[1]

            try:
                if den_start == 0.0 and den_end == 0.0:
                    final_result[output] = (0.0, 0.0)
                    if not ignore_warnings:
                        print(
                            "WARNING: the sum of rules' firing for variable '%s' is equal to 0. The result of the Sugeno inference was set to (0,0)." % output)
                elif den_start == 0.0:
                    final_result[output] = (0.0, num_end / den_end)
                elif den_end == 0.0:
                    final_result[output] = (num_start / den_start, 0.0)
                else:
                    interval_start = num_start / den_start
                    interval_end = num_end / den_end
                    if interval_start <= interval_end:
                        final_result[output] = interval_start, interval_end
                    else:
                        final_result[output] = interval_end, interval_start

            except ArithmeticError:
                if ignore_errors:
                    print(
                        "WARNING: cannot perform Sugeno inference for variable '%s'. The variable appears only as antecedent in the rules or an arithmetic error occurred." % output)
                else:
                    raise Exception(
                        "ERROR: cannot perform Sugeno inference for variable '%s'. The variable appears only as antecedent in the rules or an arithmetic error occurred." % output)

        return final_result

    def mediate_interval_Mamdani(self, outputs, antecedent, results, ignore_errors=False, ignore_warnings=False,
                                 verbose=False, subdivisions=1000):
        """
        Function calculate Mamdani method of IVFS.
        """
        final_result = {}

        for output in outputs:

            if verbose:
                print(" * Processing output for variable '%s'" % output)
                print("   whose universe of discourse is:", self._lvs[output].get_universe_of_discourse())
                print("   contains the following fuzzy sets:", self._lvs[output]._FSlist)
            cuts_list = defaultdict(list)

            x0, x1 = self._lvs[output].get_universe_of_discourse()

            for (ant, res) in zip(antecedent, results):

                outname = res[0]
                outterm = res[1]

                if verbose:
                    print(" ** Rule composition:", ant, "->", res, ", output variable: '%s'" % outname,
                          "with term: '%s'" % outterm)

                if outname == output:

                    try:
                        value = ant.evaluate_interval(self)
                    except RuntimeError:
                        raise Exception("ERROR: one rule could not be evaluated\n"
                                        + " --- PROBLEMATIC RULE:\n"
                                        + "IF " + str(ant) + " THEN " + str(res) + "\n")

                    cuts_list[outterm].append(value)

            values_start = []
            values_stop = []
            weightedvalues_start = []
            weightedvalues_stop = []
            integration_points = linspace(x0, x1, subdivisions)

            convenience_dict = {}
            for k in cuts_list.keys():
                convenience_dict[k] = self._lvs[output].get_index(k)
            if verbose: print(" * Indices:", convenience_dict)

            for u in integration_points:
                comp_values_start = []
                comp_values_stop = []
                for k, v_list in cuts_list.items():
                    for v in v_list:
                        n = convenience_dict[k]
                        fs_term = self._lvs[output]._FSlist[n]
                        if self._type_system == 2:
                            result_start = float(fs_term.get_value_cut_start(u, cut=v))
                            result_stop = float(fs_term.get_value_cut_end(u, cut=v))
                        else:
                            result_start = float(fs_term.get_value_cut(u, cut=v)[0])
                            result_stop = float(fs_term.get_value_cut(u, cut=v)[1])
                        comp_values_start.append(result_start)
                        comp_values_stop.append(result_stop)
                keep_start = max(comp_values_start)
                keep_stop = max(comp_values_stop)
                values_start.append(keep_start)
                values_stop.append(keep_stop)
                weightedvalues_start.append(keep_start * u)
                weightedvalues_stop.append(keep_stop * u)
            sumwv_start = sum(weightedvalues_start)
            sumwv_stop = sum(weightedvalues_stop)
            sumv_start = sum(values_start)
            sumv_stop = sum(values_stop)

            try:
                if sumv_start == 0.0:
                    CoG = (0, sumwv_stop / sumv_stop)
                    if not ignore_warnings:
                        print(
                            "WARNING: the sum of rules' firing for variable '%s' is equal to 0. The result of the Mamdani inference was set to 0." % output)
                elif sumv_stop == 0.0:
                    CoG = (sumwv_start / sumv_start, 0)
                    if not ignore_warnings:
                        print(
                            "WARNING: the sum of rules' firing for variable '%s' is equal to 0. The result of the Mamdani inference was set to 0." % output)
                # else:
                #   CoG = sumwv_start / sumv_start, sumwv_stop / sumv_stop
                else:
                    interval_start = sumwv_start / sumv_start
                    interval_end = sumwv_stop / sumv_stop
                    if interval_start <= interval_end:
                        CoG = interval_start, interval_end
                    else:
                        CoG = interval_end, interval_start

            except ArithmeticError:
                if ignore_errors:
                    print(
                        "WARNING: cannot perform Mamdani inference for variable '%s'. The variable appears only as antecedent in the rules or an arithmetic error occurred." % output)
                else:
                    raise Exception(
                        "ERROR: cannot perform Mamdani inference for variable '%s'. The variable appears only as antecedent in the rules or an arithmetic error occurred." % output)

            if verbose: print(" * Weighted values: %.2f\tValues: %.2f\tCoG: %.2f" % (
                (sumwv_start, sumv_start), (sumwv_stop, sumv_stop), CoG))
            final_result[output] = CoG

        return final_result

    def Sugeno_interval_inference(self, terms=None, ignore_errors=False, ignore_warnings=False, verbose=False):
        """
        Performs Sugeno interval fuzzy inference.
            :param terms: names of the variables on which inference must be performed
                If empty, all variables appearing in the consequent of a IVFR are inferred.
            :type terms: list
            :param ignore_errors: toggles the raising of errors during the inference.
            :type ignore_errors: bool
            :param ignore_warnings: toggles the raising of warnings during the inference.
            :type ignore_warnings: bool
            :param verbose: toggles verbose mode.
            :type verbose: bool
            :return: a dictionary, containing as keys the variables names and as values their interval inferred values
        """
        if self._sanitize and terms is not None:
            terms = [self._sanitize(term) for term in terms]
            # default: inference on ALL rules/terms

        if terms == None:
            temp = [rule[1][0] for rule in self._rules]
            terms = list(set(temp))
        else:
            # get rid of duplicates in terms to infer
            terms = list(set(terms))
            for t in terms:
                if t not in set([rule[1][0] for rule in self._rules]):
                    raise Exception("ERROR: Variable " + t + " does not appear in any consequent.")

        array_rules = array(self._rules, dtype='object')
        if len(self._constants) == 0:
            result = self.mediate_interval(terms, array_rules.T[0], array_rules.T[1], ignore_errors=ignore_errors,
                                           ignore_warnings=ignore_warnings, verbose=verbose)
        else:
            # remove constant variables from list of variables to infer
            ncost_terms = [t for t in terms if t not in self._constants]
            result = self.mediate_interval(ncost_terms, array_rules.T[0], array_rules.T[1], ignore_errors=ignore_errors,
                                           ignore_warnings=ignore_warnings, verbose=verbose)
            # add values of constant variables
            cost_terms = [t for t in terms if t in self._constants]
            for name in cost_terms:
                result[name] = self._variables[name]

        return result

    def Mamdani_interval_inference(self, terms=None, subdivisions=1000, ignore_errors=False, ignore_warnings=False,
                                   verbose=False):
        """
        Performs Mamdani interval fuzzy inference.
            :param terms: names of the variables on which inference must be performed
                If empty, all variables appearing in the consequent of a IVFR are inferred.
            :type terms: list
            :param subdivisions: the number of integration steps to be performed for calculating fuzzy set area,
                defaults to 1000.
            :type subdivisions: int
            :param ignore_errors: toggles the raising of errors during the inference
            :type ignore_errors: bool
            :param ignore_warnings: toggles the raising of warnings during the inference
            :type ignore_warnings: bool
            :param verbose: toggles verbose mode
            :type verbose: bool
            :return: a dictionary, containing as keys the variables names and as values their interval inferred values
        """
        if self._sanitize and terms is not None:
            terms = [self._sanitize(term) for term in terms]

        # default: inference on ALL rules/terms
        if terms == None:
            temp = [rule[1][0] for rule in self._rules]
            terms = list(set(temp))
        else:
            # get rid of duplicates in terms to infer
            terms = list(set(terms))
            for t in terms:
                if t not in set([rule[1][0] for rule in self._rules]):
                    raise Exception("ERROR: Variable " + t + " does not appear in any consequent.")

        array_rules = array(self._rules, dtype=object)
        if len(self._constants) == 0:
            result = self.mediate_interval_Mamdani(terms, array_rules.T[0], array_rules.T[1],
                                                   ignore_errors=ignore_errors,
                                                   ignore_warnings=ignore_warnings, verbose=verbose,
                                                   subdivisions=subdivisions)
        else:
            # remove constant variables from list of variables to infer
            ncost_terms = [t for t in terms if t not in self._constants]
            result = self.mediate_interval_Mamdani(ncost_terms, array_rules.T[0], array_rules.T[1],
                                                   ignore_errors=ignore_errors,
                                                   ignore_warnings=ignore_warnings, verbose=verbose,
                                                   subdivisions=subdivisions)
            # add values of constant variables
            cost_terms = [t for t in terms if t in self._constants]
            for name in cost_terms:
                result[name] = self._variables[name]

        return result

