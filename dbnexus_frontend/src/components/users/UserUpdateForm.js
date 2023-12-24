import React, { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'

const UserAddForm = () => {
  let navigate = useNavigate()
  const { userId } = useParams()
  const [formData, setFormData] = useState({
    id: '',
    username: '',
    email: '',
    firstName: '',
    lastName: '',
    password: '',
  });

  let getUser = async () => {
    // console.log('userId >>', userId)
    let res = await fetch(`/api/users/${userId}/`)
    let data = await res.json()
    // console.log('data', data)

    // Update formData state with the extracted fields
    setFormData({
      id: data.id || '',
      username: data.username || '',
      email: data.email || '',
      firstName: data.first_name || '',
      lastName: data.last_name || '',
      password: data.password
    });
  }

  const updateUser = async (data) => {
    let sendData = {
      username: data.username,
      password: data.password,
      email: data.email,
      first_name: data.firstName,
      last_name: data.lastName,
    }
    // console.log('data', sendData)

    let res = await fetch(`/api/users/${userId}/`, {
      method: "PUT",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(sendData)
    })

    if(res.status === 200) {
      navigate('/users')
    } else {
      alert(`Error updating user ${data.username}`)
    }
  }

  const handleChange = (e) => {
    // console.log('formData >>>>>', formData)
    const {name, value} = e.target
    setFormData((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    updateUser(formData)
  }

  useEffect(() => {
    getUser()
  }, [])

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Enter a username:</label>
        <input type="text" name="username" value={formData.username} onChange={handleChange} />
        {/* <label htmlFor="password">Enter a password:</label> */}
        <input type="hidden" name="password" value={formData.password} />
        <label htmlFor="email">Enter an email:</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange} />
        <label htmlFor="firstName">Enter first name:</label>
        <input type="text" name="firstName" value={formData.firstName} onChange={handleChange} />
        <label htmlFor="lastName">Enter last name:</label>
        <input type="text" name="lastName" value={formData.lastName} onChange={handleChange} />
        <input type="submit" />
        {/* // TODO:
        // select de group
        // select de company */}
      </form>
    </div>
  )
}

export default UserAddForm