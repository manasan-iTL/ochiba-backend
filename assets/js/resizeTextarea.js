const textareas = document.getElementsByTagName('textarea');


function resizeHeight(e) {
    if (this.textarea.scrollHeight < 200) {
         //高さを再設定している。これがないとinputイベントが発火するたびに高さが増えるため
         this.textarea.style.height = this.textarea.clientHeight + 'px';
         //高さをスクロールする高さ分大きくしている
         this.textarea.style.height = this.textarea.scrollHeight + 'px';
    }
}

for (let i=0; i < textareas.length; i++) {
    textareas[i].addEventListener('input', {textarea:textareas[i], handleEvent:resizeHeight});
}