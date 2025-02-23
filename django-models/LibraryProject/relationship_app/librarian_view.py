from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class LibrarianView(UserPassesTestMixin, TemplateView):
    template_name = 'relationship_app/librarian_view.html'

    def test_func(self):
        return self.request.user.userprofile.role == 'Librarian'
