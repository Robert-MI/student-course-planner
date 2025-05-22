import os
import google.generativeai as genai
from dotenv import load_dotenv
from planner.config import generation_config, safety_settings, system_instruction
from planner.course_scraper import fetch_courses

load_dotenv()

def read_file_contents(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    with open(file_path, "r") as f:
        return f.read()

def format_course_catalog(courses):
    catalog = "Here are the available courses:\n"
    for course in courses:
        section = course.get('section', '').strip()
        section_text = f" | Section: {section}" if section and section not in ['0', 'O', 'o'] else ""
        catalog += f"- {course['course_name']} | {course['course_time']} | Instructor: {course['instructor']}{section_text}\n"
    return catalog

class ChatHandler:
    def __init__(self, chat, context):
        self.chat = chat
        self.context = context

    def send_message(self, user_input):
        enriched_input = f"{self.context}\n\nStudent asks: {user_input}"
        return self.chat.send_message(enriched_input)

def start_chat_session():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash-preview-05-20",
        safety_settings=safety_settings,
        generation_config=generation_config,
        system_instruction=system_instruction,
    )

    chat = model.start_chat(history=[])

    courses = fetch_courses()
    catalog = format_course_catalog(courses)
    constraints = read_file_contents("Schedule_Constraints.txt")
    schedule = read_file_contents("BSCS_Typical_Schedule.csv")

    context = (
        f"These are the student's constraints:\n{constraints}\n\n"
        f"This is the student's typical BSCS schedule:\n{schedule}\n\n"
        f"{catalog}"
    )

    return ChatHandler(chat, context)

