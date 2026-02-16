# Vacation Planner

This project is an AI-powered travel planning system built using the crewAI framework. It leverages multiple specialized agents to research destinations and generate comprehensive travel reports.

## Overview

The system consists of two primary agents:
1.  **Vacation Researcher**: Conducts automated internet research to find unique facts and information about a specified destination.
2.  **Itinerary Planner**: Synthesizes research data into a structured travel report.

The project features a robust search tool with self-healing capabilities to ensure reliable data retrieval even when agent inputs are malformed.

## Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) for dependency management
- Serper API Key (for internet search functionality)
- AWS Bedrock access (configured for us-amazon-nova-pro-v1:0)

## Setup

1. Clone the repository.
2. Ensure `uv` is installed:
   ```bash
   pip install uv
   ```
3. Configure environment variables in a `.env` file:
   ```text
   SERPER_API_KEY=your_serper_api_key
   AWS_REGION_NAME=your_aws_region
   ```
4. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

To run the vacation planner, execute the following command:

```bash
uv run run_crew
```

The destination can be modified in `src/vacation_planner/main.py`. The final report will be generated as `report.md` in the root directory.

## Project Structure

- `src/vacation_planner/crew.py`: Core logic for agents, tools, and tasks.
- `src/vacation_planner/main.py`: Entry point for running the crew.
- `src/vacation_planner/config/agents.yaml`: Configuration for agent roles and goals.
- `src/vacation_planner/config/tasks.yaml`: Definition of tasks and expected outputs.
- `streamlitui.py`: Optional Streamlit interface for the application.
