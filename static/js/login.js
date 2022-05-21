let username = document.getElementById('name')
let email = document.getElementById('username')
let csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')

let password = document.getElementById('password');
let rePassword = document.getElementById('rePassword');
let smtBtn = document.getElementById('smtBtn');
let wPass = document.getElementById('wPass');
let smtBtn_otp = document.getElementById('smtBtn-otp');
let otp_value = document.getElementById('otp-value');
let success01 = document.getElementById('success01');
let lg_username = document.getElementById('lg-username')
let lg_password = document.getElementById('ig-password')


wPass.style.visibility = 'hidden';


function checkPassword() {
    if (password.value === rePassword.value && rePassword.value != "") {
        rePassword.style.boxShadow = "0 0 20px green";
        wPass.style.visibility = 'hidden';
        smtBtn.disabled = false;

    } else {
        // wPass.innerText = "Incorrect Password";
        wPass.style.visibility = 'visible';
        rePassword.style.boxShadow = "0 0 20px red";
        smtBtn.disabled = true;
    }

}

var sendData;

smtBtn.addEventListener('click', () => {
    sendData = {
        'name': username.value,
        'username': email.value,
        'password': password.value,
    }
    if (username.value == '' || email.value == '' || password.value == '' || rePassword.value == '') {
        alert('Please fill The Details')
    }
    else {
        let url01 = new URL(document.location.origin + '/sendotp');
        url01.search = new URLSearchParams(sendData).toString();

        fetch(url01)
            .then(res => res.json())
            .then(res => {
                console.table(res);
                sign_up_form_container.classList.remove('active');
                send_otp.classList.add('active');
            })
            .catch(alert('Internal server error'));
    }


})


smtBtn_otp.addEventListener('click', () => {
    sendData['otp'] = otp_value.value;

    let url01 = new URL(document.location.origin + '/singup');
    url01.search = new URLSearchParams(sendData).toString();

    fetch(url01)
        .then(res => res.json())
        .then(res => {
            send_otp.classList.remove('active');
            if (Object.keys(res)[0] == 'success') {
                // login_success.classList.add('active');
                alert('Login Success')
                document.getElementById('usernameSet').innerHTML = res['userName'] + '<br><a id="userLogout" href="logout">logout</a>';
                // success01.innerText = 'Login Success';
            }

            else {
                send_otp.classList.remove('active');
                sign_up_form_container.classList.add('active');
                alert('Check Your Email ID');
            }
            console.table(res);
        })

})


function showmybook(event) {
    document.getElementsByClassName('my-booking')[0].classList.add('active');
}