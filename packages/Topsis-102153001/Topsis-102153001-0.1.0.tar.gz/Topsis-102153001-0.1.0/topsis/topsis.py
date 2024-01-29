# topsis/topsis.py
import pandas as pd
import numpy as np

def topsis(input_file, weights_and_impacts, result_file):
    try:
        # Read input CSV file
        data = pd.read_csv(input_file)

        # Extract weights and impacts from the command line argument
        weights = list(map(float, list(weights_and_impacts)))
        impacts = [1 if imp == '+' else -1 for imp in list(weights_and_impacts)]

        # Check for the correct number of parameters
        if len(weights) != len(impacts) or len(weights) != len(data.columns) - 1:
            raise ValueError("Number of weights, impacts, and columns in the input file should be the same.")

        # Normalize the data
        normalized_data = data.copy()
        for i, col in enumerate(data.columns[1:]):
            normalized_data[col] = data[col] / np.linalg.norm(data[col])

        # Weighted normalized data
        weighted_normalized_data = normalized_data.copy()
        for i, col in enumerate(data.columns[1:]):
            weighted_normalized_data[col] = normalized_data[col] * weights[i]

        # Positive and negative ideal values
        positive_ideal = np.max(weighted_normalized_data, axis=0)
        negative_ideal = np.min(weighted_normalized_data, axis=0)

        # Positive-negative and negative-positive ideal distances
        pos_neg_ideal_dist = np.linalg.norm(weighted_normalized_data - positive_ideal, axis=1)
        neg_pos_ideal_dist = np.linalg.norm(weighted_normalized_data - negative_ideal, axis=1)

        # Topsis score
        topsis_score = neg_pos_ideal_dist / (neg_pos_ideal_dist + pos_neg_ideal_dist)
        #Final score

        # Rank
        rank = np.argsort(topsis_score) + 1

        # Create the result dataframe
        result_df = pd.DataFrame({
            'Object/Variable': data.iloc[:, 0],
            'Normalized Value': normalized_data.iloc[:, 1:].sum(axis=1),
            'Weighted Normalized Value': weighted_normalized_data.iloc[:, 1:].sum(axis=1),
            'Positive-Negative Ideal Distance': pos_neg_ideal_dist,
            'Negative-Positive Ideal Distance': neg_pos_ideal_dist,
            'Topsis Score': topsis_score,
            'Rank': rank
        })

        # Save the result to a CSV file
        result_df.to_csv(result_file, index=False)
        print("Topsis analysis completed. Result saved to", result_file)

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as e:
        print("Error:", e)
