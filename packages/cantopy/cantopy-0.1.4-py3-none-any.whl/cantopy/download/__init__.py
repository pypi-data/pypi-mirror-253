# To expose the DownloadManager class to the user, we need to make it clear that
# we want to expose it to the user. We do this by importing it here and then
# re-exporting it in the __init__.py file.
# See: https://github.com/microsoft/pylance-release/issues/2953
from cantopy.download.download_manager import DownloadManager as DownloadManager # type: ignore