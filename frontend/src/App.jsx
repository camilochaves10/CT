import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [apiStatus, setApiStatus] = useState("Checking API...");

  useEffect(() => {
    async function checkApi() {
      try {
        const response = await fetch("http://localhost:8000/health");

        if (!response.ok) {
          throw new Error("API request failed");
        }

        const data = await response.json();
        setApiStatus(`API status: ${data.status}`);
      } catch (error) {
        console.error(error);
        setApiStatus("API is unavailable");
      }
    }

    checkApi();
  }, []);

  return (
    <main>
      <h1>Clean Tangerine</h1>
      <p>Professional residential and commercial cleaning.</p>
      <p>{apiStatus}</p>
    </main>
  );
}

export default App;
