# Booksy Rating Fetcher

### Rating fetcher for Booksy profiles

This script fetches the HTML content from a profile on Booksy, parses it to extract the average rating and total reviews count, and saves this data along with the current date and time to a JSON file.

## Requirements
- GNU/Linux or macOS (not tested on Windows)
- Python 3.x
- pip

## Installation steps

1. Go to the project's root directory.

    **`cd /path/to/booksy-rating-fetcher`**

2. Create and activate Python virtual environment.

    **`python -m venv . && chmod +x ./bin/activate && ./bin/activate`**

3. Install required libraries.

    **`pip install -r requirements.txt`**

4. Create a text file `url.txt` containing the URL of the Booksy profile from which you want to fetch the rating. It must be in the project's root directory.
    
    *Example:*

    **`echo https://booksy.com/en-us/dl/show-business/12345 > url.txt`**

## Running the script

- Saves the rating file to the default path (`./rating.json`):

  **`python rating-fetcher.py`**

- Saves the rating file to a custom path:

  **`python rating-fetcher.py /path/to/rating.json`**
