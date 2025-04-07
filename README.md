# Uncertainty-Aware AI Agent

A Python application that demonstrates an AI agent with explicit uncertainty awareness and confidence evaluation in its reasoning process.

## Overview

This project implements an uncertainty-aware reasoning agent using the Agno framework. The agent is designed to:

- Explicitly evaluate confidence for each reasoning step
- Respond with "I don't know" when uncertainty exists in the final answer
- Never guess or provide adjacent/similar answers
- Flag ambiguous terms or unclear requirements

## Features

- 🤔 Explicit confidence evaluation for each reasoning step
- ❌ "I don't know" responses when uncertainty exists
- 🎯 Never guesses or provides adjacent/similar answers
- ⚠️ Flags ambiguous terms or unclear requirements
- 🔄 Multiple LLM model support
- 📝 Question history tracking
- 🔒 Secure API key management
- 💻 Both CLI and GUI interfaces available

#Output
1. CLI
   ![1743143954376](https://github.com/user-attachments/assets/f6bb54c0-9535-4857-92e3-d9ef1c76c2f1)

2. GUI
![Screenshot 2025-04-07 at 3 48 29 PM](https://github.com/user-attachments/assets/6f6e8c99-185c-40ac-b038-ac4b1a9e0c6d)



## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/uncertainty-aware-ai.git
cd uncertainty-aware-ai
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Command Line Interface (CLI)

Run the CLI version to process a set of predefined questions:
```bash
python uncertainty_agent.py
```

The CLI version will:
- Process predefined security-related questions
- Show full reasoning process for each question
- Display confidence assessments and final answers
- Stream responses in real-time

### Graphical User Interface (GUI)

Run the Streamlit web interface for interactive usage:
```bash
streamlit run ui.py
```

The GUI version offers:
1. Interactive web interface (typically at http://localhost:8501)
2. API key configuration in the sidebar
3. Multiple LLM model selection
4. Custom question input
5. Example questions to try
6. Question history tracking
7. Visual display of the thinking process

## How It Works

The agent follows a structured reasoning process:

1. **Question Analysis**: Understanding what is being asked
2. **Knowledge Verification**: Verifying available knowledge
3. **Confidence Assessment**: Evaluating confidence in the answer
4. **Final Answer Decision**: Providing the final response


