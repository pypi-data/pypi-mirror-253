import pandas as pd
import numpy as np
import sys

def topsis(filename, weights, impacts, resultFile):
    try:
        # Step 1: Getting Decision Matrix
        # Reading the file
        
        dataorg = pd.read_csv(filename)

        # Dropping col[0]
        data = dataorg.drop(dataorg.columns[0], axis=1)

        # Converting dataset to floating numbers for further calculation
        df = pd.DataFrame(data).to_numpy(dtype=float)

        # Step 2: Calculating Normalized Decision Matrix
        n_rows = df.shape[0]
        n_cols = df.shape[1]

        denom = []

        for j in range(n_cols):
            col_sum = sum(df[i][j] ** 2 for i in range(n_rows))
            value = col_sum ** 0.5
            denom.append(value)

        # Updating Matrix
        for i in range(n_rows):
            for j in range(n_cols):
                df[i][j] = df[i][j] / denom[j]

        # Step 3: Multiplying weights (Weighted Normalized Matrix)
        weights_list = weights.split(',')
        
        # Checking if the number of weights matches the number of columns
        if len(weights_list) != n_cols:
            raise ValueError("Number of weights must be equal to the number of columns.")
        
        # Converting the weights to a list of floats
        weights = list(map(float, weights_list))

        for j in range(n_cols):
            for i in range(n_rows):
                df[i][j] = df[i][j] * weights[j]

        # Step 4: Ideal best and worst for each column
        impacts = [1 if imp == '+' else -1 for imp in impacts]

        maximum = np.amax(df, axis=0)
        minimum = np.amin(df, axis=0)
        best = []
        worst = []

        for i in range(n_cols):
            if impacts[i] == 1:
                best.append(maximum[i])
                worst.append(minimum[i])
            elif impacts[i] == -1:
                best.append(minimum[i])
                worst.append(maximum[i])

        # Step 5: Calculating Euclidean distance from best and worst
        distance_best = np.linalg.norm(df - best, axis=1)
        distance_worst = np.linalg.norm(df - worst, axis=1)

        # Step 6: Calculating Performance
        performance = distance_worst / (distance_worst + distance_best)
        performance = np.round(performance, 5)
        result_df = pd.concat([dataorg, pd.Series(performance, name='Performance')], axis=1)
        result_df = result_df.sort_values(by='Performance', ascending=False).reset_index(drop=True)
        result_df['Rank'] = result_df.index + 1

        # Step 7: Calculating Rank
        # rank = np.argsort(-performance) + 1  # Adding 1 to make it 1-based index

        # Step 8: Writing Results to Output File
        # result_df = pd.DataFrame({
        #     'Performance Score': performance,
        #     'Rank': rank
        # })
        # result_df = pd.concat([dataorg, result_df], axis=1)
        result_df.to_csv(resultFile, index=False)
        
        print("Results written to", resultFile)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    except ValueError as ve:
        print(f"Error: {ve}")

def main():
  if len(sys.argv) != 5:
    print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
    print("Example: python topsis.py input_data.csv \"1,1,1,2\" \"+,+,-,+\" result_output.csv")
  else:
    input_file, weights, impacts, result_file = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    topsis(input_file, weights, impacts, result_file)

  
if (__name__=="__main__"):
  main()



