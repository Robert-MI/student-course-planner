import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import google.generativeai as genai
from planner.config import generation_config, safety_settings, system_instruction
from planner.course_scraper import fetch_courses

load_dotenv()

# Read external context files
def read_file_contents(filename):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        base_dir = os.getcwd()
    file_path = os.path.join(base_dir, filename)
    with open(file_path, "r") as f:
        return f.read()

# Format the scraped course data
def format_course_catalog(courses):
    catalog = "Here are the available courses:\n"
    for course in courses:
        section = course.get('section', '').strip()
        section_text = f" | Section: {section}" if section and section.lower() != 'o' and section != '0' else ""
        catalog += f"- {course['course_name']} | {course['course_time']} | Instructor: {course['instructor']}{section_text}\n"
    return catalog

# Load Gemini and context
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash-preview-05-20",
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

# Handle incoming Telegram messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()
    enriched_input = f"{full_context}\n\nStudent asks: {user_input}"
    response = chat.send_message(enriched_input)
    await update.message.reply_text(response.text.strip())

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Telegram bot is running...")
    app.run_polling()
