import requests
from datetime import datetime

class Suite:

    #===========================================================================
    # *                           POST NUP
    #===========================================================================
    def post_nup(self, nup):
        """
        Find the last status and date of process NUP
        
        Args:
            nup (str): Unique Number Protocol of Process

        Returns:
            str: String formatted containing the simple status and date of last history of the process
            (in this format: "STATUS - DD-MM-YYYY")

        Example:
            >>> suite = Suite()
            >>> suite.post_nup("123456/2025")
            'SPS/SEXEC-PSO/CEART - 03-12-2025'
        """
        # Parameters for Request
        url = "https://suite.prod.papel-zero.suite.ce.gov.br/process/search/filters"
        payload = {"search":nup,"page":1,"order_by":{"date":"desc"},"paginator_count":5}
        headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json'}

        # Request config
        r = requests.post(url, json=payload, headers=headers)

        # Response to json
        data = r.json()

        # Get Last Status and Date of process
        history = data['results'][0]['history_search']
        first_history = history[0]

        # Get Status of NUP
        status = first_history['status']
        status = status.partition("(a) ")[2]

        # Get date and format for DD-MM-YYYY
        date = first_history['date']
        date = datetime.fromisoformat(date)
        date = date.strftime("%d-%m-%Y")

        # Returns status and date of process with formatation
        return f"{status} - {date}"