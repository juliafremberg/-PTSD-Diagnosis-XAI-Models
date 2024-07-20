import pandas as pd

def filter_and_group_csv_by_tid(input_file, output_file, tid_column='tid', max_unique_tids=44):
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Get the unique 'tids' up to the maximum number specified
        unique_tids = df[tid_column].unique()[:max_unique_tids]
        
        # Filter the dataframe to include only the rows with the selected 'tids'
        filtered_df = df[df[tid_column].isin(unique_tids)]
        
        # Group by 'tid' and calculate the mean of all other columns
        grouped_df = filtered_df.groupby(tid_column).mean()
        
        # Save the grouped dataframe to a new CSV file
        grouped_df.to_csv(output_file)
        
        print(f"Data has been successfully filtered and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Provide the full path to the input file
    input_file = '/Users/juliafremberg/Desktop/urop project/synthetic data collection/ann.pp_control_data_M_18_24.csv'
    output_file = '/Users/juliafremberg/Desktop/urop project/synthetic data collection/grouped_data_c_1.csv'
    filter_and_group_csv_by_tid(input_file, output_file)

if __name__ == "__main__":
    main()
