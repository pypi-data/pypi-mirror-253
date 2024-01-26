import matplotlib.pyplot as plt

from . import plot_colors as plotColors

def trendPlot(xValues, yValues, **kwargs):
    """Plots matplotlib for given values

    Parameters
    ---
    xValues: list
        List of integers on x-axis
    
    yValues: list
        List of integer on y-axis

    **kwargs:
        * xTicks: list
            Data ticks for x values, defaults to xValues

        * rotateXTicks int
            Value is passed as matlplotlib xTicks rotation

        * xLabel: list
            Data label for x values
        
        * yLabel: list
            Data label for y values

        * plotTitle
            Plot title

        * trendValues
            List of integers to plot trend line

        * trendColor
            Color of the trend line

        * legends
            Legends for the plot

        * text
            Text to write in the center of the plot

        * textBackground
            Background color of the text

        * watermark
            Watermark for the plot

        * showValues
            Show bar values

        * saveToFile
            File path to save the image
    """

    midX = min(xValues) + (max(xValues) - min(xValues)) / 2
    midY = max(yValues) / 2

    fix, ax = plt.subplots(figsize=(10, 5))
    ax.bar(xValues, yValues, color = plotColors.YELLOW, width = 0.6)

    # Keyword arguments
    # xTicks, rotateXTicks
    rotateXTicks = 0
    if "rotateXTicks" in kwargs:
        rotateXTicks = kwargs["rotateXTicks"]

    plt.xticks(xValues, rotation = rotateXTicks)
    if "xTicks" in kwargs:
        ax.set_xticklabels(kwargs["xTicks"], rotation = rotateXTicks)

    # xLabel
    if "xLabel" in kwargs:
        ax.set_xlabel(kwargs["xLabel"], fontsize = 14)

    # yLabel
    if "yLabel" in kwargs:
        ax.set_ylabel(kwargs["yLabel"], fontsize = 14)

    # plotTitle
    if "plotTitle" in kwargs:
        ax.set_title(kwargs["plotTitle"], fontsize = 18)

    # trendValues, trendColor
    if "trendValues" in kwargs:
        trendValues = kwargs["trendValues"]
        trendArgs = dict(lw = 2.5)
        if "trendColor" in kwargs:
            trendArgs["c"] = kwargs["trendColor"]
        ax.plot(xValues, trendValues, **trendArgs)

    # legends
    if "legends" in kwargs:
        legends = kwargs["legends"]
        plt.legend(legends, loc ="upper left")

    # text, textBackground
    if "text" in kwargs:
        text = kwargs["text"]
        
        textBackground = "#f7f7f7"
        if "textBackground" in kwargs:
            textBackground = kwargs["textBackground"]

        textProps = dict(boxstyle='round', facecolor=textBackground, alpha=0.25)
        plt.text(
            midX, midY, text, fontsize=14, 
            bbox=textProps, va="center", ha="center"
        )

    # watermark
    if "watermark" in kwargs:
        watermark = kwargs["watermark"]
        plt.text(
            midX, midY / 10, watermark, fontsize=8, 
            bbox=dict(
                boxstyle="round", 
                facecolor=plotColors.LIGHT_GREY, 
                alpha=0.1
            ),
            va="center", ha="center", color="grey"
        )

    if "showValues" in kwargs:
        if kwargs["showValues"]:
            for i, bar in enumerate(ax.patches):
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height() / 2 + bar.get_y(),
                    yValues[i], ha = 'center',
                    color = "black", size = 10
                )

    if "saveToFile" in kwargs:
        fileName = kwargs["saveToFile"]
        plt.savefig(fileName, bbox_inches="tight", dpi=150)

    plt.show()