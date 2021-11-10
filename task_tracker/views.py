from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.forms.models import inlineformset_factory
from .models import Task, TaskChekList
from .forms import TaskForm


# Список задач
class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'task_tracker/task/list.html'
    model = Task
    context_object_name = 'tasks'


# Mixin задачи
class TaskEditMixin(LoginRequiredMixin):
    template_name = 'task_tracker/task/form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_tracker:task_list')

    # formset
    def __get_task_formset(self, data=None):
        TaskFormSet = inlineformset_factory(
            Task,
            TaskChekList,
            fields=['title', 'is_completed'],
            extra=1, can_delete=True)
        return TaskFormSet(
            instance=self.object, data=data)

    def form_valid(self, form):
        task_formset = self.__get_task_formset(
            data=self.request.POST)
        if task_formset.is_valid():
            task_checklists = task_formset.save(
                commit=False
            )
            for task_checklist in task_checklists:
                task_checklist.task = form.instance
                task_checklist.save()
            task_deleted_objects = task_formset.deleted_objects
            for task_deleted in task_deleted_objects:
                task_deleted.delete()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_formset'] = self.__get_task_formset()
        return context


# Создание задачи
class TaskCreateView(TaskEditMixin, CreateView):
    pass


# Обновление задачи
class TaskUpdateView(TaskEditMixin, UpdateView):
    pass
