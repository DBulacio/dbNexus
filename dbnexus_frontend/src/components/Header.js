import React, { useContext } from 'react'
import { Link } from 'react-router-dom'
import AuthContext from '../context/AuthContext'
import '../App.css'

const Header = () => {
  let {user, logoutUser} = useContext(AuthContext)

  return (
    <div>
      {user ? (
        <nav className='navbar'>
          <Link to="/">Home</Link>
          <Link to="/users">Users</Link>
          <Link onClick={logoutUser}>Logout</Link>
        </nav>
      ) : (
        <p>LOGIN</p>
      )}

      {user && <p>Hello {user.username}</p>}
    </div>
  )
}

export default Header