from django.shortcuts import redirect, render
from django.views.generic import View

from .users.forms import UserCreationForm


class MultiFormsView(View):

    "generic view which manage several forms"
    template_name = None
    form_classes = None
    success_url = None

    def get_forms(self):
        return [form(self.request.POST or None) for form in self.form_classes]

    def render_to_response(self, **context):
        return render(
            self.request,
            self.template_name,
            context,
        )

    def all_valid(self):
        "return True if all forms are valid"
        if all(form.is_valid() for form in self.forms):
            return True
        return False

    def form_valid(self):
        "what to do if all forms are valid"
        return redirect(str(self.success_url))


class HomeView(MultiFormsView):
    "View which manage the home page"


home_view = HomeView.as_view()
