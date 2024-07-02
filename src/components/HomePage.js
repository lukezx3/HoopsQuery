//import libraries
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/HomePage.css';
const HomePage = () => {
  const [query, setQuery] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      //use JavaScript's fetch API to send request to server-side (app.py)
      const url = "http://127.0.0.1:5000/query";
      const response = await fetch(url, {
        method: "POST",
        headers: {
          'Content-Type': 'application/json' //use content-type header resolve CORS conflict
        },
        body: JSON.stringify({input: query})
      });
      
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
      //retrieve server-side response and redirect it to QueryOutput page with the data
      const responseJson = await response.json();
      navigate('/result', { state: {resultList: responseJson}});

    } catch (error) {
      console.error(error.message);
    }
  };

  const handleChange = (event) => {
    setQuery(event.target.value);
  };

  //html code for outputting the home page
  return (
    <div className="home-page">
      <div id="home"></div>
      <div className="container">
        <h1>NBA Shot Predictor</h1>

          <div className="input-container">
            <form onSubmit={handleSubmit}>
              <input type="text" name="query" placeholder="Enter your query here" value = {query} onChange={handleChange}></input>
              <br/>
              <input type="submit" value="Submit"></input>
            </form>
          </div>

      </div>
    </div>
  );
};

export default HomePage;