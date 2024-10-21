import streamlit as st

# Function to create an icon link
def create_icon_link(name, url, icon_url, description):
    return f"""
    <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <a href="{url}" target="_blank">
            <img src="{icon_url}" alt="{name} icon" width="40" style="margin-right: 15px;">
        </a>
        <div>
            <a href="{url}" target="_blank" style="text-decoration: none; font-size: 16px; font-weight: bold;">
                {name}
            </a>
            <p style="margin: 0; font-size: 14px;">{description}</p>
        </div>
    </div>
    """

# Set page title and layout
st.set_page_config(page_title="OMNIAI Connect", layout="wide")

# Create a container for the header with the Canva embed
header_container = st.container()
with header_container:
    st.markdown("""
        <div style="position: relative; width: 100%; height: 0; padding-top: 56.2225%;
        padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
        border-radius: 8px; will-change: transform;">
          <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
            src="https://www.canva.com/design/DAGUIKuxKWQ/4ieiuxWMEWG164U4N80sNw/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
          </iframe>
        </div>
        <a href="https://www.canva.com/design/DAGUIKuxKWQ/4ieiuxWMEWG164U4N80sNw/view?utm_content=DAGUIKuxKWQ&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener"></a>
    """, unsafe_allow_html=True)
    
    search_query = st.text_input("Search for AI tools...")  # Search input field
    if st.button("Voice Assist"):
        st.write("Voice assist functionality is not yet implemented.")  # Voice assist placeholder

# AI tools categorized by type
categories = {
    "note_making": [
        ("Tetra", "https://www.tetra.ai/", "https://example.com/tetra.png", "AI for note-taking during calls and meetings."),
        ("Notion AI", "https://www.notion.so/", "https://example.com/notion.png", "AI-enhanced note-taking and project management."),
        ("Evernote", "https://www.evernote.com/", "https://example.com/evernote.png", "Note-taking app with AI features for organization."),
        ("Roam Research", "https://roamresearch.com/", "https://example.com/roam.png", "AI-driven note-making and knowledge management.")
    ],
    "task_management": [
        ("ClickUp AI", "https://clickup.com/", "https://example.com/clickup.png", "AI-powered project management with task automation."),
        ("Omniflow", "https://omniflow.com/", "https://example.com/omniflow.png", "AI-powered assistant to manage tasks and emails."),
        ("Motion", "https://www.usemotion.io/", "https://example.com/motion.png", "AI-based time planner and task manager."),
        ("TimeHero", "https://www.timehero.com/", "https://example.com/timehero.png", "AI task automation and time management tool.")
    ],
    "meeting_scheduling": [
        ("Clara", "https://www.clara.com/", "https://example.com/clara.png", "AI-powered meeting scheduler."),
        ("X.ai", "https://x.ai/", "https://example.com/xai.png", "AI assistant for scheduling meetings."),
        ("CalendarHero", "https://calendarhero.com/", "https://example.com/calendarhero.png", "AI meeting scheduling and calendar management."),
        ("Spoke", "https://www.askspoke.com/", "https://example.com/spoke.png", "AI for meeting coordination and task assignment.")
    ]
}

# Keywords to match user intent
keywords_mapping = {
    "notes": "note_making",
    "make notes": "note_making",
    "note taking": "note_making",
    "task assist": "task_management",
    "task management": "task_management",
    "manage tasks": "task_management",
    "schedule meeting": "meeting_scheduling",
    "book meeting": "meeting_scheduling",
    "meeting assist": "meeting_scheduling"
}

# Function to filter tools based on the search query and keywords
def filter_tools(query):
    query = query.lower()
    # First, check if the query matches any specific AI tool name
    for category in categories.values():
        for tool in category:
            if tool[0].lower() in query:
                return [tool]  # Return the matching tool
    
    # Otherwise, match the query against keywords to find relevant categories
    for keyword, category in keywords_mapping.items():
        if keyword in query:
            return categories[category]
    
    return []

# Main content: Filter and display tools based on the search query
st.header("AI Tool Suggestions")

if search_query:
    filtered_tools = filter_tools(search_query)
    if not filtered_tools:
        st.write("No matching tools found for your search.")
    else:
        for name, url, icon_url, description in filtered_tools:
            st.markdown(create_icon_link(name, url, icon_url, description), unsafe_allow_html=True)
else:
    # Show default content or categories
    st.write("Enter a search query, such as 'I want to make notes' or 'I want a task assist' to get AI tool suggestions.")

# Footer container with "About Us" and "Contact" information
footer_container = st.container()

with footer_container:
    col1, col2 = st.columns([1, 1])
    with col1:
        st.text("ABOUT US")
    with col2:
        st.text("CONTACT")
