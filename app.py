import streamlit as st

# ------------------ DATA ------------------ #

def get_roadmap():
    return {
        "Coding": [
            ("Basics of Programming", "Learn what programming is and how programs work."),
            ("Variables & Data Types", "Understand variables and types like int, float, char."),
            ("Conditions & Loops", "Learn if, for, while loops."),
            ("Functions", "Write reusable blocks of code."),
            ("Arrays & Lists", "Store multiple values."),
            ("Problem Solving", "Solve simple coding problems."),
            ("Mini Programs", "Create small programs."),
            ("Revision & Test", "Revise all topics + test")
        ],
        "Communication": [
            ("Self Introduction", "Learn to introduce yourself confidently."),
            ("Basic English Speaking", "Improve daily conversation skills."),
            ("Confidence Building", "Practice speaking with confidence."),
            ("Group Discussion", "Participate in discussions."),
            ("Presentation Skills", "Learn public speaking."),
            ("Interview Speaking", "Answer interview questions clearly."),
            ("Mock Interviews", "Practice interview scenarios."),
            ("Final Practice", "Revision + test")
        ],
        "Git": [
            ("What is Git & GitHub", "Version control basics."),
            ("Git Init, Status, Add", "Basic commands."),
            ("Branches", "Understand branching."),
            ("Merge", "Merge branches."),
            ("Push & Pull", "Sync with GitHub."),
            ("README File", "Project documentation."),
            ("Mini Project Repo", "Create sample repo."),
            ("Revision & Test", "Review + test")
        ],
        "LinkedIn": [
            ("Profile Creation", "Create LinkedIn profile."),
            ("Headline & Summary", "Write strong bio."),
            ("Skills Section", "Add technical skills."),
            ("Project Section", "Add projects."),
            ("Connections", "Grow network."),
            ("Posts & Activity", "Be active."),
            ("Job Search Basics", "Apply for jobs."),
            ("Profile Review", "Optimize profile")
        ]
    }


resources = {
    "Coding": "https://www.learn-c.org",
    "Communication": "https://www.englishclub.com",
    "Git": "https://www.atlassian.com/git/tutorials",
    "LinkedIn": "https://www.linkedin.com/learning"
}


mock_questions = [
    ("Did you understand today's topic?", ["Yes", "Somewhat", "No"], 0),
    ("Did you practice today?", ["Yes", "No"], 0),
    ("Can you explain the topic?", ["Yes", "No"], 0),
    ("Are you confident?", ["Yes", "No"], 0),
    ("Do you want to move next?", ["Yes", "No"], 0)
]

# ------------------ FUNCTIONS ------------------ #

def ai_doubt_response(doubt):
    return f"Good question! Here's a simple explanation: {doubt} can be understood with practice and examples. Try learning step by step and practicing daily."


# ------------------ STREAMLIT UI ------------------ #

st.set_page_config(page_title="Placement Preparation Tracker", layout="wide")

st.title("🎯 Placement Preparation Tracker")
st.subheader("4 Tracks × 8 Weeks Learning System")

if "progress" not in st.session_state:
    st.session_state.progress = {track: [False]*8 for track in get_roadmap()}

roadmap = get_roadmap()

track = st.sidebar.selectbox("Select Track", list(roadmap.keys()))
week = st.sidebar.selectbox("Select Week", range(1,9))

st.header(f"{track} - Week {week}")

topic, explanation = roadmap[track][week-1]

st.success(f"📘 Topic: {topic}")
st.write(f"📝 Explanation: {explanation}")
st.write(f"🔗 Resource: {resources[track]}")

# ------------------ DOUBTS ------------------ #

st.subheader("❓ Ask Your Doubt")

doubt = st.text_input("Enter your doubt here")

if st.button("Get Answer"):
    if doubt.strip() != "":
        st.info(ai_doubt_response(doubt))
    else:
        st.warning("Please enter a doubt.")

# ------------------ MOCK TEST ------------------ #

st.subheader("🧪 Weekly Mock Test")

score = 0
for i, (q, options, ans) in enumerate(mock_questions):
    user_ans = st.radio(q, options, key=f"{track}{week}{i}")
    if options.index(user_ans) == ans:
        score += 1

if st.button("Submit Test"):
    st.write(f"🎯 Your Score: {score}/5")
    if score >= 3:
        st.success("🎉 Passed! You can move to next week.")
        st.session_state.progress[track][week-1] = True
    else:
        st.error("❌ Please revise and try again.")

# ------------------ PROGRESS ------------------ #

st.subheader("📊 Progress Tracker")

completed = sum(st.session_state.progress[track])
st.progress(completed / 8)

st.write("Week Status:")
for i, done in enumerate(st.session_state.progress[track]):
    st.write(f"Week {i+1}: {'✅ Completed' if done else '❌ Not Completed'}")

st.info("Complete week tests to unlock progress!")

# ------------------ FOOTER ------------------ #

st.caption("Built for Students & Freshers 🚀")