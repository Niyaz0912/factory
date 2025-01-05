document.addEventListener("DOMContentLoaded", function() {
    // Устанавливаем фокус на поле "Специальная характеристика"
    const specialCharacteristicInput = document.querySelector('#specialCharacteristic');
    if (specialCharacteristicInput) {
        specialCharacteristicInput.focus();
    }

    // Функция для проверки диапазона специальной характеристики
    function validateSpecialCharacteristic(value) {
        const min = 21.95;
        const max = 22;
        return !isNaN(value) && value >= min && value <= max;
    }

    // Функция для добавления новой строки в таблицу
    function addRow() {
        const quantityInput = document.getElementById('quantity');
        let quantity = parseInt(quantityInput.value); // Преобразуем в число
        const roughness = document.querySelector('input[name="roughness"]:checked').value;
        const specialCharacteristic = parseFloat(specialCharacteristicInput.value); // Сохраняем текущее значение и преобразуем в число
        const appearance = document.querySelector('input[name="appearance"]:checked').value;
        const threadHole = document.querySelector('input[name="thread_hole"]:checked').value;
        const galtelSize = document.querySelector('input[name="galtel_size"]:checked').value;
        const controlCode = document.getElementById('controlCode') ? document.getElementById('controlCode').value : ''; // Проверка наличия поля
        const markYesNo = document.querySelector('input[name="mark_yes_no"]:checked').value;

        // Проверяем, что специальная характеристика введена и в диапазоне
        if (!validateSpecialCharacteristic(specialCharacteristic)) {
            alert("Пожалуйста, введите специальную характеристику в диапазоне от 21.95 до 22.");
            return; // Прерываем выполнение, если поле пустое или вне диапазона
        }

        // Создаем новую строку таблицы
        const newRow = `
            <tr>
                <td>${quantity}</td>
                <td>${roughness}</td>
                <td>${specialCharacteristic}</td>
                <td>${appearance}</td>
                <td>${threadHole}</td>
                <td>${galtelSize}</td>
                <td>${controlCode}</td>
                <td>${markYesNo}</td>
            </tr>`;

        // Добавляем строку в начало таблицы
        document.getElementById('parametersTableBody').insertAdjacentHTML('afterbegin', newRow);

        // Очищаем поле "Специальная характеристика"
        specialCharacteristicInput.value = '';

        // Увеличиваем количество деталей на 30
        quantity += 30;
        quantityInput.value = quantity;

        // Устанавливаем фокус на поле "Специальная характеристика"
        specialCharacteristicInput.focus();
    }

    // Обработка нажатия клавиши "Enter" в поле "Специальная характеристика"
    specialCharacteristicInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault(); // Предотвращаем стандартное поведение формы
            addRow(); // Вызываем функцию добавления строки
        }
    });

    // Обработка нажатия кнопки "Новый замер"
    document.getElementById('addMeasurementButton').addEventListener('click', function() {
        console.log("Кнопка 'Новый замер' нажата"); // Отладочное сообщение
        addRow(); // Вызываем функцию добавления строки
    });

   // Проверка диапазона при потере фокуса
specialCharacteristicInput.addEventListener('blur', function() {
    let value = parseFloat(this.value);

    if (!validateSpecialCharacteristic(value)) {
        alert(`Пожалуйста, введите значение в диапазоне от 21.95 до 22.`);
        this.value = ''; // Очищаем поле
        this.focus(); // Возвращаем фокус на поле
    } else {
        // Округляем значение до трех знаков после запятой и обновляем поле
        this.value = value.toFixed(3);
    }
});

