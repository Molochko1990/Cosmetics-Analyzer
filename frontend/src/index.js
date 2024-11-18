function toggleProfileMenu() {
    const menu = document.getElementById("profile-menu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

function openLoginModal() {
    document.getElementById("auth-modal").style.display = "block";
    document.getElementById("overlay").style.display = "block";
    toggleProfileMenu();
}

function closeAuthModal() {
    document.getElementById("auth-modal").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}

function openRegisterModal() {
    document.getElementById("register-modal").style.display = "block";
    document.getElementById("overlay").style.display = "block";
    toggleProfileMenu();
}

function closeRegisterModal() {
    document.getElementById("register-modal").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}

function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    alert("Добро пожаловать, " + username + "!");
    closeAuthModal();
}

function register() {
    const lastname = document.getElementById("lastname").value;
    const firstname = document.getElementById("firstname").value;
    const middlename = document.getElementById("middlename").value;
    const username = document.getElementById("register-username").value;
    const password = document.getElementById("register-password").value;
    alert("Регистрация прошла успешно, " + firstname + "!");
    closeRegisterModal();
}

function toggleTextBar() {
    const textBar = document.getElementById("text-bar");
    textBar.style.display = textBar.style.display === "none" ? "block" : "none";
}

function submitText() {
    const textArea = document.getElementById("text-area");
    const successMessage = document.getElementById("success-message");
    successMessage.innerText = "Состав успешно отправлен: " + textArea.value;
    textArea.value = "";
    alert("Спасибо! Состав отправлен.");
}

function notWorking() {
    alert("Извините, эта функция пока не работает.");
}
