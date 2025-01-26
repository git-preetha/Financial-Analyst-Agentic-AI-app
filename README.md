# Financial-Analyst-Agentic-AI-app

A multi-agent system developed with the Phi framework to analyze financial data and conduct web searches. This project utilizes AI-driven tools to deliver structured insights, including stock recommendations, company news, and real-time web data, empowering informed decision-making. The system operates in a multimodal environment, combining data from both structured financial sources and unstructured web data.

The project is integrated with PhiData Playground, which enables testing and interaction with these agents in a web-based environment for seamless exploration and experimentation.

## Features

- 🌐 **Web Search Agent** - Uses DuckDuckGo to search the web for reliable information, including the latest news and general queries.
- 📊 **Finance Agent** - Fetches stock prices, analyst recommendations, company news, and financial data using YFinanceTools.
- 🤝 **Multi-Agent Collaboration** - Combines specialized agents to collaboratively handle complex queries for comprehensive insights.
- ⏱️ **Real-Time Responses** - Provides streamed responses for interactive and seamless communication.
- 📋 **Structured Outputs** - Delivers well-organized summaries, tables, and sources for transparency and better decision-making.
- 🧑‍💻 **PhiData Playground Integration** - The system can be tested and used interactively in the PhiData Playground, allowing you to test agent responses, perform real-time queries, and visualize structured data outputs.

## Technologies Used

- Phi Framework: For building and managing AI agents.
- Groq AI Models: Powers natural language understanding and tool usage.
- YFinanceTools: Retrieves financial data and market insights.
- DuckDuckGo API: For web-based information retrieval.
- Python: Core programming language for implementation.
- PhiData Playground: A web interface to interact with the agents and view results in real-time.

## Project Workflow

1. **Agent Setup**: The system includes two agents: a Web Search Agent and a Finance Agent. Each agent is assigned specific tasks like searching the web for news or retrieving financial data. The Web Search Agent utilizes the DuckDuckGo API to fetch relevant web-based information. The Finance Agent uses the YFinanceTools to gather data like stock prices, analyst recommendations, and company news.
2. **Agent Collaboration**: The Multi-Agent System allows these agents to collaborate on more complex queries. For example, an inquiry for a stock’s analysis could involve fetching analyst recommendations from the Finance Agent and current news from the Web Search Agent.
3. **Real-Time Data Retrieval**: Both agents use their respective APIs to fetch real-time data. The Web Search Agent looks up up-to-date news and articles, while the Finance Agent retrieves the latest stock data.
4. **Structured Outputs**: The data retrieved by the agents is presented as structured outputs, such as tables, summaries, and reports, that can be directly used for decision-making.
5. **PhiData Playground**: The system integrates with PhiData Playground, which allows you to interact with the agents, send queries, and receive live responses. It provides an interactive interface for testing and using the system without requiring local setup.

### Prerequisites
- Python 3.10+
- API key for [Phi](https://www.phidata.com/)
- API key for [Groq](https://groq.com/)

### Create a virtual environment
`conda create -p venv python==3.12`

`conda activate venv`

### Install dependencies
`pip install -r requirements.txt`

### Set up environment variables in a .env file
`PHI_API_KEY="your_phi_api_key"`

`GROQ_API_KEY="your_groq_api_key"`

### Usage
- Run the main script
  `python financial_agent.py`

- Using the PhiData Playground
  1. Run the playground.py script using `python playground.py`
  2. Go to [PhiData Playground](https://www.phidata.app/playground/chat)
  3. Choose endpoint as localhost:7777
  4. Type your queries




