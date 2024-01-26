import simpful as sf
from numpy import linspace
from simpful import UndefinedUniverseOfDiscourseError

try:
    from matplotlib.pyplot import plot, show, title, subplots, legend
    import seaborn as sns

    matplotlib = True
except ImportError:
    matplotlib = False


class IntervalLinguisticVariable(sf.LinguisticVariable):
    """
    Class which represent new interval linguistic variable

    :param FS_list: a list of IVFS instances
    :param concept: a string providing a brief description of the concept represented by the linguistic variable,
        (optional)
    :param universe_of_discourse: a list of two elements, specifying min and max of the universe of discourse.
        Optional, but it must be specified to exploit plotting facilities.
    """

    def __init__(self, FS_list=[], concept=None, universe_of_discourse=None):
        """
        Constructor method
        """
        super().__init__(FS_list=FS_list, concept=concept, universe_of_discourse=universe_of_discourse)

    def get_values(self, v):
        result = {}
        for fs in self._FSlist:
            result[fs._term] = fs.get_value(v)
        return result

    def get_universe_of_discourse(self):
        """
        This method provides the leftmost and rightmost values of the universe of discourse of the linguistic variable.
            :return: the two boundary values of the universe of discourse.
            :rtype: tuple
        """
        if self._universe_of_discourse is not None:
            return self._universe_of_discourse
        mins = []
        maxs = []
        try:
            for fs in self._FSlist:
                mins.append(min(fs._points.T[0]))
                maxs.append(max(fs._points.T[0]))
        except AttributeError:
            raise UndefinedUniverseOfDiscourseError(
                "Cannot get the universe of discourse. Please, use point-based fuzzy sets or explicitly specify a universe of discourse")
        return min(mins), max(maxs)

    def draw(self, ax, TGT=None, highlight=None):
        """
        This method returns a matplotlib ax, representing all IVFS contained in the liguistic variable.
            :param ax: the matplotlib axis to plot to.
            :param TGT: show the memberships of a specific element of discourse TGT in the figure.
            :param highlight: string, indicating the linguistic term/fuzzy set to highlight in the plot.
            :return: A matplotlib axis, representing all IVFS contained in the liguistic variable.
        """
        if not matplotlib:
            raise Exception("ERROR: please, install matplotlib for plotting facilities")

        mi, ma = self.get_universe_of_discourse()
        x = linspace(mi, ma, 10000)

        if highlight is None:
            linestyles = ["-", "--", ":", "-."]
        else:
            linestyles = ["-"] * 4

        for nn, fs in enumerate(self._FSlist):
            if fs.get_type_start() == "function":
                y_start = [fs.get_value_start(xx) for xx in x]
                if fs.get_type_end() == "function":
                    y_end = [fs.get_value_end(xx) for xx in x]
                color = None
                lw = 1

                if highlight == fs.get_term():
                    color = "red"
                    lw = 5
                elif highlight is not None:
                    color = "lightgray"
                ax.plot(x, y_start, linestyles[nn % 4], lw=lw, label=fs.get_term(), color=color)
                if fs.get_type_end() == "function":
                    ax.plot(x, y_end, linestyles[nn % 4], lw=lw, label=fs.get_term(), color=color)
            else:
                pass
                # sns.regplot(x=fs._points.T[0], y=fs._points.T[1], marker="d", color="red", fit_reg=False, ax=ax)
                # f = interp1d(fs._points.T[0], fs._points.T[1], bounds_error=False,
                #              fill_value=(fs.boundary_values[0], fs.boundary_values[1]))
                # ax.plot(x, f(x), linestyles[nn % 4], label=fs._term, )
        if TGT is not None:
            ax.axvline(x=TGT, ymin=0.0, ymax=1.0, color="red", linestyle="--", linewidth=2.0)
        ax.set_xlabel(self._concept)
        ax.set_ylabel("Membership degree")
        ax.set_ylim(bottom=-0.05)
        if highlight is None: ax.legend(loc="best")
        return ax

    def plot(self, outputfile="", TGT=None, highlight=None):
        """
        Shows a plot representing all IVFS contained in the liguistic variable.
            :param outputfile: path and filename where the plot must be saved
            :type outputfile: str
            :param TGT: show the memberships of a specific element of discourse TGT in the figure
            :param highlight: string, indicating the linguistic term/fuzzy set to highlight in the plot.
        """
        if not matplotlib:
            raise Exception("ERROR: please, install matplotlib for plotting facilities")

        fig, ax = subplots(1, 1)
        self.draw(ax=ax, TGT=TGT, highlight=highlight)

        if outputfile != "":
            fig.savefig(outputfile)

        show()