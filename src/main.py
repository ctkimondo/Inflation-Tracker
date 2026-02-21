from extract import fetch_data_cpi
from transform import parse_oecd_cpi
from load import save_data, upload_to_s3


def pipeline():
    print("-- Starting pipeline --")

    # Extract
    raw_json = fetch_data_cpi()
    print(f"Extraction successful. Received {len(raw_json)} bytes.")

    # Transform
    clean_df = parse_oecd_cpi(raw_json)
    print(f"Transformation Successful. Processed {len(clean_df)} records.")

    save_data(clean_df, "data/inflation_2023.parquet")
    upload_to_s3("data/inflation_2023.parquet", "inflation-tracker-storage")
    print("Complete")

if __name__ == "__main__":
    pipeline()