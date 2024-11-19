from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.core.exceptions import PermissionDenied

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


class ShiftAssignmentCreateView(LoginRequiredMixin, CreateView):
    model = ShiftAssignment
    form_class = ShiftAssignmentForm
    template_name = 'shift_assignment/shift_assignment_create.html'
    success_url = reverse_lazy('shift_assignment_list')

    def form_valid(self, form):
        if self.request.user.role not in [UserRoles.MASTER, UserRoles.ADMIN]:
            raise PermissionDenied("У вас нет прав для создания задания.")
        self.object = form.save()
        self.object.master = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    
class ShiftAssignmentDetailView(DetailView):
    model = ShiftAssignment
    template_name = 'shift_assignment/detail.html'
    context_object_name = 'assignment'


class ShiftAssignmentUpdateView(LoginRequiredMixin, UpdateView):
    model = ShiftAssignment
    template_name = 'shift_assignment/shift_assignment_create.html'
    extra_context = {
        'title': 'Редактирование сменного задания'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.master != self.request.user and self.request.user.role not in [UserRoles.MASTER,
                                                                                      UserRoles.ADMIN]:
            raise PermissionDenied("У вас нет прав для редактирования этого задания.")
        return self.object

    def get_success_url(self):
        return reverse('shift_assignment:assignments_list')

    def form_valid(self, form):
        if self.request.user.role not in [UserRoles.MASTER, UserRoles.ADMIN]:
            raise PermissionDenied("У вас нет прав для обновления задания.")
        self.object = form.save()
        return super().form_valid(form)


class ShiftAssignmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ShiftAssignment
    template_name = 'shift_assignment/shift_assignment_delete.html'
    success_url = reverse_lazy('shift_assignment:assignments_list')
    permission_required = 'shift_assignment.delete_shift_assignment'

    # permission_required = 'process_history.delete_process_history'
