
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

    #connection = MongoClient(server,authSource=database)
    #OLD
    #connection = MongoClient("mongodb://remote_python:password@cluster0-shard-00-00.ja3ud.gcp.mongodb.net:27017,cluster0-shard-00-01.ja3ud.gcp.mongodb.net:27017,cluster0-shard-00-02.ja3ud.gcp.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-jgyvvk-shard-0&authSource=admin&retryWrites=true&w=majority")
    #NEW
    #connection = MongoClient("mongodb+srv://cve_python:password@cluster0.ja3ud.gcp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    #Localhost
    connection = MongoClient("mongodb://localhost:27017/<dbname>")


    db = connection[database]
    collection = ''
    file_name = input('Please enter filename: ')
    collection = db['cve_'+file_name.replace('.json', '')]
    cve_data = ''
    counter = 0

    with open(file_name, 'r') as jsonfile:
        cve_data = json.loads(jsonfile.read())

    for item in cve_data['CVE_Items']:
        if item['impact'] != {}:
          temp_data = {}
          temp_data['cve'] = str(item['cve']['CVE_data_meta']['ID'])
          temp_data['description'] = str(item['cve']['description']['description_data'][0]['value'])
#Code from Tyler Conrad for primary and secondary CPE information
          try:
               temp_data['product'] = str(item['configurations']['nodes'][0])
          except:
               pass

          temp_data['products'] = str(item['configurations']['nodes'])
#End new code
          temp_data['references'] = str(item['cve']['references']['reference_data'])

          if 'baseMetricV3' in item['impact']:
              temp_data['score'] = item['impact']['baseMetricV3']['cvssV3']['baseScore']
          else:
              temp_data['score'] = item['impact']['baseMetricV2']['cvssV2']['baseScore']

#Add in Main Platforms
          temp_data['vendor'] = []
          temp_data['application'] = []
          temp_data['os'] = []
          temp_data['hardware'] = []
#Add in Secondary Platforms
          temp_data['sec_vendor'] = []
          temp_data['sec_application'] = []
          temp_data['sec_os'] = []
          temp_data['sec_hardware'] = []

          counter = counter + 1
          collection.insert_one(temp_data)

    print("Total Records Entererd: ", counter );

if __name__ == '__main__':
    return_value = main()
