// Imports
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'

// Page Imports
import Homepage from './routes/Hompage'
import Results from './routes/Results'




const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path='/' element={<Homepage />} />
        <Route path='results' element={<Results />} />
      </Routes>
    </Router>
  </React.StrictMode>
);
