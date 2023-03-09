from assets.pdfFetcher import parsePdfText
from assets.checkMasking import maskedChecker


def generateLog(policies):
    log = []
    for policy in policies:
        response = {
            "policy_id": policy['policy_id'], "document": policy['pdf']
        }
        if (policy['pdf'] != None):
            Input_Text = parsePdfText(policy['pdf'])
            isMasked = maskedChecker(Input_Text)
            response['masked_status'] = isMasked
        log.append(response)
    return log
