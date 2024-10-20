document.querySelector(".choose_size").addEventListener("click", function(e) {
    const o = e.target.closest('.cs_card')
    if (!o) return
    this.querySelectorAll(".active_size_btn").forEach(o => o.classList.remove("active_size_btn"))
    o.classList.add("active_size_btn");
});


/* Когда пользователь нажимает на кнопку, переключаться раскрывает содержимое */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}
  
// Закрыть раскрывающийся список, если пользователь щелкнет за его пределами.
window.onclick = function(event) {
if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
    var openDropdown = dropdowns[i];
    if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
    }
    }
}
}
