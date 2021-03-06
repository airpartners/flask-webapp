import os
try:
    user_profile = os.path.basename(os.path.normpath(os.environ['USERPROFILE']))
except KeyError:
    user_profile = "mmezaki"

if user_profile == "ieykamp":
    raw_csv_paths = [
        "C:/dev/Air Partners/Data Analysis/data/east_boston/raw/sn45-final-w-ML-PM.csv",
        "C:/dev/Air Partners/Data Analysis/data/east_boston/raw/sn46-final-w-ML-PM.csv",
        "C:/dev/Air Partners/Data Analysis/data/east_boston/raw/sn49-final-w-ML-PM.csv",
        "C:/dev/Air Partners/Data Analysis/data/east_boston/raw/sn62-final-w-ML-PM.csv",
        "C:/dev/Air Partners/Data Analysis/data/east_boston/raw/sn67-final-w-ML-PM.csv",
        "C:/dev/Air Partners/Data Analysis/data/east_boston/raw/sn72-final-w-ML-PM.csv",
    ]

    processed_csv_paths = [
        "C:/dev/Air Partners/Data Analysis/data/east_boston/processed/sn45-final-w-ML-PM.parquet",
        "C:/dev/Air Partners/Data Analysis/data/east_boston/processed/sn46-final-w-ML-PM.parquet",
        "C:/dev/Air Partners/Data Analysis/data/east_boston/processed/sn49-final-w-ML-PM.parquet",
        "C:/dev/Air Partners/Data Analysis/data/east_boston/processed/sn62-final-w-ML-PM.parquet",
        "C:/dev/Air Partners/Data Analysis/data/east_boston/processed/sn67-final-w-ML-PM.parquet",
        "C:/dev/Air Partners/Data Analysis/data/east_boston/processed/sn72-final-w-ML-PM.parquet",
    ]

    stats_file = "C:/dev/Air Partners/Data Analysis/data/east_boston/stats/east_boston_summary_stats.parquet"

    flight_csv_dir = "C:/dev/Air Partners/Data Analysis/data/flights/raw/"

    processed_flight_dir = "C:/dev/Air Partners/Data Analysis/data/flights/processed/"

    final_flights = "C:/dev/Air Partners/Data Analysis/data/flights/final/combined_flights.parquet"

elif user_profile == "zxiong":
    raw_csv_paths = [
        'C:/Users/zxiong/Desktop/Olin/Air Partners/Code/sn45-final-w-ML-PM.csv',
        'C:/Users/zxiong/Desktop/Olin/Air Partners/Code/sn46-final-w-ML-PM.csv',
        'C:/Users/zxiong/Desktop/Olin/Air Partners/Code/sn49-final-w-ML-PM.csv',
        'C:/Users/zxiong/Desktop/Olin/Air Partners/Code/sn62-final-w-ML-PM.csv',
        'C:/Users/zxiong/Desktop/Olin/Air Partners/Code/sn67-final-w-ML-PM.csv',
        'C:/Users/zxiong/Desktop/Olin/Air Partners/Code/sn72-final-w-ML-PM.csv'
    ]

    processed_csv_paths = [
        "C:/Users/zxiong/Desktop/Olin/Air Partners/downsampled/sn45-final-w-ML-PM.parquet",
        "C:/Users/zxiong/Desktop/Olin/Air Partners/downsampled/sn46-final-w-ML-PM.parquet",
        "C:/Users/zxiong/Desktop/Olin/Air Partners/downsampled/sn49-final-w-ML-PM.parquet",
        "C:/Users/zxiong/Desktop/Olin/Air Partners/downsampled/sn62-final-w-ML-PM.parquet",
        "C:/Users/zxiong/Desktop/Olin/Air Partners/downsampled/sn67-final-w-ML-PM.parquet",
        "C:/Users/zxiong/Desktop/Olin/Air Partners/downsampled/sn72-final-w-ML-PM.parquet",
    ]

    stats_file = "C:/Users/zxiong/Desktop/Olin/Air Partners/Code/stats.parquet"

    flight_csv_dir = "C:/Users/zxiong/Desktop/Olin/Air Partners/flight data/raw"

    processed_flight_dir = "C:/Users/zxiong/Desktop/Olin/Air Partners/flight data/intermediate files"

    final_flights = "C:/Users/zxiong/Desktop/Olin/Air Partners/flight data/final files/final_flights.parquet"

else: # if not Ian or Lauren, feel free to make a copy of this and change the file names below:
    raw_csv_paths = [
        "./src/data_tool/data/east-boston/raw/sn45-final-w-ML-PM.csv",
        "./src/data_tool/data/east-boston/raw/sn46-final-w-ML-PM.csv",
        "./src/data_tool/data/east-boston/raw/sn49-final-w-ML-PM.csv",
        "./src/data_tool/data/east-boston/raw/sn62-final-w-ML-PM.csv",
        "./src/data_tool/data/east-boston/raw/sn67-final-w-ML-PM.csv",
        "./src/data_tool/data/east-boston/raw/sn72-final-w-ML-PM.csv",
    ]

    processed_csv_paths = [
        "./src/data_tool/data/east-boston/processed/sn45-final-w-ML-PM.parquet",
        "./src/data_tool/data/east-boston/processed/sn46-final-w-ML-PM.parquet",
        "./src/data_tool/data/east-boston/processed/sn49-final-w-ML-PM.parquet",
        "./src/data_tool/data/east-boston/processed/sn62-final-w-ML-PM.parquet",
        "./src/data_tool/data/east-boston/processed/sn67-final-w-ML-PM.parquet",
        "./src/data_tool/data/east-boston/processed/sn72-final-w-ML-PM.parquet",
    ]
    
    stats_file = "./src/data_tool/data/stats.parquet"

    flight_csv_dir =       "./src/data_tool/data/flights/raw/"
    processed_flight_dir = "./src/data_tool/data/flights/processed/"
    final_flights =        "./src/data_tool/data/flights/final/combined_flights.parquet"