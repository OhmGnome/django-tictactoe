from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, new_invitation, accept_invitation, SignUpView


urlpatterns = [
    # name - URL alias should always be prefixed with the app name (player_home)
    url(r'home$', home, name="player_home"),
    url(r'login$',
        LoginView.as_view(template_name="player/login_form.html"),
        name="player_login"),
    url(r'logout$',
        # LogoutView - class based logout. LOGOUT_REDIRECT_URL is set in settings.py
        LogoutView.as_view(),
        name="player_logout"),
    url(r'new_invitation$', new_invitation, name="player_new_invitation"),
    # named group - example: (?P<id>\d+) - format (?P<name>regex)
    # use named group in the template like: <a href="{% url 'player_accept_invitation' id=inv.id %}">
    url(r'accept_invitation/(?P<id>\d+)/$',
        accept_invitation,
        name="player_accept_invitation"),
    url(r'signup$', SignUpView.as_view(), name='player_signup'),
]