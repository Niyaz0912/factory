// scripts.js
document.addEventListener("DOMContentLoaded", function() {
    // Устанавливаем фокус на поле "Значение специальной характеристики"
    document.querySelector('input[name="special_characteristic"]').focus();

    // Пример добавления динамики (например, обработка события)
    const radioButtons = document.querySelectorAll('input[type=radio]');

    radioButtons.forEach(radio => {
        radio.addEventListener('change', function() {
            console.log(`Выбрано значение: ${this.value}`);
        });
    });
});
