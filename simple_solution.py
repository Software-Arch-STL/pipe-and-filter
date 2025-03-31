import os
import importlib
import argparse

def process_file(file_name):
    # Ensure the filters directory exists
    filters_dir = os.path.join(os.path.dirname(__file__), 'filters')
    if not os.path.isdir(filters_dir):
        raise FileNotFoundError("The 'filters' directory does not exist.")

    # Define the order of filters
    filter_names = [
        "read_text",
        "remove_comments",
        "remove_duplicates",
        "count_frequency",
        "get_most_frequent_words"
    ]

    # Dynamically import and apply filters
    print(type(file_name))
    data = file_name
    for filter_name in filter_names:
        try:
            filter_module = importlib.import_module(f"filters.{filter_name}")
            if hasattr(filter_module, filter_name):
                filter_function = getattr(filter_module, filter_name)
                data = filter_function(data)
            else:
                raise AttributeError(f"The filter '{filter_name}' does not have a function named '{filter_name}'.")
        except ModuleNotFoundError:
            raise ModuleNotFoundError(f"The filter module '{filter_name}' was not found in the 'filters' directory.")
    
    return data

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process a file through a series of filters.")
    parser.add_argument("input_file", help="Path to the input file to be processed.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call process_file with the provided input file
    print(args)
    with open(args.input_file, 'r') as input_stream:
        print("Processing result:")
        result = process_file(input_stream)
        print(result)