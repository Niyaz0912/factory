from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import pandas as pd

# Настройка доступа к Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'C:/Users/Нияз/PycharmProjects/NiyazProduction_new/service-account.json'


credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SPREADSHEET_ID = 'your_google_sheet_id'  # Замените на ID вашей таблицы


def read_google_sheet(range_name):
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
    values = result.get('values', [])

    if not values:
        return pd.DataFrame()  # Если нет данных, возвращаем пустой DataFrame

    return pd.DataFrame(values[1:], columns=values[0])  # Преобразуем в DataFrame


def write_to_google_sheet(range_name, data):
    service = build('sheets', 'v4', credentials=credentials)
    body = {'values': data}
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()
