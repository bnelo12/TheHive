'use strict';

document.addEventListener('DOMContentLoaded', init);

function init() {
    const loginForm = document.getElementById('login-form-submit');
    if (loginForm) loginForm.addEventListener('click', handleLogin);

    const logoutButton = document.getElementById('logoutButton');
    if (logoutButton) logoutButton.addEventListener('click', handleLogout);
}

function getSignUpFormInfo() {
    const emailEl = document.getElementById("signup-email-form");
    const passwordEl = document.getElementById("signup-password-form");
    const passwordConfirmEl = document.getElementById("signup-confirm-password-form");
    const email = emailEl.value;
    const password = passwordEl.value;
    const passwordConfirm = passwordConfirmEl.value;
    return { email: email, password: password };
}

function getLoginFormInfo() {
    const emailEl = document.getElementById("emailInput");
    const passwordEl = document.getElementById("passwordInput");
    const email = emailEl.value;
    const password = passwordEl.value;
    return { email: email, password: password };
}

function handleLogin() {
    let userInfo = getLoginFormInfo()
    $.post({ 
        url: "/api/user/login",
        data: JSON.stringify(getLoginFormInfo()),
        type: "POST",
        contentType: "application/json",
        success: (_) => {
            window.location.href = "/";
        },
        error: (error) => {
            alert(error.responseText);
        }
    });
}

function handleLogout() {
    document.cookie = 'username=;expires=Thu, 01 Jan 1970 00:00:01 GMT';
    window.location.href = "/";
}

function handleSignUp() {
    let userInfo = getSignUpFormInfo()
    $.post({ 
        url: "/api/user/signup",
        data: JSON.stringify(userInfo),
        type: "POST",
        contentType: "application/json",
        success: (_) => {
            window.location.href = "/";
        },
        error: (error) => {
            console.log(error)
            alert(error.responseText);
        }
    });
}
