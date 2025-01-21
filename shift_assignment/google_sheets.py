from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import pandas as pd

# Настройка доступа к Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'C:/Users/Нияз/PycharmProjects/NiyazProduction_new/service-account.json'

# Получение учетных данных из файла сервисного аккаунта
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SPREADSHEET_ID = 'your_google_sheet_id'  # Замените на ID вашей таблицы


def read_google_sheet(range_name):
    """
    Читает данные из указанного диапазона Google Sheets.

    Параметры:
    range_name (str): Диапазон ячеек для чтения, например 'Sheet1!A1:D10'.

    Возвращает:
    pd.DataFrame: Данные из таблицы в виде DataFrame. Если данных нет, возвращает пустой DataFrame.
    """
    service = build('sheets', 'v4', credentials=credentials)  # Создание сервиса для работы с API
    sheet = service.spreadsheets()

    # Получение значений из таблицы
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
    values = result.get('values', [])

    if not values:
        return pd.DataFrame()  # Если нет данных, возвращаем пустой DataFrame

    # Преобразуем полученные данные в DataFrame, используя первую строку как заголовки
    return pd.DataFrame(values[1:], columns=values[0])


def write_to_google_sheet(range_name, data):
    """
    Записывает данные в указанный диапазон Google Sheets.

    Параметры:
    range_name (str): Диапазон ячеек для записи, например 'Sheet1!A1'.
    data (list): Данные для записи в таблицу в формате списка списков.
    """
    service = build('sheets', 'v4', credentials=credentials)  # Создание сервиса для работы с API
    body = {'values': data}  # Форматируем данные для записи

    # Обновление значений в таблице
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=range_name,
        valueInputOption='RAW',
        body=body
    ).execute()

