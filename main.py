# Import Python Libraries

import Data.get_data


def test(df):
    print(df.head(10).to_markdown())


df = Data.get_data.create_data_frame()