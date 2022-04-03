console.log('Click');
let element = document.querySelectorAll('.is-validate');
let errorlists = document.querySelectorAll('.errorlist');
const email = document.getElementById('id_login');
const pass = document.getElementById('id_password');
const pass1 = document.getElementById('id_password1');
const pass2 = document.getElementById('id_password2');

console.log(errorlists);



for(let i=0; i < element.length; i++) {
    if(element[i].innerHTML !== "") {
        console.log('ok');
        email.classList.add('validate-error');
        pass.classList.add('validate-error');
        element[i].classList.add('error-text');
    }
}

for(let k=0; k < errorlists.length; k++) {
    if(errorlists[k].innerHTML !== "") {
        console.log('ok');
        email.classList.add('validate-error');
        pass1.classList.add('validate-error')
        pass2.classList.add('validate-error')
    }
} 