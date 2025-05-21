import CourseList from "./components/CourseList";
import { useEffect, useState } from "react";
import ChatInput from "./components/ChatInput";
import CourseList from "./components/CourseList";
import ResponseBox from "./components/ResponseBox";
import { getCourses, sendQuery } from "./api";

function App() {
  const [courses, setCourses] = useState([]);
  const [response, setResponse] = useState("");

  useEffect(() => {
    getCourses().then(setCourses).catch(console.error);
  }, []);

  const handleQuery = async (text) => {
    try {
      const result = await sendQuery(text);
      setResponse(result.response);
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div className="max-w-3xl mx-auto p-4 space-y-6">
      <h1 className="text-3xl font-bold">Student Course Planner</h1>
      <CourseList courses={courses} />
      <ChatInput onSend={handleQuery} />
      <ResponseBox response={response} />
    </div>
  );
}

export default App;

