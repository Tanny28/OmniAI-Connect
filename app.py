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
        <a href="https://www.canva.com/design/DAGUIKuxKWQ/4ieiuxWMEWG164U4N80sNw/view?utm_content=DAGUIKuxKWQ&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">Employee Field Guide</a>
    """, unsafe_allow_html=True)
    
    search_query = st.text_input("Search")  # Search input field
    if st.button("Voice Assist"):
        st.write("Voice assist functionality is not yet implemented.")  # Voice assist placeholder

# Main content: Professional AI Tools
st.header("1. Professional AI Tools")
professional_tools = [
    ("Timely", "https://timelyapp.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/timely.png", "Automatic time tracking software powered by AI."),
    ("Tetra", "https://www.tetra.ai/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/tetra.png", "An AI that takes notes during your calls and meetings."),
    ("Clockk", "https://www.clockk.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/clockk.png", "AI-based time management for freelancers and agencies."),
    ("Spoke", "https://www.askspoke.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/spoke.png", "AI-driven knowledge management for teams."),
    ("Receptiviti", "https://www.receptiviti.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/receptiviti.png", "AI-based emotional intelligence insights from conversations."),
    ("Flowrite", "https://www.flowrite.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/flowrite.png", "AI writing assistant for business emails and professional writing."),
    ("Aider", "https://www.aider.ai/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/aider.png", "AI-driven virtual assistant for accountants."),
    ("Gong.io", "https://www.gong.io/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/gongio.png", "AI-based sales analytics and coaching."),
    ("Textio", "https://textio.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/textio.png", "AI-enhanced writing for HR and recruitment."),
    ("WorkFusion", "https://www.workfusion.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/workfusion.png", "AI-powered digital workforce for repetitive office tasks."),
]

# Display professional tools with interactive icons
for name, url, icon_url, description in professional_tools:
    st.markdown(create_icon_link(name, url, icon_url, description), unsafe_allow_html=True)

# Task Management AI Tools
st.header("2. Task Management AI Tools")
task_management_tools = [
    ("ClickUp AI", "https://clickup.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/clickup.jpg", "AI-powered project management with task automation."),
    ("Krisp", "https://krisp.ai/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/krisp.jpg", "AI noise-cancelling for online meetings."),
    ("Superpowered", "https://www.superpowered.me/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/superpowered.jpg", "AI that helps to block distractions and focus."),
    ("TimeHero", "https://www.timehero.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/timehero.jpg", "AI task automation and time management tool."),
    ("Nanonets", "https://nanonets.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/nanonets.jpg", "AI for automating workflows with document recognition."),
    ("Taskade", "https://www.taskade.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/taskade.jpg", "AI-assisted task manager with collaboration features."),
    ("Notion AI", "https://www.notion.so/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/notion.jpg", "AI-enhanced note-taking and project management."),
    ("Omniflow", "https://omniflow.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/omniflow.jpg", "AI-powered assistant to manage tasks and emails."),
    ("Motion", "https://www.usemotion.io/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/motion.jpg", "AI-based time planner and task manager."),
    ("Friday", "https://www.friday.app/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/friday.jpg", "AI assistant for team task tracking and goal setting."),
]

# Display task management tools with interactive icons
for name, url, icon_url, description in task_management_tools:
    st.markdown(create_icon_link(name, url, icon_url, description), unsafe_allow_html=True)

# Footer container with "About Us" and "Contact" information
footer_container = st.container()

with footer_container:
    col1, col2 = st.columns([1, 1])
    with col1:
        st.text("ABOUT US")
    with col2:
        st.text("CONTACT")
