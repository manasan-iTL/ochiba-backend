const email = document.getElementById('id_email');
const pass1 = document.getElementById('id_password1');
const pass2 = document.getElementById('id_password2');
let inputs = [];
inputs.push(email, pass1, pass2);


for(let j=0; j<inputs.length; j++) {
    if(inputs[j].validity.valid) {
        targetErrorlist = inputs[j].nextElementSibling;
        while(targetErrorlist.lastChild) {
            targetErrorlist.removeChild(targetErrorlist.lastChild);
        }
        targetErrorlist.innerHTML = '<li>OK</li>';

    }
}