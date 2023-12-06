import './App.css';
import Header from './components/Header'
import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import PrivateRoutes from './utils/PrivateRoutes'
import { AuthProvider } from './context/AuthContext';

import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'

function App() {
  return (
    <div className="app">
      <Router>
        <AuthProvider>

          <Header />
          <Routes>
            <Route element={<PrivateRoutes />}>
              <Route path="/" exact element={<HomePage />} />
            </Route>

            <Route path="/login" element={<LoginPage />} />
          </Routes>
        </AuthProvider>
      </Router>
    </div>
  );
}

export default App;
