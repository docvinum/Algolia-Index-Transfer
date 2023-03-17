# Algolia Data Transfer
This is a Python script that transfers data between two Algolia Search indices. It uses the Algolia Search API and the algoliasearch Python package to retrieve records from a source index and push them to a destination index.

## Installation
To use this script, you will need to have Python 3.x and the algoliasearch package installed on your system. You can install the algoliasearch package using pip:

> pip install algoliasearch

## Configuration
Before running the script, you will need to set up the following environment variables:

> ALGOLIA_APP_ID: The Application ID of your Algolia account.
> ALGOLIA_API_KEY: The Write API Key of your Algolia account.
> ALGOLIA_SOURCE_INDEX: The name of the source index to transfer data from.
> ALGOLIA_DESTINATION_INDEX: The name of the destination index to transfer data to.
You can set these environment variables in your shell or in a .env file.

## Usage
To transfer data between the source and destination indices, simply run the script:

> python transfer_data.py

The script will retrieve all records from the source index and push them to the destination index. The records in the destination index will be overwritten if they have the same object ID as a record in the source index.

## Error Handling
The script is designed to handle errors that may occur during the data transfer. If an error occurs, the script will log an error message to the console and write a traceback to the log file.

## License
This script is released under the MIT License. Feel free to use, modify, and distribute it as you wish.

# Support
If you encounter any issues or have any questions about the script, feel free to open an issue on GitHub or contact me directly.

# Credits
This script was created by Alexandre Bast and is based on the Algolia Search API and the algoliasearch Python package.

I hope this helps you create a useful and informative README file for your project! Let me know if you have any other questions.