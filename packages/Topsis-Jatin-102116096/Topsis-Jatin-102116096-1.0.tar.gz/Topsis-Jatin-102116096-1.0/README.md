## Topsis Python Package

Made By Jatin Thakur (Roll No. 102116096)

# Description

The Topsis Python Package is a Python library that provides an implementation of the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method. TOPSIS is a multi-criteria decision-making method used to determine the best alternative among a set of alternatives based on their performance on multiple criteria.

# Features

Efficient Topsis Analysis: The package efficiently calculates Topsis scores and ranks for decision-making alternatives given a dataset.

Command-Line Interface: Use the command-line interface to run Topsis analysis easily with specified parameters.

Error Handling: The package includes robust error handling to provide clear feedback on incorrect inputs or missing files.

# Installation

pip install topsis-jatin-102116096

# Usage

Please provide the filename for the CSV, including the .csv extension. After that, enter the weights vector with values separated by commas. Following the weights vector, input the impacts vector, where each element is denoted by a plus (+) or minus (-) sign. Lastly, specify the output file name along with the .csv extension.

# Example Usage

The below example is for the data have 5 columns.

python program.py InputDataFile Weights Impacts ResultFileName

Example : python Topsis 102116096-data.csv "1,1,1,1,1" "+,-,+,+,+" 102116096-result.csv

# Important Points

There should be only numeric columns except the first column i.e. Fund Name.
Input file must contain atleast three columns.