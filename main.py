# Import Python Libraries
import tabulate

import Data.get_data
import visuals.visuals


def main():
    print()
    print("Data Frame imported.", end='\n\n')

    df = Data.get_data.create_data_frame()
    visuals.visuals.all_def()

    return df


if __name__ == "__main__":
    main()


