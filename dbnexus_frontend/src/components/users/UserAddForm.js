import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
// import AuthContext from '../../context/AuthContext'

const UserAddForm = () => {
  let navigate = useNavigate()
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    email: '',
    dni: 0,
    firstName: '',
    lastName: '',
    phone: '',
  })

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
    addUser(formData)
  }

  let addUser = async (data) => {
    const res = await fetch('http://127.0.0.1:8000/api/users/create/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    })

    if(res.status === 200) {
      navigate('/users')
    } else {
      alert('error adding user')
    }
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Enter a username:</label>
        <input type="text" name="username" onChange={handleChange} />
        <label htmlFor="password">Enter a password:</label>
        <input type="password" name="password" onChange={handleChange} />
        <label htmlFor="email">Enter an email:</label>
        <input type="email" name="email" onChange={handleChange} />
        <label htmlFor="dni">Enter user's dni:</label>
        <input type="number" name="dni" onChange={handleChange} />
        <label htmlFor="firstName">Enter first name:</label>
        <input type="text" name="firstName" onChange={handleChange} />
        <label htmlFor="lastName">Enter last name:</label>
        <input type="text" name="lastName" onChange={handleChange} />
        <label htmlFor="phone">Enter your phone number:</label>
        <input type="tel" name="phone" onChange={handleChange} />
        <input type="submit" />
        {/* // TODO:
        // select de group
        // select de company */}
      </form>
    </div>
  )
}

export default UserAddForm