import React, { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'

const UserAddForm = () => {
  let navigate = useNavigate()
  const { userId } = useParams()
  const [formData, setFormData] = useState({
    id: '',
    username: '',
    // password: '',
    email: '',
    dni: 0,
    firstName: '',
    lastName: '',
    phone: '',
  });

  let getUser = async () => {
    // console.log('userId >>', userId)
    let res = await fetch(`http://127.0.0.1:8000/api/users/${userId}/`)
    let data = await res.json()

    const userFields = data.user || {};

    // Update formData state with the extracted fields
    setFormData({
      id: userFields.id || '',
      username: userFields.username || '',
      password: userFields.password || '',
      email: userFields.email || '',
      dni: data.dni || 0,
      firstName: userFields.first_name || '',
      lastName: userFields.last_name || '',
      phone: data.phone || '',
    });
  }

  const updateUser = async (data) => {
    console.log('formData', formData)
    console.log('data', formData)
    let sendData = {
      user: {
        id: data.id,
        username: data.username || '',
        password: data.password || '',
        email: data.email || '',
        first_name: data.firstName || '',
        last_name: data.lastName || '',
      },
      dni: data.dni || 0,
      phone: data.phone || '',
    }

    let res = await fetch(`http://127.0.0.1:8000/api/users/${userId}/`, {
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
        {/* <label htmlFor="password">Enter a password:</label>
        <input type="password" name="password" value={formData.password} onChange={handleChange} /> */}
        <label htmlFor="email">Enter an email:</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange} />
        <label htmlFor="dni">Enter user's dni:</label>
        <input type="number" name="dni" value={formData.dni} onChange={handleChange} />
        <label htmlFor="firstName">Enter first name:</label>
        <input type="text" name="firstName" value={formData.firstName} onChange={handleChange} />
        <label htmlFor="lastName">Enter last name:</label>
        <input type="text" name="lastName" value={formData.lastName} onChange={handleChange} />
        <label htmlFor="phone">Enter your phone number:</label>
        <input type="tel" name="phone" value={formData.phone} onChange={handleChange} />
        <input type="submit" />
        {/* // TODO:
        // select de group
        // select de company */}
      </form>
    </div>
  )
}

export default UserAddForm