
// let searchBtn = document.querySelector('#search-btn');
// let searchBar = document.querySelector('.search-bar-container');
let formBtn = document.querySelector('#login-btn');
let loginForm = document.querySelector('.login-form-1');
let formClose = document.querySelector('#form-close');
let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');
let videoBtn = document.querySelectorAll('.vid-btn');
let sign_up_button = document.querySelector('#sign-up-button');
let sign_up_form_container = document.querySelector('.sign-up-form-container');
let signUpform_close = document.querySelector('#signUpform-close');
let send_otp = document.querySelector('.send-otp');
// let login_success = document.querySelector('.login-success');
let userLogout = document.querySelector('#userLogout');
let login = document.querySelector('#login');
let login_form_container = document.querySelectorAll('.login-form-container');


window.onscroll = () => {
    // searchBtn.classList.remove('fa-times');
    // searchBar.classList.remove('active');
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
    loginForm.classList.remove('active');
    sign_up_form_container.classList.remove('active');
    // login_success.classList.remove('active');
    document.querySelector('.my-booking').classList.remove('active');

}

menu.addEventListener('click', () => {
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
});

// searchBtn.addEventListener('click', () => {
//     searchBtn.classList.toggle('fa-times');
//     searchBar.classList.toggle('active');
// });

formBtn.addEventListener('click', () => {
    loginForm.classList.add('active');
});

function activeLogin() {
    loginForm.classList.add('active');


}

formClose.addEventListener('click', () => {
    login_form_container[0].classList.remove('active');
    login_form_container[1].classList.remove('active');
    login_form_container[2].classList.remove('active');
});

sign_up_button.addEventListener('click', () => {
    loginForm.classList.remove('active');
    // loginForm.classList.add('active');
    sign_up_form_container.classList.add('active');

});

function cancle_msg(event) {
    let ptr = event.parentElement;
    ptr.style.display = 'none';
}





videoBtn.forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelector('.controls .active').classList.remove('active');
        btn.classList.add('active');
        let src = btn.getAttribute('data-src');
        document.querySelector('#video-slider').src = src;
    });
});

var swiper = new Swiper(".review-slider", {
    spaceBetween: 20,
    loop: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    breakpoints: {
        640: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    },
});

var swiper = new Swiper(".brand-slider", {
    spaceBetween: 20,
    loop: true,
    autoplay: {
        delay: 2500,
        disableOnInteraction: false,
    },
    breakpoints: {
        450: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 3,
        },
        991: {
            slidesPerView: 4,
        },
        1200: {
            slidesPerView: 5,
        },
    },
});

