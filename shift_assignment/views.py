from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, ListView, DeleteView, CreateView

from .forms import ShiftAssignmentForm
from .models import ShiftAssignment
from users.models import UserRoles


class ShiftAssignmentListView(ListView):
    model = ShiftAssignment
    template_name = 'shift_assignment/shift_assignment_list.html'
    context_object_name = 'assignments'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.role in [UserRoles.MASTER, UserRoles.ADMIN]:
            queryset = queryset.filter(master=self.request.user)
        elif self.request.user.role == UserRoles.OPERATOR:
            queryset = queryset.filter(operator=self.request.user)
        return queryset


class ShiftAssignmentCreateView(CreateView):
    model = ShiftAssignment
    form_class = ShiftAssignmentForm
    template_name = 'shift_assignment/shift_assignment_create.html'  # Убедитесь, что путь указан правильно

    def form_valid(self, form):
        # Здесь можно добавить дополнительную логику перед сохранением формы, если необходимо
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('shift_assignment:list')


class ShiftAssignmentDetailView(DetailView):
    model = ShiftAssignment
    template_name = 'shift_assignment/shift_assignment_detail.html'
    context_object_name = 'assignment'


class ShiftAssignmentUpdateView(UpdateView):
    model = ShiftAssignment
    form_class = ShiftAssignmentForm
    template_name = 'shift_assignment/shift_assignments_update.html'
    success_url = reverse_lazy('users:profile_user')  # Перенаправление на профиль после успешного обновления


class ShiftAssignmentDeleteView(DeleteView):
    model = ShiftAssignment
    template_name = 'shift_assignment/shift_assignment_delete.html'  # Убедитесь, что путь указан правильно

    def get_success_url(self):
        return reverse_lazy('users:profile_user', kwargs={'pk': self.request.user.pk})
