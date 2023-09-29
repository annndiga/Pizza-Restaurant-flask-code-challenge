import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

function RestaurantDetail() {
  const { id } = useParams();
  const [restaurant, setRestaurant] = useState(null);

  useEffect(() => {
    // Make an API call to get restaurant details by ID
    fetch(`/api/restaurants/${id}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Restaurant not found');
        }
        return response.json();
      })
      .then((data) => setRestaurant(data))
      .catch((error) => {
        console.error(error);
        setRestaurant({ error: 'Restaurant not found' });
      });
  }, [id]);

  if (restaurant === null) {
    return <p>Loading...</p>;
  }

  if (restaurant.error) {
    return <p>{restaurant.error}</p>;
  }

  return (
    <div>
      <h1>{restaurant.name}</h1>
      <p>{restaurant.address}</p>
      <h2>Pizzas</h2>
      <ul>
        {restaurant.pizzas.map((pizza) => (
          <li key={pizza.id}>
            <h3>{pizza.name}</h3>
            <p>Ingredients: {pizza.ingredients}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default RestaurantDetail;
