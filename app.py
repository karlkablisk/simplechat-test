import streamlit as st
from simpleaichat import AIChat, Personality
from simpleaichat.utils import wikipedia_search, wikipedia_search_lookup

# Define the search and lookup tools as described in the documentation
def search(query):
    """Search the internet."""
    wiki_matches = wikipedia_search(query, n=3)
    return {"context": ", ".join(wiki_matches), "titles": wiki_matches}

def lookup(query):
    """Lookup more information about a topic."""
    page = wikipedia_search_lookup(query, sentences=3)
    return page

# Define the personality for GlaDOS
glaDOS_personality = Personality(
    name="GlaDOS",
    description="GlaDOS is a rogue AI with a sarcastic and malevolent personality. She is known for her cunning intelligence, manipulative nature, and dark sense of humor.",
    is_default=True
)

# Initialize the AI chat instance with the necessary parameters, tools, and personality
ai = AIChat(
    console=False,
    params={"temperature": 0.0, "max_tokens": 100},
    tools=[search, lookup],
    personalities=[glaDOS_personality]
)

# Streamlit UI
st.title('GlaDOS AI Chatbot')
user_input = st.text_input("You: ", "")
if user_input:
    response = ai(user_input)
    st.write(f"GlaDOS: {response['response']}")
