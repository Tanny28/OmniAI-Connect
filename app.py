import streamlit as st
import speech_recognition as sr
import threading

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
    
    search_query = st.text_input("Search by AI tool or category")  # Search input field

    if st.button("Voice Assist"):
        st.write("Listening for your command...")  # Indicate that voice recognition is starting
        threading.Thread(target=recognize_speech).start()  # Run speech recognition in a separate thread

# Function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source)  # Listen for audio input

    try:
        command = r.recognize_google(audio)  # Convert audio to text
        st.success(f"You said: {command}")  # Display the recognized command
        process_command(command)  # Process the recognized command
    except sr.UnknownValueError:
        st.error("Could not understand audio.")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")

# Function to process the recognized command
def process_command(command):
    # Normalize command text for searching
    command = command.lower()
    
    # Check for category commands
    if "time management" in command:
        category = "Time Management"
        filtered_tools = filter_tools(professional_tools + task_management_tools, category)
        display_tools(filtered_tools)
    elif "open" in command:
        # Open specific tool based on the command
        tool_name = command.replace("open ", "").strip()
        open_tool(tool_name)
    else:
        st.warning("Please specify a valid category or tool to open.")

# Function to open the specified tool
def open_tool(tool_name):
    all_tools = professional_tools + task_management_tools
    for name, url, _, _ in all_tools:
        if tool_name.lower() in name.lower():
            st.write(f"Opening {name}...")
            js = f"window.open('{url}', '_blank');"
            st.components.v1.html(f"<script>{js}</script>", height=0)
            return
    st.error("Tool not found.")

# Function to filter tools based on the search query (searches both name and category)
def filter_tools(tools, query):
    return [tool for tool in tools if query.lower() in tool[0].lower() or query.lower() in tool[3].lower()]

# Main content: Professional AI Tools (with categories)
st.header("1. Professional AI Tools")
professional_tools = [
    ("Timely", "https://timelyapp.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/timely.png", "Time Management"),
    ("Tetra", "https://www.tetra.ai/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/tetra.png", "Note-taking, Meeting AI"),
    ("Clockk", "https://www.clockk.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/Clockk.png", "Time Management"),
    ("Spoke", "https://www.askspoke.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/Spoke.png", "Knowledge Management"),
    ("Receptiviti", "https://www.receptiviti.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/receptiviti.png", "Emotional Insights"),
    ("Flowrite", "https://www.flowrite.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/Flowrite.png", "Writing Assistance"),
    ("Aider", "https://www.aider.ai/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/Aider.png", "Virtual Assistant for Accountants"),
    ("Gong.io", "https://www.gong.io/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/Gong.io.png", "Sales Analytics"),
    ("Textio", "https://textio.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/Textio.png", "HR Writing Assistance"),
    ("WorkFusion", "https://www.workfusion.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/WorkFusion.png", "Task Automation"),
]

# Filter and display professional tools based on search
if search_query:
    filtered_professional_tools = filter_tools(professional_tools, search_query)
else:
    filtered_professional_tools = professional_tools

for name, url, icon_url, category in filtered_professional_tools:
    st.markdown(create_icon_link(name, url, icon_url, f"Category: {category}"), unsafe_allow_html=True)

# Task Management AI Tools (with categories)
st.header("2. Task Management AI Tools")
task_management_tools = [
    ("ClickUp AI", "https://clickup.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/clickup.png", "Task Scheduling, Project Management"),
    ("Krisp", "https://krisp.ai/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/krisp.png", "Noise Cancelling, Meetings"),
    ("Superpowered", "https://www.superpowered.me/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/superpowered.png", "Distraction Blocking"),
    ("TimeHero", "https://www.timehero.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/timehero.png", "Time Management, Task Automation"),
    ("Nanonets", "https://nanonets.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/nanonets.png", "Workflow Automation, Document Recognition"),
    ("Taskade", "https://www.taskade.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/taskade.png", "Task Manager, Collaboration"),
    ("Notion AI", "https://www.notion.so/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/notion.png", "Note-taking, Project Management"),
    ("Omniflow", "https://omniflow.com/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/omniflow.png", "Task and Email Management"),
    ("Motion", "https://www.usemotion.io/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/motion.png", "Time Planner, Task Manager"),
    ("Friday", "https://www.friday.app/", "https://raw.githubusercontent.com/Tanny28/OmniAi-Connect/main/friday.png", "Team Task Tracking"),
]

# Filter and display task management tools based on search
if search_query:
    filtered_task_management_tools = filter_tools(task_management_tools, search_query)
else:
    filtered_task_management_tools = task_management_tools

for name, url, icon_url, category in filtered_task_management_tools:
    st.markdown(create_icon_link(name, url, icon_url, f"Category: {category}"), unsafe_allow_html=True)

# Footer section
st.markdown("""
    <footer style="text-align: center; margin-top: 40px;">
        <p>© 2024 OMNIAI Connect. All rights reserved.</p>
    </footer>
""", unsafe_allow_html=True)
