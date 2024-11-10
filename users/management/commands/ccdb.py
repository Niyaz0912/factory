from django.core.management import BaseCommand
import pyodbc
from config.settings import DATABASE, USER, PASSWORD, HOST


class Command(BaseCommand):

    def handle(self, *args, **options):
        conn = None
        ConnectionString = f'''DRIVER={{ODBC Driver 17 for SQL Server}};
                               SERVER={HOST};
                               DATABASE=master;
                               UID={USER};
                               PWD={PASSWORD}'''
        try:
            conn = pyodbc.connect(ConnectionString)
            conn.autocommit = True
            conn.execute(fr"CREATE DATABASE {DATABASE};")
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            print("База данных factory успешно создана;")
        finally:
            if conn:  # Проверяем, что conn был создан перед закрытием
                conn.close()

