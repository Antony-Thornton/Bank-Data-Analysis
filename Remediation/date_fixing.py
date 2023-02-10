# Import libraries
import pandas as pd
import numpy as np

# Import scripts
import Data.get_data


def fix_date(df):
    print("Running date fixing", end='\n\n')

    df = df[['day', 'month', 'duration']]

    months = pd.Series(df['month'])

    unique_months = months.nunique()
    print("Total unique months found = ", unique_months, end='\n\n')

    fixed_months = pd.DataFrame({'fixed_months': [
        'jan',
        'feb',
        'mar',
        'apr',
        'may',
        'jun',
        'jul',
        'aug',
        'sep',
        'oct',
        'nov',
        'dec',
    ]})
    fixed_months['Full Months'] = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]
    fixed_months['Month Numbers'] = [
        '01',
        '02',
        '03',
        '04',
        '05',
        '06',
        '07',
        '08',
        '09',
        '10',
        '11',
        '12',
    ]

    df['day'] = df['day'].astype(str)
    df['day'] = np.where(
        (df['day'].str.len() == 1),
        "0" + df['day'],
        df['day']
    )

    new_df = pd.merge(
        df,
        fixed_months,
        how='left',
        left_on=['month'],
        right_on='fixed_months',
        indicator=True,
    )

    new_df['Full Date'] = new_df['day'].astype(str) + " " + new_df['Full Months'] + " 2022"
    new_df['day'] = new_df['day'].astype(str)
    new_df['Month Numbers'] = new_df['Month Numbers'].astype(str)
    new_df['Full Date Numbered'] = new_df['day'] + "/" + new_df['Month Numbers'] + "/2022"
    new_df['Full Date Numbered'] = pd.to_datetime(new_df['Full Date Numbered'].str.strip(), format='%d/%m/%Y')

    print(new_df.dtypes)

    print(new_df.head(100).to_markdown())



def all_def():
    fix_date(df)


df = Data.get_data.create_data_frame()