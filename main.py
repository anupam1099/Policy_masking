# imports
import sys
import json

# assets
from assets.config import dbConfig, intermediaryId, limit
from assets.dbQuery import policyList
from assets.documentList import extract_documents
from assets.generateLog import generateLog

# start driver code
print("\n ----- Policy Pdf Engine & Chassis Number Mask Checker Started -----\n")

# import data from DB
data = policyList(dbConfig, intermediaryId, limit)

# query unsuccessfull
if (data == None):
    print("Exiting...")
    sys.exit(0)

# extract all pdf links from data
pdfLinks = extract_documents(data, 'prod')

# log
log = generateLog(pdfLinks)

# log output
print(json.dumps(log, indent=4))

# end driver code
print("\n ----- Completed Successfully! ----- \n")
