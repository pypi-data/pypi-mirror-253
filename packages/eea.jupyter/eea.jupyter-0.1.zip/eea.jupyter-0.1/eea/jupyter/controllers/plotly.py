import IPython
import requests
from urllib.parse import urlparse


class PlotlyController:
    """
    A class that represents a Plotly controller.

    Attributes:
      url (str): The URL of the plotly visualization to be added or edited.

    Methods:
      __init__(self, url): Initializes a new instance of the PlotlyController class.
      uploadPlotly(self, chart_data, metadata): Uploads Plotly chart data.
    """

    def __init__(self, url):
        self.url_tuple = urlparse(url)
        self.host = self.url_tuple.scheme + "://" + self.url_tuple.netloc
        self.path = self.__sanitizePath(self.url_tuple.path)
        self.path_parts = self.path.split('/')

    def __sanitizePath(self, path):
        return path.replace("/edit", "").replace("/add", "").rstrip('/')

    def uploadPlotly(self, chart_data, metadata):
        parent_path = self.path_parts[:-1]
        parent_status = requests.get(
            self.host + '/'.join(parent_path)).status_code

        if parent_status == 404:
            print(
                "The path %s does not exist! Please try again." %
                ('/'.join(parent_path)))
            return
        else:
            url = self.host

            status = requests.get(self.host + self.path).status_code

            if status in [200, 401, 403]:
                url += self.path + '/edit'
            else:
                url += '/'.join(parent_path) + '/add?type=visualization'

            html = '<div><script>({})()</script><iframe name="jupyter" src="{}" width="100%" height="1080""/></div>'.format(
                self.__getOnLoadHandlerJS(chart_data, metadata), url)
        return IPython.display.HTML(html)

    def __getOnLoadHandlerJS(self, chart_data, metadata={}):
        metadata["id"] = self.path_parts[-1]
        return open('./eea/jupyter/controllers/scripts/plotly.js', 'r').read() % ({
            "host": self.host
        }, {
            "type": 'jupyter-ch:setContent',
            "content": {
                **metadata,
                "visualization": {
                    "chartData": chart_data
                }
            }
        })