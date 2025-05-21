export default function ResponseBox({ response }) {
  return (
    <div className="mt-4 p-4 bg-gray-100 rounded shadow">
      <h2 className="font-bold">Gemini Response</h2>
      <p>{response}</p>
    </div>
  );
}


