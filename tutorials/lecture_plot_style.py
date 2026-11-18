from cycler import cycler
from matplotlib.colors import LinearSegmentedColormap

# Print style for the lecture-note figures. Widths are in inches at final size.
plot_width = {"single": 3.02, "paired": 2.83, "wide": 5.67, "third": 1.99}
plot_blue = "#245b83"
plot_clay = "#914b43"
surface_blue = LinearSegmentedColormap.from_list(
    "lecture_blue", [plot_blue, "#8baec7", "#eaf1f6"]
)
surface_diverging = LinearSegmentedColormap.from_list(
    "lecture_blue_clay", [plot_blue, "#f2f5f9", plot_clay]
)
lecture_plot_style = {
    "axes.prop_cycle": cycler(color=[plot_blue, plot_clay, "#567366", "#725779", "#806322"]),
    "lines.linewidth": 1.2,
    "figure.constrained_layout.use": True,
    "font.family": "serif",
    "font.size": 9,
    "axes.titlesize": 9,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "axes.edgecolor": "#4b5563",
    "axes.labelcolor": "#263340",
    "xtick.color": "#263340",
    "ytick.color": "#263340",
    "axes.linewidth": 0.6,
    "grid.color": "#b4bdc7",
    "grid.linewidth": 0.5,
    "axes.axisbelow": True,
    "legend.frameon": False,
    "savefig.transparent": True,
}
