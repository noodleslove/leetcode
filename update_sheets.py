import pandas as pd
import df2gspread.df2gspread as d2g


SHEETS_ID = '10Uq6QKtkSVNVGoaYF81eEF9eNgQu20JFCVipo741akk'
worksheet_name = 'development'
logs_df = pd.read_csv('logs.csv')

d2g.upload(logs_df, SHEETS_ID, worksheet_name, row_names=True)
