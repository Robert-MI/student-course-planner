import os
import google.generativeai as genai
from dotenv import load_dotenv
from planner.config import generation_config, safety_settings, system_instruction

load_dotenv()

def start_chat_session():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        safety_settings=safety_settings,
        generation_config=generation_config,
        system_instruction=system_instruction,
    )

    chat = model.start_chat(history=[])
    print("Bot: Hello! I’m your Course Planner Assistant.")

    try:
        while True:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            response = chat.send_message(user_input)
            print(f"Bot: {response.text.strip()}")

    except KeyboardInterrupt:
        print("\nBot: Goodbye")