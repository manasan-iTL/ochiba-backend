const editDeleteButton = document.getElementById("edit-delete")
console.log(editDeleteButton)

editDeleteButton.addEventListener("click", function (e) {
    let confirmWindow = window.confirm('本当に削除しても良いですか？')
    if (confirmWindow) {
        return true;
    } else {
        e.preventDefault();
    }
})