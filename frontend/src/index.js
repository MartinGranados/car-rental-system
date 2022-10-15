// Imports
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import { QueryClient, QueryClientProvider, } from 'react-query';
import { ReactQueryDevtools } from 'react-query/devtools'

// Page Imports
import Homepage from './routes/Hompage'
import Results from './routes/Results'

const root = ReactDOM.createRoot(document.getElementById('root'));
const queryClient = new QueryClient();

root.render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <Router>
        <Routes>
          <Route path='/' element={<Homepage />} />
          <Route path='results' element={<Results />} />
        </Routes>
      </Router>
      <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  </React.StrictMode>
);
