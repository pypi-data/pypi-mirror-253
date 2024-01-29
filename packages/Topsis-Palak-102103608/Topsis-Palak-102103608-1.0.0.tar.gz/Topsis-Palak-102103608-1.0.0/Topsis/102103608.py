import pandas as pd
import numpy as np
import sys

def topsis(filename, weights, impacts, resultFile):
    try:
        
        
        data_org = pd.read_csv(filename)

        
        data = data_org.drop(data_org.columns[0], axis=1)

        
        df = pd.DataFrame(data).to_numpy(dtype=float)

        
        nrow = df.shape[0]
        ncol = df.shape[1]

        d = []

        for j in range(ncol):
            sum1 = sum(df[i][j] ** 2 for i in range(nrow))
            value = sum1 ** 0.5
            d.append(value)

        
        for i in range(nrow):
            for j in range(ncol):
                df[i][j] = df[i][j] / d[j]

        
        weights_l = weights.split(',')
        
        
        if len(weights_l) != ncol:
            raise ValueError("Number of weights must be equal to the number of columns.")
        
        
        weights = list(map(float, weights_l))

        for j in range(ncol):
            for i in range(nrow):
                df[i][j] = df[i][j] * weights[j]

        
        impacts = [1 if imp == '+' else 0 for imp in impacts]

        maxi = np.amax(df, axis=0)
        mini = np.amin(df, axis=0)
        b = []
        w = []

        for i in range(ncol):
            if impacts[i] == 1:
                b.append(maxi[i])
                w.append(mini[i])
            elif impacts[i] == 0:
                b.append(mini[i])
                w.append(maxi[i])

        
        db = np.linalg.norm(df - b, axis=1)
        dw = np.linalg.norm(df - w, axis=1)

        
        p = dw / (dw+db)
        p= np.round(p, 5)
        result = pd.concat([data_org, pd.Series(p, name='Topsis Score')], axis=1)
        result = result.sort_values(by='Topsis Score', ascending=False).reset_index(drop=True)
        result['Rank'] = result.index + 1

        
        result.to_csv(resultFile, index=False)
        
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



