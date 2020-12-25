from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm


@user_passes_test(lambda user: user.is_superuser)
@user_passes_test(lambda user: user.is_staff)
def index(request):
    return render(request, 'adminapp/index.html')



class UserListViews(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(UserListViews, self).dispatch(*args, **kwargs)



class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    form_class = UserAdminRegisterForm

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Создание пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(UserCreateView, self).dispatch(*args, **kwargs)



class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url =  reverse_lazy('admin_staff:admin_users')
    form_class = UserAdminProfileForm

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Редактирование пользователя'
        return context


    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(*args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_remove(request, user_id):
#     user = User.objects.get(id=user_id)
#     # user.delete() - (Пометка для себя) если нужно удалить полностью пользователя
#     user.is_active = False  # - за комментить
#     user.save()  # - за комментить
#     return HttpResponseRedirect(reverse('admin_staff:admin_users'))
