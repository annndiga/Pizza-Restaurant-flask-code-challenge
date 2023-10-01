// RestaurantList.js
import React, { useEffect, useState } from 'react';
import './RestaurantList.css'; // Import your CSS file

function RestaurantList() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    // Make an API call to get the list of restaurants
    fetch('http://127.0.0.1:5555/restaurants') // Remove the leading /
      .then((response) => response.json())
      .then((data) => setRestaurants(data));
  }, []);

  return (
    <div className="restaurant-list-container">
      <h1 className="restaurant-list-title">Explore Nearby Restaurants</h1>
      <p className="restaurant-list-description">
        Discover a variety of delicious restaurants in your area. Whether you're
        craving pizza, sushi, or something else, you'll find it here.
      </p>
      <div className="restaurant-cards">
        {restaurants.map((restaurant) => (
          <div key={restaurant.id} className="restaurant-card">
            <h2 className="restaurant-name">{restaurant.name}</h2>
            <p className="restaurant-address">{restaurant.address}</p>
            <a className="view-details-link" href={`/restaurants/${restaurant.id}`}>
              View Details
            </a>
          </div>
        ))}
      </div>
    </div>
  );
}

export default RestaurantList;
