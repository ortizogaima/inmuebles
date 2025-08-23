import { useEffect, useState } from "react";
import React from "react";

function App() {
  const [inmuebles, setInmuebles] = React.useState([]);

  React.useEffect(() => {
    fetch("http://127.0.0.1:5000/api/inmuebles/")
      .then(res => res.json())
      .then(data => setInmuebles(data))
      .then(error => console.error("Error fetching inmuebles:", error));
  }, []);

  return (
    <div style={{ display: "block"}}>
      <h1>Lista de inmuebles</h1>
      {inmuebles.map((inmueble) => (
        <div key={inmueble.id}>
          <div class="card mb-4 shadow-sm border-0 rounded bg-light text-dark p-3" style={{ width: "540px" }}>
          <h3>Tipo: {inmueble.tipo} - {inmueble.operacion}</h3>
          <h4>Zona: {inmueble.zona}</h4>
          <h4>Domicilio: {inmueble.domiciliocalle} {inmueble.domicilioaltura}</h4>
          <h4>Precio: USD {inmueble.preciousd} - ARS {inmueble.precioars}</h4>
          <h5>Descripcion: {inmueble.descripcion}</h5>
          </div>
        </div>
      ))}
    </div>
  );
}

export default App;
