# imports
import json

# assets
from assets.dbQuery import policyList
from assets.documentList import extract_documents
from assets.generateLog import generateLog
from assets.utils import startExecution, stopExecution

# start driver code
startExecution()

# import data from DB
data = policyList()

# query unsuccessfull
if (data == None):
    stopExecution()

# extract all pdf links from data
pdfLinks = extract_documents(data, 'prod')

# log
log = generateLog(pdfLinks)

# log output
print(json.dumps(log, indent=4))

# end driver code
print("\n ----- Completed Successfully! ----- \n")
