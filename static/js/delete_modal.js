$(document).ready(function() {
    $('#deleteModal').on('show.bs.modal', function(event) {
        var button = $(event.relatedTarget); // Кнопка, которая открыла модальное окно
        var assignmentId = button.data('id'); // Получаем ID задания
        var actionUrl = '/shift_assignment/' + assignmentId + '/delete/'; // Создаем URL для удаления

        // Устанавливаем действие формы удаления
        $('#deleteForm').attr('action', actionUrl);
    });
});
