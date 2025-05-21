document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("menuForm");
  const message = document.getElementById("message");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const Producte = document.getElementById("producte").value.trim();
    const Precio = parseInt(document.getElementById("precio").value);
    const Fecha_y_hora = document.getElementById("fecha").value;

    if (!Producte || isNaN(Precio) || !Fecha_y_hora) {
      message.textContent = "Tots els camps són obligatoris.";
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/menus/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ Producte, Precio, Fecha_y_hora }),
      });

      if (!response.ok) throw new Error("Error afegint menú");

      message.textContent = "Menú afegit correctament!";
      form.reset();
    } catch (error) {
      message.textContent = "Error: No s'ha pogut afegir el menú.";
      console.error("Error:", error);
    }
  });
});
