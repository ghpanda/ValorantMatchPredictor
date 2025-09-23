import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Home() {
  const [teams, setTeams] = useState([]);
  const [teamA, setTeamA] = useState("");
  const [teamB, setTeamB] = useState("");
  const navigate = useNavigate();

  // Fetch teams from backend when component loads
  // Runs each time the component is rendered
  useEffect(() => {
    // console.log("Fetching teams from backend...");
    fetch("http://127.0.0.1:8000/teams") // your FastAPI endpoint
      .then((res) => res.json())
      .then((data) => {
        // console.log("Fetched teams:", data);
        setTeams(data);
      })    
      .catch((err) => console.error("Error fetching teams:", err));
  }, []);

  // Handle prediction button click
  const handlePredict = () => {
    if (teamA && teamB && teamA !== teamB) {
      navigate(`/predict?teamA=${teamA}&teamB=${teamB}`);
    } else {
      alert("Please select two different teams.");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Valorant Match Predictor</h1>
      <p>Select two teams to see the prediction.</p>

      <div style={{ marginBottom: "1rem" }}>
        <label>
          Team A:
          <select
            value={teamA}
            onChange={(e) => setTeamA(e.target.value)}
            style={{ marginLeft: "0.5rem" }}
          >
            <option value="">-- Select Team --</option>
            {teams.map((team) => (
              <option key={team.id} value={team.name}>
                {team.name}
              </option>
            ))}
          </select>
        </label>
      </div>

      <div style={{ marginBottom: "1rem" }}>
        <label>
          Team B:
          <select
            value={teamB}
            onChange={(e) => setTeamB(e.target.value)}
            style={{ marginLeft: "0.5rem" }}
          >
            <option value="">-- Select Team --</option>
            {teams.map((team) => (
              <option key={team.id} value={team.name}>
                {team.name}
              </option>
            ))}
          </select>
        </label>
      </div>

      <button onClick={handlePredict}>Predict</button>
    </div>
  );
}
