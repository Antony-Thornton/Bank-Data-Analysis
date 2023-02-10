# Import Python Libraries

# Import scripts
import Data.get_data
import visuals.visuals
import Remediation.date_fixing


def main():
    print("Data Frame imported.", end='\n\n')

    df = Data.get_data.create_data_frame()
    # visuals.visuals.all_def()
    Remediation.date_fixing.all_def()

    return df


if __name__ == "__main__":
    main()


