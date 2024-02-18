import React, { useContext, useState, useEffect } from 'react'
import AuthContext from '../context/AuthContext'

const AddOrderPage = () => {
  let { user, logoutUser } = useContext(AuthContext)
  const [services, setServices] = useState([]);


  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch("/api/services/", {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          },
        });
  
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
  
        const data = await res.json();
        setServices(data);
        console.log('>>', data);
      } catch (error) {
        console.error('Error fetching services:', error);
        // Handle error - for example, logout user
        logoutUser();
      }
    };
  
    fetchData();
  }, []);
  

  return (
    <div>
      <h1>Add order</h1>
      <form >
        <input type="hidden" name="client" value={user.user_id} />
        <select name="service">
          <option></option>
          {/* Add all services */}
        </select>
        <select name="cur_status">
        </select>

        <input type="text" name="total_cost" /> 
        {/* calculate total cost base on service cost */}
        <input type="date" name="date" />
        {/* curdate */}
        <input type="submit" />
      </form>
    </div>
  )
}

export default AddOrderPage