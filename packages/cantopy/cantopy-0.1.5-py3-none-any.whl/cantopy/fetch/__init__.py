# # To expose the FetchManager class to the user, we need to make it clear that
# we want to expose it to the user. We do this by importing it here and then
# re-exporting it in the __init__.py file.
# See: https://github.com/microsoft/pylance-release/issues/2953
from cantopy.fetch.fetch_manager import FetchManager as FetchManager # type: ignore