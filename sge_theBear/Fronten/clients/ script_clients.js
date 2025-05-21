document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("clientForm");
  const message = document.getElementById("message");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const age = parseInt(document.getElementById("age").value);

    if (!name || !email || isNaN(age)) {
      message.textContent = "Tots els camps són obligatoris.";
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/clients/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, age }),
      });

      if (!response.ok) throw new Error("Error afegint client");

      message.textContent = "Client afegit correctament!";
      form.reset();
    } catch (error) {
      message.textContent = "Error: No s'ha pogut afegir el client.";
      console.error("Error:", error);
    }
  });
});
