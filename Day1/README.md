# <ins> DAY 1 </ins>

## Times
I got up really late so my times were atrocious!

| Day | Part | Time     | Rank   | Score |
|-----|------|----------|--------|-------|
|  1  |  1   | 06:40:07 | 37312  |   0   |
|     |  2   | 06:48:38 | 34736  |   0   |

## Solution 
### Part 1
Overall, nice easy introduction. 
I started by thinking of ways to make the input file a bit easier to work with, maybe a few loops or splitting by line with some regex to split the numbers based on white spaces etc.

I wanted some practice with Pandas so I settled with writing a short script that would place a comma every 5 characters (ignoring whitespaces) and then converting to a comma delimited version (CSV). Now I had 2 columns to work with and easy access to Pandas to do all the work :D.

First thing was to sort the columns independently by their value in ascending order:

```
dataframe = pd.read_csv('output.csv', header=None)
sorted_dataframe = dataframe.apply(sorted, axis=0)
```

Then get the difference between the columns and add them up:

```
sorted_dataframe['Difference'] = abs(sorted_dataframe[0] - sorted_dataframe[1])
difference_sum = sorted_dataframe['Difference'].sum()
print(f"The answer to part 1 = {difference_sum}")
```

Part 1 complete!

### Part 2
Didn't take long to figure this out now I had pandas doing the heavy lifting. Lost lots of time troubleshooting though...

First, we need to get how often numbers in column A appear in column B:

```
sorted_dataframe['Count in B'] = sorted_dataframe[0].apply(lambda x: (sorted_dataframe[1] == x).sum())
```
Then multiply them!

```
sorted_dataframe['Product'] = sorted_dataframe[0] * sorted_dataframe['Count in B']
```

And thats game!

```
total_product_sum = sorted_dataframe['Product'].sum()
print(f"The answer to part 2 = {total_product_sum}")
```
