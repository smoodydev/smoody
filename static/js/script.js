// Nav Bar
window.addEventListener("scroll", function () {
    var header = document.querySelector("nav");
    header.classList.toggle("sticky", window.scrollY > 0);
});

$("#nav-toggle").click(function (d) {
    $("#nav-list").toggleClass("show");
})

$(".wrapper").click(function(d){
    $("#nav-list").removeClass("show");
});