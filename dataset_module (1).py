# dataset_module.py

def load_dataset(file_path):
    """
    Loads a CSV file into a nested dictionary using only file object methods.
    The first column (ID) is used as the key for each patient record.

    Args:
        file_path (str): Path to the dataset CSV file.

    Returns:
        dict: Nested dictionary where each key is a patient ID and value is a dictionary of features.
    """
    dataset = {}

    try:
        with open(file_path, 'r') as file:
            # Read the header
            header_line = file.readline().strip()
            headers = header_line.split(',')

            # Read each data row
            for line in file:
                line = line.strip()
                if not line:
                    continue  # skip empty lines
                values = line.split(',')

                # Ensure the row is valid
                if len(values) != len(headers):
                    continue  # skip malformed rows

                record_id = values[0].strip()
                features = {}

                for i in range(1, len(headers)):
                    features[headers[i].strip()] = values[i].strip()

                dataset[record_id] = features

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred while loading the dataset: {e}")

    return dataset
