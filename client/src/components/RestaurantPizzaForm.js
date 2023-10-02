import React, { useState } from "react";

function RestaurantPizzaForm() {
  const [formData, setFormData] = useState({
    price: '',
    pizza_id: '',
    restaurant_id: '',
  });

  const [errors, setErrors] = useState([]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Make an API call to create a new RestaurantPizza entry
    fetch('http://127.0.0.1:5555/restaurant_pizzas', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((response) => {
        if (response.ok) {
          // Clear the form and show success message
          setFormData({
            price: '',
            pizza_id: '',
            restaurant_id: '',
          });
          setErrors([]);
          return response.json();
        } else {
          return response.json().then((data) => {
            throw new Error(data.errors.join(', '));
          });
        }
      })
      .catch((error) => {
        setErrors([error.message]);
      });
  };

  return (
    <div>
      <h1>Add Restaurant Pizza</h1>
      {errors.length > 0 && (
        <div className="errors">
          <p>{errors.join(', ')}</p>
        </div>
      )}
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="price">Price:</label>
          <input
            type="number"
            id="price"
            name="price"
            value={formData.price}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="pizza_id">Pizza ID:</label>
          <input
            type="number"
            id="pizza_id"
            name="pizza_id"
            value={formData.pizza_id}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="restaurant_id">Restaurant ID:</label>
          <input
            type="number"
            id="restaurant_id"
            name="restaurant_id"
            value={formData.restaurant_id}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit">Add Pizza</button>
      </form>
    </div>
  );
}

export default RestaurantPizzaForm;
