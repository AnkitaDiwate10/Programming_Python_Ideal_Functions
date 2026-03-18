from src.data_loader import DataLoader
from src.ideal_function_selector import IdealFunctionSelector
from src.test_mapper import TestMapper
from src.database import DatabaseManager
import pandas as pd
from src.visualization import Visualizer


def main():
    try:
        loader = DataLoader()

        train_data = loader.load_training_data("data/train.csv")
        ideal_data = loader.load_ideal_functions("data/ideal.csv")
        test_data = loader.load_test_data("data/test.csv")

        # Step 1: Select best ideal functions
        selector = IdealFunctionSelector()

        best_functions = {}

        for column in train_data.columns[1:]:
            best_func, error = selector.find_best_function(
                train_data[column],
                ideal_data
            )
            best_functions[column] = best_func

        print("\nSelected Ideal Functions:")
        print(best_functions)

        # Step 2: Map test data
        mapper = TestMapper()

        mapped_results = []

        for index, row in test_data.iterrows():
            x_test = row["x"]
            y_test = row["y"]

            for train_func, ideal_func in best_functions.items():
                ideal_value = ideal_data.loc[index, ideal_func]

                deviation = mapper.calculate_deviation(y_test, ideal_value)

                mapped_results.append({
                    "x": x_test,
                    "y": y_test,
                    "ideal_function": ideal_func,
                    "deviation": deviation
                })

        print("\nTest Mapping Results:")
        print(mapped_results[:10])

        # Convert mapping results into DataFrame
        results_df = pd.DataFrame(mapped_results)

        # Create database connection
        db = DatabaseManager()

        # Save datasets to database
        db.save_training_data(train_data)
        db.save_ideal_functions(ideal_data)
        db.save_test_results(results_df)

        # Visualization
        visualizer = Visualizer()
        visualizer.plot_data(train_data, ideal_data, test_data)

        print("Project version updated")

    except FileNotFoundError as e:
        print("Error: One of the data files was not found.", e)

    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()

        
