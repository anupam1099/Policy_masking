import io
import requests
from pdfminer.high_level import extract_text


def parsePdfText(pdfURL):
    response = requests.get(pdfURL)
    rawText = extract_text(io.BytesIO(response.content))
    text = rawText.split("\n")
    text = [str for str in text if str != ""]
    return text
