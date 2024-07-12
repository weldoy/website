// Открыть модальное окно
document.getElementById("open-modal-btn").addEventListener("click", function() {
    document.getElementById("my-modal").classList.add("open")
})

// Закрыть модальное окно
document.getElementById("close-my-modal-btn").addEventListener("click", function() {
    document.getElementById("my-modal").classList.remove("open")
})

// Закрыть модальное окно при нажатии на Esc
window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.getElementById("my-modal").classList.remove("open")
    }
});

// Закрыть модальное окно при клике вне его
document.querySelector("#my-modal .modal__box").addEventListener('click', event => {
    event._isClickWithInModal = true;
});
document.getElementById("my-modal").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove('open');
});

var size_btn = document.getElementById("sizebtn1");
size_btn.addEventListener("click", function() {
  this.classList.add("active_size_btn");
});

var size_btn = document.getElementById("sizebtn2");
size_btn.addEventListener("click", function() {
  this.classList.add("active_size_btn");
});

var size_btn = document.getElementById("sizebtn3");
size_btn.addEventListener("click", function() {
  this.classList.add("active_size_btn");
});

var size_btn = document.getElementById("sizebtn4");
size_btn.addEventListener("click", function() {
  this.classList.add("active_size_btn");
});

var size_btn = document.getElementById("sizebtn5");
size_btn.addEventListener("click", function() {
  this.classList.add("active_size_btn");
});
