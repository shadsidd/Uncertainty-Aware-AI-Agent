import streamlit as st
import sys
import io
import contextlib
import os
from agno.models.openai import OpenAIChat
from agno.tools.thinking import ThinkingTools
from agno.agent import Agent

# Initialize session state
if 'agent_loaded' not in st.session_state:
    st.session_state.agent_loaded = False
if 'agent' not in st.session_state:
    st.session_state.agent = None
if 'selected_model' not in st.session_state:
    st.session_state.selected_model = "gpt-4o-mini"
if 'api_key' not in st.session_state:
    st.session_state.api_key = os.environ.get("OPENAI_API_KEY", "")

# Function to capture stdout
@contextlib.contextmanager
def capture_stdout():
    new_stdout = io.StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = new_stdout
        yield new_stdout
    finally:
        sys.stdout = old_stdout

st.set_page_config(
    page_title="Uncertainty-Aware AI Agent",
    page_icon="🤔",
    layout="wide"
)

st.title("Uncertainty-Aware AI Agent")
st.markdown("""
This agent explicitly evaluates confidence for each reasoning step and responds with "I don't know" when uncertainty exists.
""")

# Sample questions
sample_questions = [
    "Select a sample question...",
    "What is the exact CVE identifier for the Heartbleed vulnerability?",
    "What's the exact cryptographic algorithm used in Tesla's latest vehicle-to-infrastructure communication protocol?",
    "Who is currently the most dangerous ransomware group?",
    "What's the 'best' cybersecurity certification for everyone?"
]

# Sidebar with information
with st.sidebar:
    st.header("About")
    st.markdown("""
    This agent follows these rules:
    - Explicitly evaluates confidence for each reasoning step
    - Responds with "I don't know" when uncertainty exists
    - Never guesses or provides adjacent/similar answers
    - Flags ambiguous terms or unclear requirements
    """)
    
    # API Key input
    st.header("API Configuration")
    api_key = st.text_input(
        "OpenAI API Key:",
        value=st.session_state.api_key,
        type="password",
        help="Enter your OpenAI API key. This will be used for all API calls."
    )
    
    # Update API key in session state
    if api_key != st.session_state.api_key:
        st.session_state.api_key = api_key
        st.session_state.agent_loaded = False  # Reset agent when API key changes
    
    # LLM selection
    st.header("Model Selection")
    available_models = {
        "GPT-4o Mini": "gpt-4o-mini",
        "GPT-4o": "gpt-4o",
        "GPT-4": "gpt-4",
        "GPT-3.5 Turbo": "gpt-3.5-turbo"
    }
    
    selected_model_name = st.selectbox(
        "Select Language Model:",
        options=list(available_models.keys()),
        index=list(available_models.keys()).index("GPT-4o Mini")
    )
    
    # Update the selected model in session state
    st.session_state.selected_model = available_models[selected_model_name]
    
    # Reset agent when model changes
    if 'previous_model' not in st.session_state:
        st.session_state.previous_model = st.session_state.selected_model
    elif st.session_state.previous_model != st.session_state.selected_model:
        st.session_state.agent_loaded = False
        st.session_state.previous_model = st.session_state.selected_model

# Main content area
st.header("Ask a Question")

# Dropdown for sample questions
selected_sample = st.selectbox("Choose a sample question:", sample_questions)

# Text area for custom question
user_question = st.text_area("Or enter your own question:", height=100)

# Determine which question to use
question_to_ask = user_question if user_question else (selected_sample if selected_sample != sample_questions[0] else "")

if st.button("Ask the Agent"):
    if question_to_ask:
        # Check if API key is provided
        if not st.session_state.api_key:
            st.error("Please enter your OpenAI API key in the sidebar.")
        else:
            # Create a placeholder for the response
            response_placeholder = st.empty()
            
            # Show spinner in the UI
            with st.spinner("Agent is thinking..."):
                # Capture any stdout that might be generated
                with capture_stdout() as captured_output:
                    # Only import and initialize the agent when explicitly triggered by user
                    if not st.session_state.agent_loaded:
                        # Import the agent only when needed
                        
                        
                        # Set the API key in the environment
                        
                        
                        # Create a new agent with the selected model
                        st.session_state.agent = Agent(
                            model=OpenAIChat(id=st.session_state.selected_model),
                            tools=[ThinkingTools()],
                            markdown=True,
                            instructions=(
                                "You are an uncertainty-aware reasoning agent. Follow these rules:\n"
                                "1. Explicitly evaluate your confidence for each reasoning step\n"
                                "2. If ANY uncertainty exists in final answer confidence, say 'I don't know'\n"
                                "3. Never guess or provide adjacent/similar answers\n"
                                "4. Flag ambiguous terms or unclear requirements\n"
                                "\nReasoning format:\n"
                                "1. Question analysis\n"
                                "2. Knowledge verification\n"
                                "3. Confidence assessment\n"
                                "4. Final answer decision"
                            )
                        )
                        st.session_state.agent_loaded = True
                    
                    # Use the agent's run method (correct method for Agno Agent)
                    response = st.session_state.agent.run(
                        question_to_ask,
                        show_full_reasoning=True
                    )
                
                # Display any captured output first (if any)
                captured_text = captured_output.getvalue()
                if captured_text:
                    response_placeholder.markdown(f"```\n{captured_text}\n```")
                
                # Display the response
                response_placeholder.markdown(response.content)
    else:
        st.warning("Please enter a question or select a sample question first.")

# Footer
st.markdown("---")

