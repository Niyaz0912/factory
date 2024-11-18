from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView

from shift_assignment.models import ShiftAssignment
from .forms import ProcessHistoryForm
from .models import ProcessHistory
from users.models import UserRoles


class HomePageView(TemplateView):
    template_name = 'process_history/home.html'


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
