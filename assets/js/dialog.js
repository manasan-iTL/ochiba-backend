const modalButton = document.getElementById("modalButton");
const modal = document.getElementById("modal");
const close = document.getElementById("close");

modalButton.addEventListener('click', showmodal);
close.addEventListener('click', function(e) {
    e.preventDefault();
    modal.classList.add('deactive')
});

function showmodal() {
    modal.classList.toggle('deactive')
}
