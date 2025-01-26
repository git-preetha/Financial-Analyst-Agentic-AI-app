from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi.api
from dotenv import load_dotenv
import os
import phi
from phi.playground import Playground,serve_playground_app
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include source"],
    show_tool_calls=True,
    markdown=True,
)

## Financial agent
finance_agent=Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Web Search Agent handles news queries","Finance Agent handles financial data queries",
        "Provide a clear summary along with the sources"],
    show_tool_calls=True,
    markdown=True
)

app=Playground(agents=[multi_ai_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)