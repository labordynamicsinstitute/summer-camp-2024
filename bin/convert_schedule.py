#!/usr/bin/env python3
# _main.py
import argparse
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def get_args():
    parser = argparse.ArgumentParser(description='Pull data from a Google Spreadsheet and format it into a Markdown table.')
    parser.add_argument('--sheet_url', default='https://docs.google.com/spreadsheets/d/1JfAU-vIPOKvlVm01hFLmG0_LLw7SP5th11UhvHp_GIo/', help='URL of the Google Spreadsheet')
    parser.add_argument('--worksheet_name', default='Summer 2024', help='Name of the worksheet')
    parser.add_argument('--credentials', required=True, help='Path to the JSON key file')
    parser.add_argument('--output_file', default='schedule.csv', help='Output CSV file')
    return parser.parse_args()

def get_data_from_sheet(sheet_url, worksheet_name, credentials,selected_columns,blank_columns=None,consent='Yes'):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(sheet_url)
    table = sheet.worksheet(worksheet_name)
    records_data = table.get_all_records()
    df = pd.DataFrame.from_dict(records_data)
    
    # Filter rows where 'Consent' is 'yes'
    if blank_columns is not None:
        df.loc[df['Consent'] != consent, blank_columns] = ''

    # Set Time column to 'TBD' if it is empty
    df['Time'] = df['Time'].apply(lambda x: 'TBD' if pd.isnull(x) or x == '' else x)

    # Select certain columns
    df = df[selected_columns]
    
    return df

def save_as_csv(df, output_file):
    with open(output_file, 'w') as f:
        f.write(df.to_csv(index=False))

def main():
    args = get_args()
    selected_columns = ['Week','Date','Time','Who','Current affiliation','Brief vitae','Personal website']
    blank_columns = ['Who','Current affiliation','Brief vitae','Personal website']
    df = get_data_from_sheet(sheet_url=args.sheet_url, worksheet_name=args.worksheet_name, credentials=args.credentials,
                             selected_columns=selected_columns,blank_columns=blank_columns)
    save_as_csv(df, args.output_file)

if __name__ == '__main__':
    main()
