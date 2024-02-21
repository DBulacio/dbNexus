import React, { useContext } from 'react'
import { Link } from 'react-router-dom'
import AuthContext from '../context/AuthContext'
import '../App.css'

const Header = () => {
  const { user, logoutUser } = useContext(AuthContext)

  return (
    <div>
      {user ? (
        // Render navigation based on user's group
        <nav className='navbar'>
          {user.group === 'client' ? (
            <Link onClick={logoutUser}>Logout</Link>
          ) : (
            <>
              <Link to="/">Home</Link>
              <Link to="/users">Users</Link>
              <Link to="/order/add">Add order</Link>
              <Link onClick={logoutUser}>Logout</Link>
            </>
          )}
        </nav>
      ) : (
        <p>LOGIN</p>
      )}

      {user && <p>Hello {user.username}</p>}
    </div>
  )
}

export default Header
