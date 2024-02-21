import React, { useContext, useState, useEffect } from 'react'
import AuthContext from '../context/AuthContext'

const AddOrderPage = () => {
  let { user, logoutUser } = useContext(AuthContext)
  const [services, setServices] = useState([]);
  const [clients, setClients] = useState([]);

  const fetchServices = async () => {
    try {
      const res = await fetch("/api/services/", {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!res.ok) {
        throw new Error('fetchServices response was not ok');
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

  const fetchClients = async () => {
    try {
      const res = await fetch("/api/clients/", {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!res.ok) {
        throw new Error('fetchClients response was not ok');
      }

      const data = await res.json();
      setClients(data);
      console.log('>>', data);
    } catch (error) {
      console.error('Error fetching services:', error);
      // Handle error - for example, logout user
      logoutUser();
    }
  };

  function getCurrentDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
  }

  useEffect(() => {
    fetchServices();
    
    if(user.group != 'client') {
      fetchClients();
    }
  }, []);

  return (
    <div>
      <h1>Add order</h1>
      <form>
        {user.group === 'client' ? (
          // If client is placing order then assign order to them.
          <input type="hidden" name="client" value={user.user_id} />
        ) : (
          <select name="clients">
            <option value="">Select a client</option>
            {clients.map(client => (
              <option key={client.id} value={client.id}>{client.first_name + ' ' + client.last_name}</option>
            ))}
          </select>
        )}
        <select name="services">
          <option value="">Select a service</option>
          {services.map(service => (
            <option key={service.id} value={service.id}>{service.name}</option>
          ))}
        </select>
        {/* Rethink what the statuses mean and be more specific. This could maybe be Accepted since I think we first though Accepted meant the client wanted to go through with the job. */}
        <input type="hidden" value='Pending' /> 

        <input type="text" name="total_cost"/> 
        <input type="hidden" name="date" value={getCurrentDate()} />
        <input type="submit" value="Send" />

      </form>
    </div>
  )
}

export default AddOrderPage