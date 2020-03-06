from django.shortcuts import render, redirect


# is_authenticated - used in template or view for user auth status logic
# the user object is always present in the template context
def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')
    else:
        return render(request, 'tictactoe/welcome.html')
