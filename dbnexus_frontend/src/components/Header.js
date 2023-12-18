import React, { useContext } from 'react'
import { Link } from 'react-router-dom'
import AuthContext from '../context/AuthContext'

const Header = () => {
  let {user, logoutUser} = useContext(AuthContext)

  return (
    <div>
      {user ? (
        <nav>
          <Link to="/">Home</Link>
          <Link to="/users">Users</Link>
          <p onClick={logoutUser}>Logout</p>
        </nav>
      ) : (
        <p>LOGIN</p>
      )}

      {user && <p>Hello {user.username}</p>}
    </div>
  )
}

export default Header