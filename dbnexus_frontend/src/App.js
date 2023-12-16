import './App.css';
import Header from './components/Header'
import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import UsersPage from './pages/UsersPage'
import UserAddForm from './components/users/UserAddForm'
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
            <Route path="/users" element={<UsersPage />} />
            <Route path="/users/add" element={<UserAddForm />} />
          </Routes>
        </AuthProvider>
      </Router>
    </div>
  );
}

export default App;
