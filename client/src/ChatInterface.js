import React, { useState } from 'react';
import axios from 'axios';
import './ChatInterface.css'; // Optional CSS

const ChatInterface = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const res = await axios.post('http://localhost:5050/chat', { message: input });

      if (res.data.error) {
        setMessages((prev) => [...prev, { sender: 'bot', text: `Error: ${res.data.error}` }]);
      } else {
        const botMsg = { sender: 'bot', text: res.data.reply };
        setMessages((prev) => [...prev, botMsg]);
      }
    } catch (err) {
      console.error("Axios error:", err.response ? err.response.data : err.message);
      setMessages((prev) => [...prev, { sender: 'bot', text: `Error getting response: ${err.message}` }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <h2>Course Planner Assistant</h2>
      <div className="chat-box">
        {messages.map((msg, i) => (
          <div key={i} className={`chat-message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
        {loading && <div className="chat-message bot">Typing...</div>}
      </div>
      <div className="input-area">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask about your semester schedule..."
          onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default ChatInterface;

