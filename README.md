# Student Course Planner with Gemini 2.5

This project includes a Flask backend and a React frontend to interact with a Gemini-based course planning assistant.

## How to Run

### Backend

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your Gemini API key:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

3. Start the Flask backend server:

   ```bash
   python main.py
   ```

   

### Frontend

1. Navigate to the `client` folder:

   ```bash
   cd client
   ```

2. Install frontend dependencies:

   ```bash
   npm install
   ```

3. Start the React app:

   ```bash
   npm start
   ```

4. Open your browser at [http://localhost:3000](http://localhost:3000)



The frontend will send chat requests to the Flask backend running on port 5050.


### Telegram bot

This project includes a Telegram bot interface for interacting with the scheduling assistant directly via Telegram.

1. Install Telegram bot dependencies:

   ```bash
   pip install python-telegram-bot python-dotenv
   ```

2. In your .env file, add:npm install

   ```bash
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. Run the bot:

   ```bash
   python telegram_bot.py
   ```

4. Open your browser at [https://t.me/TheStudentPlannerBot](https://t.me/TheStudentPlannerBot)

The bot listens for incoming text messages from users.
It dynamically loads available course data, student constraints, and a typical BSCS schedule.
