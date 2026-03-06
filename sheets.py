import gspread, json
from suite import Suite
from oauth2client.service_account import ServiceAccountCredentials

with open("sheet.json", "r", encoding="utf-8") as archive:
    config = json.load(archive)

sheet_id = config["id"]

def execute():
    """
    Update the status column of NUP processes in a Google Sheets document.

    This function connects to Google Sheets using a Service Account,
    retrieves all NUP values from column F (starting at row 7), sends each
    NUP to the Suite API using the Suite class, and writes the returned
    status and date into column L of the same row.

    Workflow:
        1. Authenticate with Google Sheets API
        2. Open the spreadsheet using its ID
        3. Retrieve NUP values from column F
        4. For each NUP:
            - Call Suite.post_nup()
            - Collect the returned status
        5. Update column L with the results using batch_update()

    Args:
        None

    Returns:
        None

    Example:
        >>> from sheets import execute
        >>> execute()

    Notes:
        - NUP values must be located in column F starting from row 7.
        - Status results will be written to column L.
        - Updates are sent in batch to reduce Google Sheets API requests.
    """
    # Path of credentials json(created with account service Google API)
    filename= "nupatualizador-489415-61ab381a3769.json"

    # Default config of Google API scopes
    scopes = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    # Default config of credentials Google API
    creds = ServiceAccountCredentials.from_json_keyfile_name(filename=filename, 
                                                            scopes=scopes
                                                            )

    # Utilize the credentials to auth bot
    client = gspread.authorize(creds)

    # Find the Worksheet by id of Google Sheets
    worksheet = client.open_by_key(sheet_id)

    # Get the first page of worksheet
    sheet = worksheet.get_worksheet(0)

    # In your sheet, get the column of NUP's
    nups = sheet.get("F7:F")

    # Suite Class atributted to suite
    suite = Suite()

    updates = []

    # That Loop get the number of Row, NUP of NUP-Column, call the function "post_nup" of Suite Class and update Cell of L Column with return
    for i, row in enumerate(nups, start=7):

        if not row:
            continue

        nup = row[0]

        result = suite.post_nup(nup)

        updates.append({
            "range": f"L{i}",
            "values": [[result]]
        })

    if updates:
        sheet.batch_update(updates)