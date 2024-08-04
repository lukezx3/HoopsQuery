//import libraries + files
import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import '../styles/QueryOutput.css';


//output query result
export default function QueryOutput () {
  //use location hook to retrieve response from HomePage route
  const location = useLocation();
  const result = location.state.resultList;
  const query = location.state.query;
  const navigate = useNavigate();

  //reroute back to home
  const goHome = () => {
    navigate('/');
  }

  //output result nicely
  return (
    <div className="stats-container">
      <h1 className="stats-title">Results To Your Question</h1>
        <p className="user-query">Your question: "{query}"</p>
      <ul className="stats-list">
        {result.map((player, index) => (
          <li key={index} className="stats-item">
            <span className="player-name">{player[0]}</span><span className="player-score">{player[1]}</span>
          </li>
        ))}
      </ul>
      <button onClick={goHome} className="back-button">
        New Question
      </button>
    </div>
  );
};


