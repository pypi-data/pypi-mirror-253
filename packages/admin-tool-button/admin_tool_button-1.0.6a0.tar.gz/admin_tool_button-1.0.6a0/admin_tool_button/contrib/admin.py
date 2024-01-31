from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class ButtonActionAdmin(admin.ModelAdmin):

    button_actions = []

    change_list_template = 'admin_button_change_list.html'

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        if not self.has_view_or_change_permission(request):
            raise PermissionDenied()

        if request.method == 'POST' and (button_action :=  request.POST.get('button_action')):
            self._handle_button_action(button_action, request)
            return redirect(request.path)

        button_actions = self.get_button_actions()
        extra_context = extra_context or {}
        extra_context.update({
            'button_actions': [(name, desc) for func, name, desc in button_actions.values()]
        })
        return super().changelist_view(request, extra_context=extra_context)

    def get_button_actions(self):
        button_actions = [self.get_action(button_action) for button_action in self.button_actions]
        return {
            name: (func, name, desc)
            for (func, name, desc) in button_actions
        }

    def _handle_button_action(self, action_str: str, request):
        button_actions = self.get_button_actions()
        if not (button_action := button_actions.get(action_str)):
            return

        button_action[0](self, request)
