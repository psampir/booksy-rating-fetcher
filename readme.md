# abacosun-rating-fetcher

### Rating fetcher for the Abacosun Ostrów Wielkopolski website

This script fetches the HTML content from the Abacosun Ostrów Wielkopolski profile on Booksy, parses it to extract the average rating and total reviews count, and saves this data along with the current date and time to a JSON file.

## Requirements
- GNU/Linux or macOS (not tested on Windows)
- Python 3.x
- pip

## Installation steps

1. Go to the project's root directory:

    **`cd /path/to/abacosun-rating-fetcher`**

2. Create and activate Python virtual environment:

    **`python -m venv . && chmod +x ./bin/activate && ./bin/activate`**

3. Install required libraries:

    **`pip install -r requirements.txt`**

## Running the script

- Saves the rating file to the default path (`./rating.json`):

  **`python rating-fetcher.py`**

- Saves the rating file to a custom path:

  **`python rating-fetcher.py /path/to/rating.json`**
