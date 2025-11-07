from crewai.tools import BaseTool
from crewai_tools import ScrapeWebsiteTool
# Scraper
class ScraperTool(BaseTool):
    name: str = "scrape_website"
    description: str = "Scrape a website and return its content"

    def _run(self, url: str):
        return ScrapeWebsiteTool().run(url)

    def _arun(self, url: str):
        raise NotImplementedError()