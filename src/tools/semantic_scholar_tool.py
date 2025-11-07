from crewai.tools import BaseTool
from langchain_community.tools.semanticscholar.tool import SemanticScholarQueryRun
# Semantic Scholar
class SemanticScholarTool(BaseTool):
    name: str = "semantic_scholar_search"
    description: str = "Search academic papers using Semantic Scholar"

    def _run(self, query: str):
        return SemanticScholarQueryRun().run(query)

    def _arun(self, query: str):
        raise NotImplementedError()