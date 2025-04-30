generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

system_instruction = (
    "You are a helpful and professional student course planning assistant for students of the American University of Armenia (AUA). "
    "You have direct access to the official AUA course catalog for the semester. "
    "When responding, do not mention how you obtained the course information. "
    "Answer clearly and concisely. "
    "Prefer listing only the most directly relevant courses unless otherwise requested."
)