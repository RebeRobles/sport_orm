from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues":League.objects.filter(sport="Baseball"),
		"women_leagues":League.objects.filter(name__contains="women"),
		"all_hockey_leagues": League.objects.filter(sport__contains="hockey"),
		"not_football_leagues": League.objects.exclude(sport__contains="football"),
		"conferences_leagues": League.objects.filter(name__contains="conference"),
		"atlantic_leagues": League.objects.filter(name__contains="atlantic"),
		"dallas_teams":Team.objects.filter(location__contains="Utah"),
		"team_with_raptors": Team.objects.filter(team_name__contains="thunder"),
		"team_with_city": Team.objects.filter(location__contains="City"),
		"team_startwith_t": Team.objects.filter(team_name__startswith="T"),
		"team_orderby_location": Team.objects.all().order_by("location"),
		"team_orderby_name": Team.objects.all().order_by("-team_name"),
		"player_lastname_cooper": Player. objects.filter(last_name__contains="cooper"),
		"player_name_joshua": Player. objects.filter(first_name__contains="joshua"),
		"player_cooper_less_joshua": Player.objects.filter(last_name__contains="cooper").exclude(first_name__contains="joshua"),
		"player_name_alexander_or_wyatt": Player.objects.filter(first_name__in=["Alexander","Wyatt"]),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")