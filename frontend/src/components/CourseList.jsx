// CourseList.jsx

// Display the list of fetched courses
export default function CourseList({ courses }) {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-2">Available Courses</h2>

      {/* Map through courses and display course information */}
      <ul className="space-y-1">
        {courses.map(course => (
          <li key={course.course_code} className="p-2 border rounded">
            {/* Course title and code */}
            <strong>{course.course_title}</strong> ({course.course_code}) — {course.course_time}
          </li>
        ))}
      </ul>
    </div>
  );
}


