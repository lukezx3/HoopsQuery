import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Link, Switch, Redirect } from 'react-router-dom';

function Index() {
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    window.location.href = `/query?query=${encodeURIComponent(query)}`;
  };

  const handleChange = (e) => {
    setQuery(e.target.value);
  };

  return (
    <div>
      <h1>NBA Shot Predictor</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Enter your query:
          <input
            type="text"
            value={query}
            onChange={handleChange}
            placeholder="Enter your query here"
          />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

function QueryOutput() {
  return <div>Hello</div>;
}

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Index} />
        <Route exact path="/query" component={QueryOutput} />
      </Switch>
    </Router>
  );
}

export default App;
