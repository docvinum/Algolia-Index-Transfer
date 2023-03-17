import os
import algoliasearch

# Initialize Algolia client
ALGOLIA_APP_ID = os.getenv("ALGOLIA_APP_ID")
ALGOLIA_API_KEY = os.getenv("ALGOLIA_API_KEY")
client = algoliasearch.Client(ALGOLIA_APP_ID, ALGOLIA_API_KEY)

# Define source and destination indices
source_index = client.init_index(os.getenv("ALGOLIA_SOURCE_INDEX"))
destination_index = client.init_index(os.getenv("ALGOLIA_DESTINATION_INDEX"))

# Browse all records from source index and push to destination index
records = source_index.browse_all()
destination_index.save_objects(records, {"autoGenerateObjectIDIfNotExist": True})
