const usersModule = document.getElementById("usersModule");
usersModule.addEventListener("click", function () {
  window.location.href = "clients/clients_form.html";
});

const clientsModule = document.getElementById("clientsModule");
clientsModule.addEventListener("click", function () {
  window.location.href = "clients/clients_table.html";
});

const menusModule = document.getElementById("menusModule");
menusModule.addEventListener("click", function () {
  window.location.href = "menus/menus_form.html"; // ✅ NUEVO
});
