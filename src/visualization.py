from bokeh.plotting import figure, show, output_file

class Visualizer:
    """
    This class is responsible for visualizing the training data,
    ideal functions, and test data using Bokeh.
    """

    def plot_data(self, train_data, ideal_data, test_data, results_df):
        """
        Plots training data, ideal functions, and test data.
        Highlights 'Not Assigned' points in red crosses.
        """
        # Output HTML file
        output_file("visualization.html")

        # Create figure
        p = figure(
            title="Training Data, Ideal Functions and Test Data Mapping",
            x_axis_label="X",
            y_axis_label="Y",
            width=900,
            height=600
        )

        # -----------------------------
        # Plot training data
        # -----------------------------
        for column in train_data.columns[1:]:
            p.line(
                train_data["x"],
                train_data[column],
                legend_label=column,
                line_width=2,
                color="blue"
            )

        # -----------------------------
        # Plot ideal functions
        # -----------------------------
        for column in ideal_data.columns[1:]:
            p.line(
                ideal_data[ideal_data.columns[0]],
                ideal_data[column],
                line_dash="dashed",
                line_width=2,
                color="green",
                legend_label=column
            )

        # -----------------------------
        # Plot test data
        # -----------------------------
        # Separate assigned and not-assigned points
        assigned = results_df[results_df['ideal_function'] != "Not Assigned"]
        not_assigned = results_df[results_df['ideal_function'] == "Not Assigned"]

        # Assigned points → orange circles
        if not assigned.empty is False:
            p.circle(
                assigned['x'],
                assigned['y'],
                size=6,
                color="orange",
                legend_label="Assigned Test Data"
            )

        # Not Assigned points → red crosses
        if not not_assigned.empty is False:
            p.cross(
                not_assigned['x'],
                not_assigned['y'],
                size=8,
                color="red",
                legend_label="Not Assigned Test Data"
            )

        # Legend location
        p.legend.location = "top_left"

        # Show plot
        show(p)