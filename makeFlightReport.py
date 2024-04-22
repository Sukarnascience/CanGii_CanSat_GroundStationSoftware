import os
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Get a list of all CSV files in the current directory
csv_files = [file for file in os.listdir() if file.endswith('.csv')]

# Step 2: Iterate over each CSV file
for file in csv_files:
    # Step 3: Read the CSV file using Pandas
    df = pd.read_csv(file)
    
    # Step 4: Get the list of column names
    column_names = df.columns
    
    # Step 5: Generate x-values as integers (1, 2, 3, ...)
    x_values = range(1, len(df) + 1)
    
    # Step 6: Iterate over each column
    for column in column_names:
        # Step 7: Plot the data for the current column
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, df[column])
        plt.xlabel('Index')
        plt.ylabel(column)
        plt.title(f'Plot for {column} in {file}')
        plt.savefig(f"{os.path.splitext(file)[0]}_{column}_plot.png")
        plt.close()  # Close the plot to free memory
