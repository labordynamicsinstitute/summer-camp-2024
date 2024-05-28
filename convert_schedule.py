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
    parser.add_argument('--credentials', default='auth.json', help='Path to the JSON key file')
    parser.add_argument('--output_file', default='schedule.md', help='Output Markdown file')
    return parser.parse_args()

def get_data_from_sheet(sheet_url, worksheet_name, credentials):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(sheet_url)
    table = sheet.worksheet(worksheet_name)
    records_data = table.get_all_records()
    return pd.DataFrame.from_dict(records_data)

def save_as_markdown(df, output_file):
    with open(output_file, 'w') as f:
        f.write(df.to_markdown(index=False))

def main():
    args = get_args()
    df = get_data_from_sheet(args.sheet_url, args.worksheet_name, args.credentials)
    save_as_markdown(df, args.output_file)

if __name__ == '__main__':
    main()
