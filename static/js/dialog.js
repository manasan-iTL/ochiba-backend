const modalButton = document.getElementById("modalButton");
const modal = document.getElementById("modal");
const close = document.getElementById("close");

modalButton.addEventListener('click', showmodal);
close.addEventListener('click', function(e) {
    e.preventDefault();
    console.log("close")
    modal.classList.add('deactive')
});

function showmodal() {
    console.log("Click");
    modal.classList.toggle('deactive')
}
