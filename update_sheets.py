import os
import pandas as pd
import df2gspread.df2gspread as d2g


SHEETS_ID = '10Uq6QKtkSVNVGoaYF81eEF9eNgQu20JFCVipo741akk'

METADATA = '''My Leetcode Solutions
===

#### LeetCode Algorithm

'''

TABLE_FILE = './solution_table.md'
README_FILE = './README.md'

worksheet_name = 'development'

logs_df = pd.read_csv('logs.csv')
logs_df.to_markdown(TABLE_FILE, index=False)

# update README.md
with open(README_FILE, 'w') as output:
    input = open(TABLE_FILE, 'r').read()
    output.write(METADATA + input + '\n')

# remove table file
if os.path.isfile(TABLE_FILE):
    os.remove(TABLE_FILE)

d2g.upload(logs_df, SHEETS_ID, worksheet_name, row_names=True)
