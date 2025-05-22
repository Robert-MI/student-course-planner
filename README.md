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

