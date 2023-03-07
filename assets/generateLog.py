from assets.pdfFetcher import parsePdfText
from assets.checkMasking import maskedChecker


def generateLog(policies):
    # log
    log = []

    # generating log
    for policy in policies:
        response = dict()
        response['policy_id'] = policy['policy_id']
        response['document'] = policy['pdf']
        if (policy['pdf'] != None):
            # Extract text from pdf
            Input_Text = parsePdfText(policy['pdf'])

            # Check for Engine no. and Chassis No. Masking
            isMasked = maskedChecker(Input_Text)
            response['masked_status'] = isMasked
        log.append(response)

    return log
