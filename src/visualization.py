from bokeh.plotting import figure, show, output_file

class Visualizer:
    """
    This class is responsible for visualizing the training data,
    ideal functions, and test data using Bokeh.
    """

    def plot_data(self, train_data, ideal_data, test_data):

        output_file("visualization.html")

        p = figure(
            title="Training Data, Ideal Functions and Test Data",
            x_axis_label="X",
            y_axis_label="Y",
            width=900,
            height=600
        )

        # Plot training data
        for column in train_data.columns[1:]:
            p.line(train_data["x"], train_data[column],
                   legend_label=column, line_width=2)

        # Plot test data
        p.scatter(test_data["x"], test_data["y"],
                 size=6, color="red", legend_label="Test Data")

        show(p)