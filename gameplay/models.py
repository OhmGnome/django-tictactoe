# The persisted objects that generate migrations
# Migration helps keep local dev and environment databases in sync (like java hibernate)
# by generating SQLs
# from the terminal: python manage.py has migration commands:
# migrate - is responsible for applying and unapplying migrations.
# makemigrations - is responsible for creating new migrations based on the changes you have made to your models.
# sqlmigrate - displays the SQL statements for a migration.
# showmigrations - lists a project’s migrations and their status.

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


GAME_STATUS_CHOICES = (
    ('F', 'First Player To Move'),
    ('S', 'Second Player To Move'),
    ('W', 'First Player Wins'),
    ('L', 'Second Player Wins'),
    ('D', 'Draw')
)


class GamesQuerySet(models.QuerySet):
    def games_for_user(self, user):
        return self.filter(
            Q(first_player=user) | Q(second_player=user)
        )

    def active(self):
        return self.filter(
            Q(status='F') | Q(status='S')
        )


@python_2_unicode_compatible
class Game(models.Model):
    first_player = models.ForeignKey(User,
                   related_name="games_first_player")
    second_player = models.ForeignKey(User,
                    related_name="games_second_player")

    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)

    # Django fields are not null by default
    # the "default" keyword is used to add populated rows to a table
    # default='F' - GAME_STATUS_CHOICES.F
    # choices - Django admin will show a dropdown for the possible game statuses
    status = models.CharField(max_length=1, default='F',
                              choices=GAME_STATUS_CHOICES)

    objects = GamesQuerySet.as_manager()

    def __str__(self):
        return "{0} vs {1}".format(
            self.first_player, self.second_player)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300)
    game = models.ForeignKey(Game)