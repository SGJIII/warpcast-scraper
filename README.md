# Warpcast Scraper

The Warpcast Scraper is a web application built with Flask and Selenium that allows users to scrape the list of followers from a Warpcast user's profile and download it as a CSV file.

## Prerequisites

Before running the application, ensure you have the following installed on your local machine:

- Python 3.12 or higher
- Chrome WebDriver (for Selenium)

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/SGJIII/warpcast-scraper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd warpcast-scraper
    ```

3. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application Locally

1. Start the Flask development server by running the following command:

    ```bash
    python3.12 server.py
    ```

2. Open your web browser and go to `http://127.0.0.1:8080` to access the application.

## Usage

1. Once the application is running, you will see a form where you can enter a Warpcast username.
2. Enter the username of the Warpcast user whose followers you want to scrape.
3. Click the "Submit" button.
4. The application will scrape the list of followers from the user's profile and generate a CSV file.
5. Click the "Download Followers CSV" link to download the CSV file containing the scraped followers.

## Notes

- This application is currently in development and should not be used in a production environment.
- Use caution when scraping data from websites and ensure you comply with the website's terms of service and legal requirements.



