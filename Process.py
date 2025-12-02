# #### Loading modules #### #
# pip3 install #
# sudo apt-get install python3-pip #

from pymongo import MongoClient
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# ###########Global Variables############
#server = 'localhost'
#port = '27017'
#username = ''
#password = ''
database = 'nvd'

def main():

    connection = MongoClient(f"mongodb://localhost:27017/{database}")

    db = connection[database]
    collection = ''
    file_name = input('Please enter filename: ')
    collection = db['cve_'+file_name.replace('.json', '')]
    cve_data = ''
    counter = 0

    with open(file_name, 'r', encoding='utf-8') as jsonfile: # Added encoding='utf-8' for safety
        cve_data = json.loads(jsonfile.read())

    # --- START OF UPDATED CODE ---

    # Loop through the list of vulnerabilities
    for item in cve_data['vulnerabilities']:
        
        # Use a try/except block for each CVE to avoid crashing the whole script
        try:
            temp_data = {}
            
            # Get the main 'cve' object for easier access
            cve_item = item['cve']

            # These paths are correct
            temp_data['cve'] = str(cve_item['id'])
            temp_data['description'] = str(cve_item['descriptions'][0]['value'])

            # --- Updated 'configurations' path ---
            # Now nested inside 'cve_item'
            try:
                # This gets the *first node* from the first configuration's node list
                temp_data['product'] = str(cve_item['configurations'][0]['nodes'][0])
            except (KeyError, IndexError, TypeError):
                temp_data['product'] = None # Use None or empty string if not found

            try:
                # This gets the full list of nodes from the first configuration
                temp_data['products'] = str(cve_item['configurations'][0]['nodes'])
            except (KeyError, IndexError, TypeError):
                temp_data['products'] = None

            # --- Updated 'references' path ---
            # 'references' is now a list directly under 'cve_item'.
            # The old 'reference_data' key is gone.
            try:
                # Storing the list of reference objects is better for Mongo
                temp_data['references'] = cve_item['references']
            except (KeyError, IndexError):
                temp_data['references'] = [] # Use an empty list if not found

            # --- Updated 'metrics' (score) path ---
            # The old 'impact' object is now 'cve_item.metrics'
            temp_data['score'] = None # Default to None
            try:
                # Try to get V3.1 score first
                # Note: 'cvssMetricV31' is a LIST, so we access its first item [0]
                temp_data['score'] = cve_item['metrics']['cvssMetricV31'][0]['cvssData']['baseScore']
            except (KeyError, IndexError, TypeError):
                # If V3.1 fails, try V2.0
                try:
                    # 'cvssMetricV2' is also a LIST
                    temp_data['score'] = cve_item['metrics']['cvssMetricV2'][0]['cvssData']['baseScore']
                except (KeyError, IndexError, TypeError):
                    pass # Keep score as None if V2 also fails

            # These fields are fine
            temp_data['vendor'] = []
            temp_data['application'] = []
            temp_data['os'] = []
            temp_data['hardware'] = []
            temp_data['sec_vendor'] = []
            temp_data['sec_application'] = []
            temp_data['sec_os'] = []
            temp_data['sec_hardware'] = []

            counter = counter + 1
            collection.insert_one(temp_data)
        
        except Exception as e:
            # Print an error if a specific CVE fails, then continue the loop
            print(f"Failed to process CVE: {item.get('cve', {}).get('id', 'UNKNOWN')}. Error: {e}")

    # --- END OF UPDATED CODE ---

    print("Total Records Entererd: ", counter )

if __name__ == '__main__':
    return_value = main()
