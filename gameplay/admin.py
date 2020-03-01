# localhost:8000/admin
# to login first run: python manage.py createsuperuser
from django.contrib import admin

from .models import Game, Move


admin.site.register(Move)

# the __str__ method can be used to add more settings than the default ones
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # which fields of the Game model to display
    list_display = ('id', 'first_player', 'second_player', 'status')
    # which fields of the Game model are editable
    list_editable = ('status',)
