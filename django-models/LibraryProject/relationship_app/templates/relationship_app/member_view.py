from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin


class MemberView(UserPassesTestMixin, TemplateView):
    template_name = 'relationship_app/member_view.html'

    def test_func(self):
        return self.request.user.userprofile.role == 'Member'
