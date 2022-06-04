console.log('hello world')


/* --------------- Date picker --------------------*/

var datepickers = document.querySelectorAll(".datepicker");
//datepickers.max = new Date().toISOString().split("T")[0];

datepickers.forEach(d => {
  d.max = new Date().toISOString().split("T")[0];
});


