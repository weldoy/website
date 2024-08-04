// // Открыть модальное окно
// document.getElementById("open-modal-btn").addEventListener("click", function() {
//     document.getElementById("my-modal").classList.add("open")
// })

// // Закрыть модальное окно
// document.getElementById("close-my-modal-btn").addEventListener("click", function() {
//     document.getElementById("my-modal").classList.remove("open")
// })

// // Закрыть модальное окно при нажатии на Esc
// window.addEventListener('keydown', (e) => {
//     if (e.key === "Escape") {
//         document.getElementById("my-modal").classList.remove("open")
//     }
// });

// // Закрыть модальное окно при клике вне его
// document.querySelector("#my-modal .modal__box").addEventListener('click', event => {
//     event._isClickWithInModal = true;
// });
// document.getElementById("my-modal").addEventListener('click', event => {
//     if (event._isClickWithInModal) return;
//     event.currentTarget.classList.remove('open');
// });

document.querySelector(".choose_size").addEventListener("click", function(e) {
    const o = e.target.closest('.cs_card')
    if (!o) return
    this.querySelectorAll(".active_size_btn").forEach(o => o.classList.remove("active_size_btn"))
    o.classList.add("active_size_btn");
});
