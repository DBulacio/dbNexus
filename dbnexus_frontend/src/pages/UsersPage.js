import React, {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom'

const UsersPage = () => {
  const navigate = useNavigate()
  let [users, setUsers] = useState([])

  let getUsers = async () => {
    let res = await fetch("http://127.0.0.1:8000/api/users/")
    let data = await res.json()

    setUsers(data)
    console.log('data', data)
  }

  useEffect(() => {
    getUsers()
  }, [])

  let deleteUser = async (id) => {
    fetch(`http://127.0.0.1:8000/api/users/${id}/`, {
      method: "DELETE",
      headers: {
        'Content-Type': 'application/json'
      }
    })
  }

  return (
    <div>
      <button onClick={() => navigate("add")}>(+) Add User</button>
      <div>
        <h1>Listado de usuarios</h1>
        {users.length > 0 ? (
          <span>
            {users.map((user, index) => (
              <span key={index}>
                <h2>{user.id}: {user.user.first_name} {user.user.last_name}, {user.dni}</h2>
                <button onClick={() => navigate(`update/${user.id}`)}>(*) Update User</button>
                <button onClick={() => deleteUser(user.id)}>(-) Delete User</button>
              </span>
            ))}
          </span>
        ) : (
          <p>No hay usuarios para mostrar</p>
        )}
        
      </div>
    </div>
  )
}

export default UsersPage