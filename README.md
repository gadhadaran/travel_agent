# Multi-Agent Travel Itinerary System

## Overview
This project is a multi-agent system that automates travel planning using LangChain and SerpAPI. It consists of four specialized agents that collaborate to create a detailed multi-page travel itinerary, including flights, hotels, itinerary planning, and expense tracking.

## Features
- **Flight Agent**: Searches for flights based on user input.
- **Hotel Agent**: Finds hotels in the destination city for specified dates.
- **Itinerary Agent**: Plans a detailed daily itinerary.
- **Accounts Agent**: Tracks expenses and maintains budget constraints.

## Tech Stack
- **Programming Language**: Python
- **Frameworks/Libraries**:
  - LangChain
  - OpenAI GPT (or alternative LLMs like Google Gemini via OpenRouter)
  - SerpAPI (for search queries)
- **Dependencies**:
  - `langchain`
  - `openai`
  - `serpapi`

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/multi-agent-travel.git
   cd multi-agent-travel
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up API keys in a `.env` file:
   ```sh
   OPENAI_API_KEY=your_openai_key
   SERPAPI_API_KEY=your_serpapi_key
   ```

## Usage
Run the main script to generate a travel itinerary:
```sh
python main.py
```

## Configuration
Modify `main.py` to change destination, dates, and budget preferences:
```python
trip_destination = "Paris"
trip_days = 5
trip_date = "2025-06-10"
checkin_date = "2025-06-10"
checkout_date = "2025-06-15"
expenses = [500, 200, 150]
```

## Troubleshooting
- **Model Not Found Error (404)**:
  - Ensure you have access to `gpt-4`. If unavailable, use `gpt-3.5-turbo`.
  - Check your API key and billing status.
  - Use alternative providers like OpenRouter or Google Gemini.
- **Invalid API Key**:
  - Double-check your `.env` file and API credentials.

## Future Improvements
- Add support for more LLM providers.
- Implement a UI for user-friendly travel customization.
- Enhance itinerary personalization with user preferences.

## License
This project is open-source under the MIT License.

## Contact
For any issues or suggestions, feel free to open an issue or contact `darangadha@gmail.com`.

