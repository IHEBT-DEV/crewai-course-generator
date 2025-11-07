from crewai.tools import BaseTool
from langchain_community.tools import  DuckDuckGoSearchRun

# DuckDuckGo
class DuckDuckGoTool(BaseTool):
    name: str = "duckduckgo_search"
    description: str = "Search the web using DuckDuckGo"

    def _run(self, query: str):
        return DuckDuckGoSearchRun().run(query)

    def _arun(self, query: str):
        raise NotImplementedError()