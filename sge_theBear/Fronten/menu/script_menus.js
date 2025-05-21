const API_URL = "http://localhost:8000/menus/";

async function fetchMenus() {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) {
      throw new Error(`Error en la sol·licitud: ${response.status}`);
    }

    const menus = await response.json();
    displayMenus(menus);
  } catch (error) {
    console.error("Error al obtenir els menús:", error);
  }
}

function displayMenus(menus) {
  const tableBody = document.querySelector("#menusTable tbody");
  tableBody.innerHTML = "";

  menus.forEach(menu => {
    const row = document.createElement("tr");

    const idCell = document.createElement("td");
    idCell.textContent = menu.ID_compra;
    row.appendChild(idCell);

    const producteCell = document.createElement("td");
    producteCell.textContent = menu.Producte;
    row.appendChild(producteCell);

    const precioCell = document.createElement("td");
    precioCell.textContent = menu.Precio;
    row.appendChild(precioCell);

    const fechaCell = document.createElement("td");
    fechaCell.textContent = menu.Fecha_y_hora;
    row.appendChild(fechaCell);

    tableBody.appendChild(row);
  });
}

document.addEventListener("DOMContentLoaded", fetchMenus);
