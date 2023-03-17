import os
import logging
import traceback
import algoliasearch

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    # Initialize Algolia client
    ALGOLIA_APP_ID = os.getenv("ALGOLIA_APP_ID")
    ALGOLIA_API_KEY = os.getenv("ALGOLIA_API_KEY")
    client = algoliasearch.Client(ALGOLIA_APP_ID, ALGOLIA_API_KEY)

    # Define source and destination indices
    source_index_name = os.getenv("ALGOLIA_SOURCE_INDEX")
    destination_index_name = os.getenv("ALGOLIA_DESTINATION_INDEX")
    source_index = client.init_index(source_index_name)
    destination_index = client.init_index(destination_index_name)

    # Browse all records from source index and push to destination index
    records = source_index.browse_all()
    destination_index.save_objects(records, {"autoGenerateObjectIDIfNotExist": True})

    logging.info(f"Data transfer from {source_index_name} to {destination_index_name} completed successfully.")

except Exception as e:
    logging.error(f"An error occurred during the data transfer: {e}")
    logging.error(traceback.format_exc())
