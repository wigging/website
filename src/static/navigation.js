const navigationToggle = document.querySelector(".nav-toggle");

navigationToggle.addEventListener("click", () => {
  const expanded = navigationToggle.getAttribute("aria-expanded") === "true";
  navigationToggle.setAttribute("aria-expanded", String(!expanded));
});
