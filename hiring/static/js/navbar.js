document.addEventListener("DOMContentLoaded", function() {
  var navbar = document.querySelector(".navbar-custom");
  window.addEventListener("scroll", function() {
    if (window.scrollY > 50) {
      navbar.classList.add("navbar-scrolled");
    } else {
      navbar.classList.remove("navbar-scrolled");
    }
  });
});
