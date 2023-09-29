import React, { useEffect, useState } from 'react';

function PizzaList() {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    // Make an API call to get the list of pizzas
    fetch('/api/pizzas')
      .then((response) => response.json())
      .then((data) => setPizzas(data));
  }, []);

  return (
    <div>
      <h1>Pizza List</h1>
      <ul>
        {pizzas.map((pizza) => (
          <li key={pizza.id}>
            <h2>{pizza.name}</h2>
            <p>Ingredients: {pizza.ingredients}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PizzaList;
