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

# Create a container for the header
header_container = st.container()

# Add the logo and navigation links
with header_container:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.image("https://github.com/your-repo/OMNIAI-Connect/assets/logo.png", width=100)  # Replace with your logo URL
    with col2:
        st.title("OMNIAI Connect")
    with col3:
        search_query = st.text_input("Search")  # Search input field
        if st.button("Voice Assist"):
            st.write("Voice assist functionality is not yet implemented.")  # Voice assist placeholder

# Function to filter tools based on the search query
def filter_tools(tools, query):
    return [tool for tool in tools if query.lower() in tool[0].lower() or query.lower() in tool[3].lower()]

# Professional AI Tools
st.header("1. Professional AI Tools")
professional_tools = [
    ("Timely", "https://timelyapp.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/timely.png", "Automatic time tracking software powered by AI."),
    ("Tetra", "https://www.tetra.ai/", "https://github.com/your-repo/OMNIAI-Connect/assets/tetra.png", "An AI that takes notes during your calls and meetings."),
    ("Clockk", "https://www.clockk.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/clockk.png", "AI-based time management for freelancers and agencies."),
    ("Spoke", "https://www.askspoke.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/spoke.png", "AI-driven knowledge management for teams."),
    ("Receptiviti", "https://www.receptiviti.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/receptiviti.png", "AI-based emotional intelligence insights from conversations."),
    ("Flowrite", "https://www.flowrite.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/flowrite.png", "AI writing assistant for business emails and professional writing."),
    ("Aider", "https://www.aider.ai/", "https://github.com/your-repo/OMNIAI-Connect/assets/aider.png", "AI-driven virtual assistant for accountants."),
    ("Gong.io", "https://www.gong.io/", "https://github.com/your-repo/OMNIAI-Connect/assets/gongio.png", "AI-based sales analytics and coaching."),
    ("Textio", "https://textio.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/textio.png", "AI-enhanced writing for HR and recruitment."),
    ("WorkFusion", "https://www.workfusion.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/workfusion.png", "AI-powered digital workforce for repetitive office tasks."),
]

# Task Management AI Tools
st.header("2. Task Management AI Tools")
task_management_tools = [
    ("ClickUp AI", "https://clickup.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/clickup.png", "AI-powered project management with task automation."),
    ("Krisp", "https://krisp.ai/", "https://github.com/your-repo/OMNIAI-Connect/assets/krisp.png", "AI noise-cancelling for online meetings."),
    ("Superpowered", "https://www.superpowered.me/", "https://github.com/your-repo/OMNIAI-Connect/assets/superpowered.png", "AI that helps to block distractions and focus."),
    ("TimeHero", "https://www.timehero.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/timehero.png", "AI task automation and time management tool."),
    ("Nanonets", "https://nanonets.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/nanonets.png", "AI for automating workflows with document recognition."),
    ("Taskade", "https://www.taskade.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/taskade.png", "AI-assisted task manager with collaboration features."),
    ("Notion AI", "https://www.notion.so/", "https://github.com/your-repo/OMNIAI-Connect/assets/notion.png", "AI-enhanced note-taking and project management."),
    ("Omniflow", "https://omniflow.com/", "https://github.com/your-repo/OMNIAI-Connect/assets/omniflow.png", "AI-powered assistant to manage tasks and emails."),
    ("Motion", "https://www.usemotion.io/", "https://github.com/your-repo/OMNIAI-Connect/assets/motion.png", "AI-based time planner and task manager."),
    ("Friday", "https://www.friday.app/", "https://github.com/your-repo/OMNIAI-Connect/assets/friday.png", "AI assistant for team task tracking and goal setting."),
]

# Filter and display tools based on search
if search_query:
    filtered_professional_tools = filter_tools(professional_tools, search_query)
    filtered_task_management_tools = filter_tools(task_management_tools, search_query)
else:
    filtered_professional_tools = professional_tools
    filtered_task_management_tools = task_management_tools

# Display filtered Professional Tools
for name, url, icon_url, description in filtered_professional_tools:
    st.markdown(create_icon_link(name, url, icon_url, description), unsafe_allow_html=True)

# Display filtered Task Management Tools
for name, url, icon_url, description in filtered_task_management_tools:
    st.markdown(create_icon_link(name, url, icon_url, description), unsafe_allow_html=True)

# Footer container with "About Us" and "Contact" information
footer_container = st.container()

with footer_container:
    col1, col2 = st.columns([1, 1])
    with col1:
        st.text("ABOUT US")
    with col2:
        st.text("CONTACT")
