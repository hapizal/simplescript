#!/usr/bin/python

import sys

with open('server.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split the line into columns using a space (or any other delimiter)
        columns = line.split()
        # Check if there are at least two columns in the line
        if len(columns) >= 2:
            # Print the second column (index 1)
            print(columns[1])
