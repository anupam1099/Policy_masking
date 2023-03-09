# Policy Pdf Engine & Chassis Number Mask Checker

## Objective

- For each policy with intermediary_id : 205
- Interact with DB to get pdf file link.
- Extract text from pdf.
- use regex pattern to check if the engine No, chassis No, User Mobile & User Email is masked or not.
- If NO trigger a mail to given recipients with details.

## Libraries Used

- re (regex)
- psycopg2 (db query)
- io, requests (web pdf fetch)
- pdfMiner (pdf text extract)
