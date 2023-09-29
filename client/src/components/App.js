import React from "react";
import { Route, Routes } from "react-router-dom"; // Import Routes
import RestaurantList from "./RestaurantList";
import RestaurantDetail from "./RestaurantDetail";
import PizzaList from "./PizzaList";
import RestaurantPizzaForm from "./RestaurantPizzaForm";

function App() {
  return (
    <div>
      <Routes> {/* Use Routes instead of Switch */}
        {/* Route to display the list of restaurants */}
        <Route path="/" element={<RestaurantList />} />

        {/* Route to display restaurant details */}
        <Route path="/restaurants/:id" element={<RestaurantDetail />} />

        {/* Route to display the list of pizzas */}
        <Route path="/pizzas" element={<PizzaList />} />

        {/* Route to add a new restaurant pizza */}
        <Route path="/add-restaurant-pizza" element={<RestaurantPizzaForm />} />

        {/* Add more routes as needed */}
      </Routes>
    </div>
  );
}

export default App;
