from typing import List, Dict
from cantopy.xenocanto_components.recording import Recording


class ResultPage:
    """Wrapper for storing a single page of results of a query to the Xeno Canto API.

    Attributes
    ----------
    page_id : int
        The page number of the results page that is being displayed.
    recordings : List[Recording]
        An array of recording objects containing detailed information about each recording.

    """

    def __init__(
        self, single_page_query_response: Dict[str, str | int | List[Dict[str, str]]]
    ):
        """Create a ResultPage object from the XenoCanto json response

        Parameters
        ----------
        single_page_query_response : Dict[str, Any]
            The query response from the XenoCanto API.

        Raises
        ------
        TypeError
            If the id of the page returned by the XenoCanto API could not be read as a string.
        TypeError
            If a recording returned by the XenoCanto API could not be read as a dict.
        """

        # Set the page id
        if isinstance(single_page_query_response["page"], int):
            self.page_id = single_page_query_response["page"]
        else:
            raise TypeError(
                f"Error creating a new ResultPage instance from the XenoCanto API response: \
                The page id returned by the XenoCanto API could not be read as a string: {single_page_query_response['page']}"
            )

        # Set the recordings
        self.recordings: List[Recording] = []

        if not isinstance(single_page_query_response["recordings"], list):
            raise TypeError(
                f"Error creating a new ResultPage instance from the XenoCanto API response: \
                The recordings returned by the XenoCanto API could not be read as a list: {single_page_query_response['recordings']}"
            )
        for query_response_recording in single_page_query_response["recordings"]:
            self.recordings.append(Recording(query_response_recording))
