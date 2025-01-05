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
    alert("Добро пожаловать, " + username + "!");
    closeAuthModal();
}

function register() {
    const firstname = document.getElementById("firstname").value;
    alert("Регистрация прошла успешно, " + firstname + "!");
    closeRegisterModal();
}

function toggleTextBar() {
    const textBar = document.getElementById("text-bar");
    textBar.style.display = textBar.style.display === "none" ? "block" : "none";
}

async function submitText() {
    const textArea = document.getElementById("text-area");
    const successMessage = document.getElementById("success-message");

    if (textArea.value.trim() === "") {
        alert("Пожалуйста, введите состав перед отправкой.");
        return;
    }

    // Отправляем текст на сервер
    try {
        const response = await fetch("http://localhost:8000/process-user-input/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text: textArea.value,  // Изменено на "text"
            }),
        });

        if (response.ok) {
            const data = await response.json();

            // Заполняем блоки данными, полученными от сервера
            document.getElementById("block1-content").innerText = data.block1 || "Нет данных";
            document.getElementById("block2-content").innerText = data.block2 || "Нет данных";
            document.getElementById("block3-content").innerText = Array.isArray(data.block3)
                ? data.block3.join("\n")
                : "Нет данных";

            // Показываем блоки
            document.getElementById("block1").style.display = "block";
            document.getElementById("block2").style.display = "block";
            document.getElementById("block3").style.display = "block";

            // Можно показать сообщение об успешной отправке, если нужно
            successMessage.style.display = "block";

        } else {
            alert("Ошибка при отправке данных.");
        }
    } catch (error) {
        console.error("Ошибка при отправке текста:", error);
        alert("Произошла ошибка при отправке текста.");
    }
}

// Инициализация событий на загрузке страницы
document.addEventListener("DOMContentLoaded", function () {
    const uploadButton = document.getElementById("upload-button");
    const fileInput = document.getElementById("image-upload");
    const submitButton = document.getElementById("submit-button"); // кнопка отправки текста

    // Открываем диалог выбора файла при клике на кнопку
    uploadButton.addEventListener("click", function () {
        fileInput.click();
    });

    // Автоматическая загрузка изображения после выбора файла
    fileInput.addEventListener("change", function () {
        if (fileInput.files.length === 0) {
            alert("Файл не выбран. Попробуйте ещё раз.");
            return;
        }
        uploadImage();
    });

    // Добавляем обработчик для кнопки отправки текста
    submitButton.addEventListener("click", submitText);
});


async function uploadImage() {
    const fileInput = document.getElementById("image-upload");
    const file = fileInput.files[0];

    if (!file) {
        alert("Пожалуйста, выберите изображение.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://localhost:8000/upload-image/", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            const data = await response.json();

            // Заполняем блоки данными
            document.getElementById("block1-content").innerText = data.block1 || "Нет данных";
            document.getElementById("block2-content").innerText = data.block2 || "Нет данных";
            document.getElementById("block3-content").innerText = Array.isArray(data.block3)
                ? data.block3.join("\n")
                : "Нет данных";

            // Показываем блоки
            document.getElementById("block1").style.display = "block";
            document.getElementById("block2").style.display = "block";
            document.getElementById("block3").style.display = "block";

        } else {
            alert("Ошибка загрузки изображения.");
        }
    } catch (error) {
        console.error("Ошибка при отправке изображения:", error);
        alert("Произошла ошибка при загрузке изображения.");
    }
}


function toggleBlock(blockId) {
    const block = document.getElementById(blockId);
    const content = block.querySelector('.block-content');
    const btn = block.querySelector('.toggle-btn');

    // Если контент скрыт, показываем его и меняем знак на стрелку вверх
    if (content.style.display === "none") {
        content.style.display = "block";
        btn.textContent = "⬆️";
    } else {
        content.style.display = "none";
        btn.textContent = "⬇️";
    }
}

