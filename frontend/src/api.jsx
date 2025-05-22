// api.js

// Send student query to backend and return Gemini's response
export async function sendQuery(query) {
  const res = await fetch("http://localhost:5000/api/query", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query }),
  });

  if (!res.ok) throw new Error("Failed to send query");
  return res.json(); // Return response as JSON
}

// Fetch all courses from backend endpoint
export async function getCourses() {
  const res = await fetch("http://localhost:5000/api/courses");
  if (!res.ok) throw new Error("Failed to fetch courses");
  return res.json(); // Return list of courses
}

