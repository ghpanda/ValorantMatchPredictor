const API_URL = "http://127.0.0.1:8000/"

export async function getTeams() {
    const res = await fetch9(`${API_URL}/teams`);
    return res.json();
}