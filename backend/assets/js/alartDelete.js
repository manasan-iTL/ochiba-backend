const detailDeleteButton = document.getElementById("detail-delete")

detailDeleteButton.addEventListener("submit", function (e) {
    let confirmWindow = window.confirm('本当に削除しても良いですか？')
    if (confirmWindow) {
        return true;
    } else {
    
        e.preventDefault();
    }
})