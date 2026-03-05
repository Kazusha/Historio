const  slider = document.getElementById("slider");
const nextBtn = document.getElementById("nextBtn");
const prevBtn =document.getElementById("prevBtn");
const scrollAmount =300;
nextBtn.addEventListener("click", () => {
    slider.scrollLeft += scrollAmount;
});
prevBtn.addEventListener("click", () => {
    slider.scrollLeft -= scrollAmount;
});