import csv
import pandas as pd

input_file = 'txt.txt'
output_file = 'output.csv'

#convert txt file to csv
def add_commas_to_csv_ignore_whitespace(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        for line in infile:
            line = ''.join(line.split())
            row = [line[i:i+5] for i in range(0, len(line), 5)] 
            csv_writer.writerow(row)

add_commas_to_csv_ignore_whitespace(input_file, output_file)

#action csv requirements
dataframe = pd.read_csv('output.csv', header=None)
sorted_dataframe = dataframe.apply(sorted, axis=0)
sorted_dataframe['Difference'] = abs(sorted_dataframe[0] - sorted_dataframe[1])
sorted_dataframe['Count in B'] = sorted_dataframe[0].apply(lambda x: (sorted_dataframe[1] == x).sum())
sorted_dataframe['Product'] = sorted_dataframe[0] * sorted_dataframe['Count in B']
sorted_dataframe.to_csv('sorted_complete.csv', index=False, header=False)
difference_sum = sorted_dataframe['Difference'].sum()
total_product_sum = sorted_dataframe['Product'].sum()

print(f"The answer to part 1 = {difference_sum}")
print(f"The answer to part 2 = {total_product_sum}")
