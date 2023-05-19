let errorlists = document.querySelectorAll('.errorlist');
const email = document.getElementById('id_email');
const pass1 = document.getElementById('id_password1');
const pass2 = document.getElementById('id_password2');

let targetErrorlist;

for(let k=0; k < errorlists.length; k++) {
    if(errorlists[k].innerHTML !== "") {
        email.classList.add('validate-error');
        pass1.classList.add('validate-error')
        pass2.classList.add('validate-error')
    }
} 

