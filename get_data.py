#This file contain a script getting data from data.gouv.fr via API


import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, help="Input CSV file")
parser.add_argument("--output", required=True, help="Output CSV file")
args = parser.parse_args()

# Load data
df = pd.read_csv(args.input)

# Example transformation
df["processed_column"] = df["existing_column"] * 2  

# Save processed data
df.to_csv(args.output, index=False)

print(f"Processed {args.input} and saved as {args.output}")

