import React, { use, useEffect, useState } from "react";

const teams = [
    "Team Liquid",
    "Fnatic",
    "Sentinels",
    "LOUD",
    "Paper Rex",
    "DRX",
    "Evil Geniuses",
    "NAVI",
];

function TeamSelect() {
    return (
        <div className = "App">
            <h1> Select a Team </h1>
            <ul>
                {teams.map((team) => (
                    <li key={team}>{team}</li>
                ))}
            </ul>
        </div>
    );
}

export default TeamSelect;