import os
import importlib
import argparse
from queue import Queue
import threading

# Function to process data through a filter and pass it to the next queue
def filter_worker(filter_name, input_queue, output_queue):
    try:
        filter_module = importlib.import_module(f"filters.{filter_name}")
        if hasattr(filter_module, filter_name):
            filter_function = getattr(filter_module, filter_name)
            while True:
                data = input_queue.get()
                if data is None:  # Sentinel value to stop the thread
                    output_queue.put(None)
                    break
                result = filter_function(data)
                output_queue.put(result)
                input_queue.task_done()
        else:
            raise AttributeError(f"The filter '{filter_name}' does not have a function named '{filter_name}'.")
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f"The filter module '{filter_name}' was not found in the 'filters' directory.")

def process_file(input_file):
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

    # Create a queue for each filter
    filter_queues = {filter_name: Queue() for filter_name in filter_names}
    filter_queues['first'] = Queue()
    # Put the initial data into the first queue
    filter_queues['first'].put(input_file)
    filter_queues['first'].put(None)  # Sentinel value to stop the first thread

    # Create threads for each filter that can be applied in parallel
    threads = []
    for i, filter_name in enumerate(filter_names[::]):
        input_queue = filter_queues[filter_names[i-1]] if i > 0 else filter_queues['first']
        output_queue = filter_queues[filter_names[i]]
        thread = threading.Thread(target=filter_worker, args=(filter_name, input_queue, output_queue))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Retrieve the final result from the last queue
    data = filter_queues[filter_names[-1]].get()
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