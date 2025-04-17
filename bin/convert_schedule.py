#!/usr/bin/env python3
# _main.py
import argparse
import gspread
import pandas as pd
import os
from oauth2client.service_account import ServiceAccountCredentials

def get_args():
    parser = argparse.ArgumentParser(description='Pull data from a Google Spreadsheet and format it into a Markdown table.')
    parser.add_argument('--sheet_url', default='https://docs.google.com/spreadsheets/d/1JfAU-vIPOKvlVm01hFLmG0_LLw7SP5th11UhvHp_GIo/', help='URL of the Google Spreadsheet')
    parser.add_argument('--years', default='2024,2025', help='Comma-separated list of years to pull data for')
    parser.add_argument('--credentials', required=True, help='Path to the JSON key file')
    parser.add_argument('--output_dir', default='_data', help='Directory for output CSV files')
    return parser.parse_args()

def get_data_from_sheet(sheet_url, worksheet_name, credentials, selected_columns, blank_columns=None, consent='Yes'):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(sheet_url)
    
    try:
        table = sheet.worksheet(worksheet_name)
        records_data = table.get_all_records()
        df = pd.DataFrame.from_dict(records_data)
        
        # Filter rows where 'Consent' is 'yes'
        if blank_columns is not None and 'Consent' in df.columns:
            df.loc[df['Consent'] != consent, blank_columns] = ''

        # Set Time column to 'TBD' if it is empty
        if 'Time' in df.columns:
            df['Time'] = df['Time'].apply(lambda x: 'TBD' if pd.isnull(x) or x == '' else x)

        # Select certain columns
        available_columns = [col for col in selected_columns if col in df.columns]
        df = df[available_columns]
        
        return df
    except gspread.exceptions.WorksheetNotFound:
        print(f"Worksheet '{worksheet_name}' not found. Returning empty DataFrame.")
        return pd.DataFrame(columns=selected_columns)

def save_as_csv(df, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write(df.to_csv(index=False))

def main():
    args = get_args()
    selected_columns = ['Week','Date','Time','Who','Current affiliation','Brief vitae','Personal website']
    blank_columns = ['Who','Current affiliation','Brief vitae','Personal website']
    
    years = [year.strip() for year in args.years.split(',')]
    
    for year in years:
        worksheet_name = f'Summer {year}'
        output_file = os.path.join(args.output_dir, f'schedule_{year}.csv')
        
        print(f"Processing data for {year}...")
        df = get_data_from_sheet(
            sheet_url=args.sheet_url, 
            worksheet_name=worksheet_name, 
            credentials=args.credentials,
            selected_columns=selected_columns,
            blank_columns=blank_columns
        )
        
        save_as_csv(df, output_file)
        print(f"Data for {year} saved to {output_file}")

if __name__ == '__main__':
    main()
