function toggleProfileMenu() {
    const menu = document.getElementById("profile-menu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

function openLoginModal() {
    document.getElementById("auth-modal").style.display = "block";
    toggleProfileMenu();
}

function closeAuthModal() {
    document.getElementById("auth-modal").style.display = "none";
}

function openRegisterModal() {
    document.getElementById("register-modal").style.display = "block";
    toggleProfileMenu();
}

function closeRegisterModal() {
    document.getElementById("register-modal").style.display = "none";
}

function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    if (username && password) {
        alert("Вы успешно вошли!");
        closeAuthModal();
    } else {
        alert("Пожалуйста, введите имя пользователя и пароль.");
    }
}

function register() {
    alert("Регистрация прошла успешно!");
    closeRegisterModal();
}

function toggleTextBar() {
    const textBar = document.getElementById("text-bar");
    textBar.style.display = textBar.style.display === "none" ? "block" : "none";
}

function submitText() {
    const text = document.getElementById("text-area").value;  // Получаем текст из textarea

    if (!text) {
        alert("Пожалуйста, введите состав косметики.");
        return;
    }

    // Формируем данные для отправки
    const formData = new FormData();
    formData.append('text', text);

    // Убедитесь, что путь правильный (например, сервер работает на http://127.0.0.1:8000)
    fetch("http://127.0.0.1:8000/submit-text/", {
        method: "POST",
        body: formData,
    })
        .then(response => {
            // Проверяем, что ответ успешен
            if (!response.ok) {
                return response.json().then(err => { throw new Error(err.Error || 'Ошибка отправки текста'); });
            }
            return response.json();  // Парсим JSON
        })
        .then(data => {
            console.log(data);  // Просмотр данных из ответа
            // Проверяем, что ключ 'Состав' существует в ответе
            if (data && data['Состав']) {
                const composition = data['Состав'];
                document.getElementById('success-message').textContent = `Состав: ${composition}`;
            } else {
                document.getElementById('success-message').textContent = 'Не удалось получить состав.';
            }
        })
        .catch(error => {
            console.error(error);
            document.getElementById('success-message').textContent = `Ошибка: ${error.message}`;
        });
}

function triggerFileUpload() {
    document.getElementById("file-input").click();
}

function uploadImage() {
    const formData = new FormData();
    const fileInput = document.getElementById('file-input');
    const file = fileInput.files[0];

    // Проверка, что файл выбран
    if (!file) {
        alert("Пожалуйста, выберите файл.");
        return;
    }

    formData.append('file', file);

    fetch("http://127.0.0.1:8000/upload_image", {
        method: "POST",
        body: formData,
    })
        .then(response => {
            // Проверяем, что ответ успешен
            if (!response.ok) {
                return response.json().then(err => { throw new Error(err.Error || 'Ошибка загрузки файла'); });
            }
            return response.json(); // Парсим JSON
        })
        .then(data => {
            console.log(data); // Просмотр данных из ответа
            // Проверяем, что ключ 'Состав' существует в ответе
            if (data && data['Состав']) {
                const composition = data['Состав'];
                document.getElementById('success-message').textContent = `Состав: ${composition}`;
            } else {
                document.getElementById('success-message').textContent = 'Не удалось извлечь состав.';
            }
        })
        .catch(error => {
            console.error(error);
            document.getElementById('success-message').textContent = `Ошибка: ${error.message}`;
        });
}
