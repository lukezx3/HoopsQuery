import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './components/HomePage';
import QueryOutput from './components/QueryOutput';

function App() {

  //list of possible routes
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/result" element={<QueryOutput />} />
      </Routes>
    </Router>
  );
}

export default App;
