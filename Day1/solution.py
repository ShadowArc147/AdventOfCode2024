import csv
import pandas as pd

def add_commas_to_csv_ignore_whitespace(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        for line in infile:
            # Remove whitespace and newline characters from the line
            line = ''.join(line.split())
            # Split the cleaned line into groups of 5 characters
            row = [line[i:i+5] for i in range(0, len(line), 5)]
            # Write the row to the CSV file
            csv_writer.writerow(row)

# Define the input and output file paths
input_file = 'txt.txt'
output_file = 'output.csv'

# Call the function
add_commas_to_csv_ignore_whitespace(input_file, output_file)

print(f"Processed lines written to CSV file: {output_file}")

import pandas as pd

# Read the CSV file without headers
dataframe = pd.read_csv('output.csv', header=None)

# Sort each column independently
sorted_dataframe = dataframe.apply(sorted, axis=0)

# Calculate the numerical difference between the two columns
sorted_dataframe['Difference'] = abs(sorted_dataframe[0] - sorted_dataframe[1])

# Check how often values in column A appear in column B
sorted_dataframe['Count in B'] = sorted_dataframe[0].apply(lambda x: (sorted_dataframe[1] == x).sum())

# Calculate the product of column A and Count in B
sorted_dataframe['Product'] = sorted_dataframe[0] * sorted_dataframe['Count in B']

# Print the products
print("Values in column A multiplied by their Count in B:")
print(sorted_dataframe[['Product']])

# Save the updated DataFrame to a new CSV file
sorted_dataframe.to_csv('sorted_with_counts_and_products.csv', index=False, header=False)

print("CSV file with counts and products saved as 'sorted_with_counts_and_products.csv'.")
total_product_sum = sorted_dataframe['Product'].sum()
print(f"The total sum of the Product column is: {total_product_sum}")
