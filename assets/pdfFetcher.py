import io
import requests
from pdfminer.high_level import extract_text
from assets.utils import printError, stopExecution


def scrapText(pdfURL):
    try:
        response = requests.get(pdfURL)
    except requests.RequestException as e:
        printError(e)
        stopExecution()
    try:
        rawText = extract_text(io.BytesIO(response.content))
    except:
        printError("PDFSyntaxError : Is this really a PDF?")
        stopExecution()
    return rawText.split("\n")


def parsePdfText(pdfURL):
    text = scrapText(pdfURL)
    text = [str for str in text if str != ""]
    return text
