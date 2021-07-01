#!/usr/bin/python3
"""function to read and filter data"""
if __name__ == "__main__":
    import pandas as pd
    import sys
    data = pd.read_csv(sys.argv[1]).query("año >= 2019")
    data.to_csv("data_filtered.csv")
