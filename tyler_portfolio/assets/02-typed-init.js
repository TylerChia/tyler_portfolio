window.addEventListener("load", function () {
  setTimeout(function () {
    if (typeof Typed !== "undefined") {
      new Typed("#typed-output", {
        strings: [
          "Machine Learning Engineer",
          "Data Scientist",
          "Web App Developer",
          "Pokémon Enthusiast",
          "Sports Fan"
        ],
        typeSpeed: 70,
        backSpeed: 45,
        backDelay: 1500,
        loop: true
      });
    } else {
      console.error("Typed.js not loaded!");
    }
  }, 500);
});
