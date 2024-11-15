from django.template.context_processors import request
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView

from .forms import ProcessHistoryForm, ShiftAssignmentForm
from .models import ShiftAssignment, ProcessHistory
from users.models import UserRoles


class HomePageView(TemplateView):
    template_name = 'process_history/home.html'


class ShiftAssignmentListView(LoginRequiredMixin, ListView):
    model = ShiftAssignment
    extra_context = {
        'title': 'Все ваши задания'
    }
    template_name = 'process_history/shift_assignment_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.role in [UserRoles.MASTER, UserRoles.ADMIN]:
            queryset = queryset.filter(master=self.request.user)
        elif self.request.user.role == UserRoles.OPERATOR:
            queryset = queryset.filter(operator=self.request.user)
        return queryset


class ShiftAssignmentCreateView(LoginRequiredMixin, CreateView):
    model = ShiftAssignment
    form = ShiftAssignmentForm
    template_name = 'process_history/shift_assignment_create_update.html'
    success_url = reverse_lazy('process_history:home')

    def form_valid(self, form):
        if self.request.user.role not in [UserRoles.MASTER, UserRoles.ADMIN]:
            raise PermissionDenied
        self.object = form.save()
        self.object.master = self.request.user
        self.object.save()


class ShiftAssignmentDetailView(LoginRequiredMixin, DetailView):
    model = ShiftAssignment
    template_name = 'process_history/shift_assignments_detail.html'
    extra_context = {
        'title': 'Ваше задание на смену'
    }


class ShiftAssignmentUpdateView(LoginRequiredMixin, UpdateView):
    model = ShiftAssignment
    template_name = 'process_history/shift_assignment_create_update.html'
    extra_context = {
        'title': 'Редактирование сменного задания'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.master != self.request.user and self.request.user.role not in [UserRoles.MASTER,
                                                                                      UserRoles.ADMIN]:
            raise PermissionDenied()
        return self.object

    def get_form_class(self):
        assignment_forms = {
            'admin': ShiftAssignmentForm,
            'master': ShiftAssignmentForm,
            'operator': ShiftAssignmentForm,
        }
        user_role = self.request.user.role
        assignment_form_class = assignment_forms[user_role]
        return assignment_form_class

    def get_success_url(self):
        return reverse('process_history:assignments_list')

    def form_valid(self, form):
        if self.request.user.role not in [UserRoles.MASTER, UserRoles.ADMIN]:
            raise PermissionDenied
        self.object = form.save()
        self.object.save()


class ShiftAssignmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ShiftAssignment
    template_name = 'process_history/assignment_delete.html'
    success_url = reverse_lazy('process_history:assignments_list')
    permission_required = 'shift_assignments.delete_shift_assignment'
    # permission_required = 'process_history.delete_process_history'

class HistoryProcessCreateView(LoginRequiredMixin, CreateView):
    model = ProcessHistory
    template_name = 'process_history/history_process_create.html'
    form_class = ProcessHistoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assignment_id = self.kwargs.get('assignment_id')
        context['assignment'] = ShiftAssignment.objects.get(id=assignment_id)
        return context

    def form_valid(self, form):
        process_history = form.save()
        if self.request.user.role not in [UserRoles.MASTER, UserRoles.ADMIN, UserRoles.OPERATOR]:
            raise PermissionDenied()
        process_history.user = self.request.user
        process_history.save()

        return super().form_valid(form)
