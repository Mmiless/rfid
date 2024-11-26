import {BrowserRouter, Routes, Route} from 'react-router-dom'
import AccessDenied from './pages/AccessDenied.tsx';
import Dashboard from './pages/Dashboard.tsx';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<AccessDenied />} />
          <Route path='/Dashboard' element={<Dashboard/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
