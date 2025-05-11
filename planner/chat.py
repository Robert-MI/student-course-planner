import os
import google.generativeai as genai
from dotenv import load_dotenv
from planner.config import generation_config, safety_settings, system_instruction
from planner.course_scraper import fetch_courses

load_dotenv()

def read_file_contents(filename):
    try:
        # If running from a script
        base_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        # Fallback for Spyder, Jupyter, etc.
        base_dir = os.getcwd()

    file_path = os.path.join(base_dir, filename)

    with open(file_path, "r") as f:
        return f.read()



def format_course_catalog(courses):
    catalog = "Here are the available courses:\n"
    for course in courses:
        section = course.get('section', '').strip()

        if section and section not in ['0', 'O', 'o']:
            section_text = f" | Section: {section}"
        else:
            section_text = ""

        catalog += f"- {course['course_name']} | {course['course_time']} | Instructor: {course['instructor']}{section_text}\n"
    return catalog

def start_chat_session():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel(
        model_name="gemini-2.5-pro-exp-03-25",
        safety_settings=safety_settings,
        generation_config=generation_config,
        system_instruction=system_instruction,
    )

    chat = model.start_chat(history=[])

    courses = fetch_courses()
    course_catalog = format_course_catalog(courses)
    
    constraints_text = read_file_contents("Schedule_Constraints.txt")
    typical_schedule = read_file_contents("BSCS_Typical_Schedule.csv")

    full_context = (
        f"These are the student's constraints:\n{constraints_text}\n\n"
        f"This is the student's typical BSCS schedule:\n{typical_schedule}\n\n"
        f"{course_catalog}"
    )


    print("Bot: Hello! I’m your Course Planner Assistant.")
    print(f"Bot: I have loaded {len(courses)} courses.\n")

    try:
        while True:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            enriched_input = f"{full_context}\n\nStudent asks: {user_input}"
            response = chat.send_message(enriched_input)

            print(f"Bot: {response.text.strip()}")

    except KeyboardInterrupt:
        print("\nBot: Goodbye")