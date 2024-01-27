from typing import Dict, List, Tuple
import requests
import urllib.parse
from cantopy.xenocanto_components import Query, QueryResult, ResultPage


class FetchManager:
    """Class for managing the fetching of data from the Xeno Canto API.

    Attributes
    ----------
    base_url : str
        The base url pointing to the XenoCanto API endpoint.

    """

    def __init__(self) -> None:
        """Init the CantoPy instance"""
        self.base_url = "https://www.xeno-canto.org/api/2/recordings"

    def send_query(self, query: Query, max_pages: int = 1) -> QueryResult:
        """Send a query to the Xeno Canto API.

        Parameters
        ----------
        query : Query
            the query to send to the Xeno Canto API.
        max_pages : int, optional
            specify a maximum number of pages of recordings to fetch, by default 1.

        Returns
        -------
        QueryResult
            The QueryResult wrapper object containing the results of the query.
        """

        # We need to first send an initial query to determine the number of available result pages
        query_str = query.to_string()
        query_metadata, result_page_1 = self._fetch_result_page(query_str, page=1)

        result_pages: List[ResultPage] = []
        result_pages.append(result_page_1)

        # Fetch the other requested result pages
        for i in range(1, min(max_pages, int(query_metadata["available_num_pages"]))):
            result_pages.append(self._fetch_result_page(query_str, page=i + 1)[1])

        return QueryResult(query_metadata, result_pages)

    def _fetch_result_page(
        self, query_str: str, page: int
    ) -> Tuple[Dict[str, str | int], ResultPage]:
        """Fetch a specific page from the XenoCanto API.

        Parameters
        ----------
        query_str : str
            the query to send to the Xeno Canto API, printed in string format.
        page : int, optional
            The number id of the page we want to fetch.

        Returns
        -------
        Tuple[Dict[str, int], ResultPage]
            A tuple containing both a dictionary with query metadata (keys: "available_num_recordings",
            "available_num_species", "available_num_pages") and a ResultPage wrapper containing
            the requested page.
        """
        # Encode the http payload
        payload_str = urllib.parse.urlencode(
            {
                "query": query_str,
                "page": page,
            },
            safe=":+",
        )

        # Send request and open json return as dict
        query_response = requests.get(
            self.base_url,
            params=payload_str,
            timeout=5.0,
        ).json()

        # Extract the metadata information of this query
        query_metadata = {
            "available_num_recordings": int(query_response["numRecordings"]),
            "available_num_species": int(query_response["numSpecies"]),
            "available_num_pages": int(query_response["numPages"]),
        }

        return query_metadata, ResultPage(query_response)
