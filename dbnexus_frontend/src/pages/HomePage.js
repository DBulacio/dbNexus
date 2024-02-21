import React, {useContext, useEffect} from 'react'
import AuthContext from '../context/AuthContext'

const HomePage = () => {
  let { user, logoutUser } = useContext(AuthContext)

  useEffect(() => {
    if(user.group != 'admin' && user.group != 'employee') {
      logoutUser();
    }
  }, []);

  return (
    <div>
      <p>Home Page</p>
    </div>
  )
}

export default HomePage