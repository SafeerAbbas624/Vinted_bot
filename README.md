# Vinted_bot

This script is designed to automate the process of uploading and listing products on the Vinted marketplace. It uses the Selenium library to interact with the Vinted website and upload product images, enter product details, and set product categories, brands, and prices. The script also reads product information from text files in a specified directory, making it easy to add multiple products in one go.

## Features
- Automates the process of uploading and listing products on Vinted
- Reads product information from text files, reducing manual data entry
- Supports multiple product categories, brands, and prices
- Can handle different product sizes (formats)

## Installation
To use this script, you need to have Python and the following libraries installed:

- Selenium
- Undetected ChromeDriver
- Pyperclip

You can install these libraries using pip:

```bash
pip install selenium undetected-chromedriver pyperclip
```

You also need to download the ChromeDriver executable and place it in a directory that is accessible to the script. Make sure to use a version of ChromeDriver that matches your Chrome browser version.

## Usage
Place the script in a directory that contains subdirectories for each product. Each product subdirectory should contain the following:

- Product images (JPG format)
- A text file with the following information, one entry per line:
- Product title
- Product description (up to 15 lines)
- Category (e.g. “Divertissement/Jeux vidéo et consoles/Xbox Series X et S/Jeux”)
- Brand (e.g. “Shein”)
- Condition (e.g. “Neuf avec étiquette”)
- Price
- Format (e.g. “Petit”)
Edit the script to include your Vinted email address and password. Run the script. The script will open a Chrome browser, navigate to the Vinted website, and start uploading and listing products.

### Thanks Note
This script was created by Safeer Abbas. If you find this script useful, please consider giving it a star. If you have any questions or suggestions, please open an issue on GitHub or contact me directly.
