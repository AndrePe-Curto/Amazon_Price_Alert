# Amazon Price Alert

## Overview

This Python script tracks the price of a specified product on Amazon and logs the price data to a CSV file. It uses a retry mechanism with a random user agent to bypass potential captchas and avoid bot detection. Additionally, it is designed to send an email notification when the price drops below a specified threshold (although this feature is currently commented out).

## Features

- Fetches the product title and price from an Amazon product page.
- Logs the product title, price, and date to a CSV file.
- Uses a retry mechanism with random user agents to bypass bot detection.
- Email notification functionality.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `fake_useragent`

You can install the required packages using:

```sh
pip install requests beautifulsoup4 fake_useragent
 ```
# Usage

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/amazon-price-tracker.git
    cd amazon-price-tracker
    ```

2. **Edit the script:**

    - Update the `URL` variable with the URL of the Amazon product you want to track.
    - Uncomment and update the email credentials in the `send_mail` function if you wish to use the email notification feature.

3. **Run the script:**

    ```sh
    python amazon_price_tracker.py
    ```

    The script will fetch the product title and price, log them to `AmazonWeb.csv`, and sleep for 24 hours before repeating the process.

## CSV Output

The script generates a CSV file named `AmazonPrice.csv` in the following format:

| Title          | Price | Date             |
|----------------|-------|------------------|
| Product Title  | 999.99| 21/06/2024 12:00 |

## Email Notification

To enable email notifications:

1. Uncomment the `send_mail` function and its call within the loop.
2. Update the email sender credentials (`your_email@gmail.com`, `your_password`) and the recipient email (`recipient@gmail.com`).
3. Follow the instructions to enable app passwords if using Gmail.


## Troubleshooting

- If you encounter captcha issues, the script will retry with a new user agent.
- Ensure that you have the correct permissions to send emails via SMTP if enabling the email notification feature.

## Acknowledgments

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing.
- [Fake UserAgent](https://pypi.org/project/fake-useragent/) for generating random user agents.


## Contact

For any questions or issues, please open an issue on the GitHub repository 
