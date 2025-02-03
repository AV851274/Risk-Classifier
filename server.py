import sys
import pandas as pd1

def process_csv(file_path):
    try:
        # Read the CSV file
        data = pd1.read_csv(file_path)
        
        # Perform some simple processing (e.g., sorting by a column or modifying values)
        print("Processing the CSV file...")
        sorted_data = data.sort_values(by=data.columns[0])  # Sort by the first column

        # Save the processed data to a new CSV file
        output_file = "processed_" + file_path.split("/")[-1]
        sorted_data.to_csv(output_file, index=False)
        print(f"CSV file processed and saved as: {output_file}")

    except Exception as e:
        print(f"Error processing the CSV file: {e}")

if __name__ == "__main__":
    # The first argument is the file path passed from Java
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
        process_csv(csv_file)
    else:
        print("No CSV file provided.")