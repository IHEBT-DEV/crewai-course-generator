from crewai.tools import BaseTool
from langchain_community.tools import  ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper

# Arxiv
class ArxivTool(BaseTool):
    name: str = "arxiv_search"
    description: str = "Search academic papers using Arxiv"

    def _run(self, query: str):
        wrapper = ArxivAPIWrapper(top_k_results=10, doc_content_chars_max=200000)
        return ArxivQueryRun(api_wrapper=wrapper).run(query)

    def _arun(self, query: str):
        raise NotImplementedError()