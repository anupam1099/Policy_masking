from assets.constants import env


def extract_document(policyId, policy, ENV):
    document = dict()
    document['policy_id'] = policyId
    try:
        document['pdf'] = env[ENV]+policy['document']
    except:
        document['pdf'] = None
    return document


def extract_documents(data, ENV):
    documents = []
    for policy in data:
        documentLink = extract_document(policy[0], policy[2], ENV)
        documents.append(documentLink)
    return documents
