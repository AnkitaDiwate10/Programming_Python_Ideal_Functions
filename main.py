from src.data_loader import DataLoader
from src.ideal_function_selector import IdealFunctionSelector
from src.test_mapper import TestMapper
from src.database import DatabaseManager
from src.visualization import Visualizer
import pandas as pd
import numpy as np
import math


def main():
    try:
        # -----------------------------
        # Step 0: Load data
        # -----------------------------
        loader = DataLoader()
        train_data = loader.load_training_data("data/train.csv")
        ideal_data = loader.load_ideal_functions("data/ideal.csv")
        test_data = loader.load_test_data("data/test.csv")

        # Automatically detect the first column of ideal_data as x-values
        x_col = ideal_data.columns[0]

        # -----------------------------
        # Step 1: Select best ideal functions
        # -----------------------------
        selector = IdealFunctionSelector()
        best_functions = {}

        for column in train_data.columns[1:]:  # skip first column (X)
            best_func, error = selector.find_best_function(
                train_data[column],
                ideal_data
            )
            best_functions[column] = best_func

        print("\nSelected Ideal Functions:")
        print(best_functions)

        # -----------------------------
        # Step 1A: Compute max training deviations (for threshold)
        # -----------------------------
        max_train_deviation = {}
        for train_func, ideal_func in best_functions.items():
            deviations = abs(train_data[train_func] - ideal_data[ideal_func])
            max_train_deviation[train_func] = deviations.max()

        # -----------------------------
        # Step 2: Map test data
        # -----------------------------
        mapper = TestMapper()
        mapped_results = []

        for index, row in test_data.iterrows():
            x_test = row["x"]
            y_test = row["y"]

            deviations_per_func = {}

            for train_func, ideal_func in best_functions.items():
                # Interpolate ideal y-value at x_test
                ideal_y = np.interp(x_test, ideal_data[x_col], ideal_data[ideal_func])
                deviation = abs(y_test - ideal_y)
                deviations_per_func[train_func] = deviation

            # Find minimum deviation and corresponding training function
            min_train_func = min(deviations_per_func, key=deviations_per_func.get)
            min_deviation = deviations_per_func[min_train_func]

            # Apply threshold: max_train_deviation * sqrt(2)
            threshold = max_train_deviation[min_train_func] * math.sqrt(2)

            if min_deviation <= threshold:
                assigned_ideal_func = best_functions[min_train_func]
            else:
                assigned_ideal_func = "Not Assigned"
                min_deviation = None  # optional for database/visualization

            mapped_results.append({
                "x": x_test,
                "y": y_test,
                "ideal_function": assigned_ideal_func,
                "deviation": min_deviation
            })

        # -----------------------------
        # Step 3: Convert mapping results into DataFrame
        # -----------------------------
        results_df = pd.DataFrame(mapped_results)
        # Print all mapping results
        print("\nTest Mapping Results:")
        print(results_df)

        # -----------------------------
        # Step 4: Save data to database
        # -----------------------------
        db = DatabaseManager()
        db.save_training_data(train_data)
        db.save_ideal_functions(ideal_data)
        db.save_test_results(results_df)

        # -----------------------------
        # Step 5: Visualization
        # -----------------------------
        visualizer = Visualizer()
        visualizer.plot_data(train_data, ideal_data, test_data, results_df)

        print("Project version updated")

    except FileNotFoundError as e:
        print("Error: One of the data files was not found.", e)

    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()