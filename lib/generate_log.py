from datetime import datetime
import os
import requests

def generate_log(data):
    # TODO: Implement log generation logic
    
    if not isinstance(data, list):
        raise ValueError("Invalid input: log_data must be a list.")
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"
    
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    print(f"Log successfully written to {filename}")
    
    return filename
    
    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename

    pass

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    post = fetch_data()
    data = post.get("title", "No title found")
    print("Fetched Post Title:",data )
    displayed_data = [
        "User updated",
        "Data with title",
        f"{data} has been created."
    ]
    generate_log(displayed_data)