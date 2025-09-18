import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {get_teams} from "../api";


export default function Home() {
    const [teams, setTeams] = useState([]);

    useEffect(() => {
        get_teams().then(setTeams);
    }, []);


    return (
        <div className="p-6">
        <h1 className="text-xl font-bold mb-4">Valorant Match Predictor</h1>
        
        <div className="mb-4">
            <label className="block">Select Team 1:</label>
            <select value={team1} onChange={e => setTeam1(e.target.value)}>
            <option value="">-- Choose --</option>
            {teams.map(t => <option key={t.id} value={t.id}>{t.name}</option>)}
            </select>
        </div>

        <div className="mb-4">
            <label className="block">Select Team 2:</label>
            <select value={team2} onChange={e => setTeam2(e.target.value)}>
            <option value="">-- Choose --</option>
            {teams.map(t => <option key={t.id} value={t.id}>{t.name}</option>)}
            </select>
        </div>

        <button 
            className="bg-blue-600 text-white px-4 py-2 rounded"
            onClick={handleSubmit}
            disabled={!team1 || !team2}
        >
            Predict
        </button>
        </div>
    );
}