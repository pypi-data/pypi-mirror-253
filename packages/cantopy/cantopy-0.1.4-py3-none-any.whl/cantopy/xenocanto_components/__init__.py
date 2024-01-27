# To expose the Query, QueryResult, Recording and ResultPage classes to the user,
# # we need to make it clear that we want to expose it to the user. We do this by
# importing it here and then re-exporting it in the __init__.py file.
# See: https://github.com/microsoft/pylance-release/issues/2953
from cantopy.xenocanto_components.query import Query as Query  # type: ignore
from cantopy.xenocanto_components.query_result import QueryResult as QueryResult  # type: ignore
from cantopy.xenocanto_components.recording import Recording as Recording  # type: ignore
from cantopy.xenocanto_components.result_page import ResultPage as ResultPage  # type: ignore
