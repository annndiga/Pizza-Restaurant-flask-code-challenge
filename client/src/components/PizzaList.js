import React, { useEffect, useState } from 'react';

function PizzaList() {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    console.log("Fetching pizzas...");
    fetch('http://127.0.0.1:5555/pizzas')
      .then((response) => response.json())
      .then((data) => {
        console.log("Received data:", data);
        setPizzas(data);
      })
      .catch((error) => console.error('Fetch error:', error));
  }, []);

  return (
    <div className="container"> {/* Apply a container class */}
      <h1 className="pizza-header">Pizza List</h1> {/* Apply a header class */}
      <ul className="pizza-list"> {/* Apply a list class */}
        {pizzas.map((pizza) => (
          <li key={pizza.id} className="pizza-item"> {/* Apply an item class */}
            <h2 className="pizza-name">{pizza.name}</h2> {/* Apply a name class */}
            <p className="pizza-ingredients">Ingredients: {pizza.ingredients}</p> {/* Apply an ingredients class */}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PizzaList;
