import pathlib
import pandas as pd
import openpyxl
import tabulate

# Import config information


def create_data_frame():
    import config

    user = config.user
    data_path = config.data_path
    file_name = config.file_name

    full_path = pathlib.Path(data_path, file_name)

    data = pd.read_excel(full_path, sheet_name='bank.xlsx')
    df = pd.DataFrame(data)

    return df

create_data_frame()
