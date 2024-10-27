import json
import requests
import os
# Assuming 'request' is your request object
serialized_request = os.getenv('JSON')
# print(serialized_request)
# serialized_request = '{"protein_sequence": "SNPYQRGPNPTRSALTADGPFSVATYTVSRLSVSGFGGGVIYYPTGTSLTFGGIAMSPGYTADASSLAWLGRRLASHGFVVLVINTNSRFDYPDSRASQLSAALNYLRTSSPSAVRARLDANRLAVAGHSMGGGGTLRIAEQNPSLKAAVPLTPWHTDKTFNTSVPVLIVGAEADTVAPVSQHAIPFYQNLPSTTPKVYVELDNASHFAPNSNNAAISVYTISWMKLWVDNDTRYRQFLCNVNDPALSDFRTNNRHCQ","job_id": ""}'
# json.dumps(request)

# Define the URL of the REST API endpoint
url = ' http://host.docker.internal:5733/run-folding'

# Send the serialized request via POST
response = requests.post(url, data=serialized_request, headers={'Content-Type': 'application/json'})

# Print the response from the server
# print(response.status_code)
print(response.json())