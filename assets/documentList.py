from assets.config import env


def extract_document(policyId, policy, ENV):
    response = dict()
    response['policy_id'] = policyId
    try:
        response['pdf'] = env[ENV]+policy['document']
    except:
        response['pdf'] = None
    return response


def extract_documents(data, ENV):
    documents = []
    for policy in data:
        documentLink = extract_document(policy[0], policy[2], ENV)
        documents.append(documentLink)
    return documents
