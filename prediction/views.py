from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages framework
from .models import GameData, Game
import csv
from django.http import HttpResponse
from .forms import CSVUploadForm


def index_func(request):
    res = 0  # Placeholder for result
    if request.method == 'POST':
        if request.POST.get('pred_button'):
            # Get form data
            name = request.POST.get('Name')
            yor = request.POST.get('yor')
            NA = request.POST.get('NA')
            EU = request.POST.get('EU')
            JP = request.POST.get('JP')
            score = request.POST.get('score')
            critic_count = request.POST.get('critic_count')
            user_count = request.POST.get('user_count')
            console = request.POST.get('console')
            dev = request.POST.get('dev')
            rate = request.POST.get('rate')
            pub = request.POST.get('pub')

            # Save form data to database
            game = GameData(
                name=name,
                year_of_release=int(yor),
                na_sales=float(NA),
                eu_sales=float(EU),
                jp_sales=float(JP),
                critic_score=float(score),
                critic_count=int(critic_count),
                user_count=int(user_count),
                console=console,
                developer=dev,
                rating=rate,
                publisher=pub
            )
            game.save()  # Save to database

            messages.success(request, "Data has been successfully submitted!")  # Success message
            return redirect('homepage')  # Redirect to clear form
    return render(request, 'index.html', {'result': res})



def export_to_csv(request):
    # Create the HttpResponse object with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="game_data.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    
    # Write the header row
    writer.writerow(['ID', 'Name', 'Year of Release', 'NA Sales', 'EU Sales', 'JP Sales', 'Critic Score', 'Critic Count', 'User Count', 'Console', 'Developer', 'Rating', 'Publisher'])

    # Write data rows from the database
    for game in GameData.objects.all():
        writer.writerow([game.id, game.name, game.year_of_release, game.na_sales, game.eu_sales, game.jp_sales, 
                         game.critic_score, game.critic_count, game.user_count, game.console, game.developer, game.rating, game.publisher])

    return response



def upload_csv(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode("utf-8").splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:
                Game.objects.create(
    name=row["Name"],
    platform=row["Platform"],
    year_of_release=int(row["Year_of_Release"]) if row["Year_of_Release"] and isinstance(row["Year_of_Release"], (int, float)) else None,
    genre=row["Genre"],
    publisher=row["Publisher"],
    na_sales=float(row["NA_Sales"]) if row["NA_Sales"] and isinstance(row["NA_Sales"], (int, float)) else None,
    eu_sales=float(row["EU_Sales"]) if row["EU_Sales"] and isinstance(row["EU_Sales"], (int, float)) else None,
    jp_sales=float(row["JP_Sales"]) if row["JP_Sales"] and isinstance(row["JP_Sales"], (int, float)) else None,
    other_sales=float(row["Other_Sales"]) if row["Other_Sales"] and isinstance(row["Other_Sales"], (int, float)) else None,
    global_sales=float(row["Global_Sales"]) if row["Global_Sales"] and isinstance(row["Global_Sales"], (int, float)) else None,
    critic_score=float(row["Critic_Score"]) if row["Critic_Score"] and isinstance(row["Critic_Score"], (int, float)) else None,
    critic_count=int(row["Critic_Count"]) if row["Critic_Count"] and isinstance(row["Critic_Count"], (int, float)) else None,
    user_score=float(row["User_Score"]) if row["User_Score"] and isinstance(row["User_Score"], (int, float)) else None,
    user_count=int(row["User_Count"]) if row["User_Count"] and isinstance(row["User_Count"], (int, float)) else None,
    developer=row["Developer"],
    rating=row["Rating"],
)


            messages.success(request, "CSV file imported successfully!")
            return redirect("upload_csv")

    else:
        form = CSVUploadForm()
    
    return render(request, "upload_csv.html", {"form": form})


def export_games_to_csv(request):
    # Create the HTTP response with CSV content type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="games_data.csv"'

    # Create a CSV writer
    writer = csv.writer(response)
    
    # Write the header row
    writer.writerow([
        "Name", "Platform", "Year of Release", "Genre", "Publisher",
        "NA Sales", "EU Sales", "JP Sales", "Other Sales", "Global Sales",
        "Critic Score", "Critic Count", "User Score", "User Count",
        "Developer", "Rating"
    ])

    # Fetch data from the Game model
    games = Game.objects.all()

    # Write data rows
    for game in games:
        writer.writerow([
            game.name, game.platform, game.year_of_release, game.genre, game.publisher,
            game.na_sales, game.eu_sales, game.jp_sales, game.other_sales, game.global_sales,
            game.critic_score, game.critic_count, game.user_score, game.user_count,
            game.developer, game.rating
        ])

    return response


def game_list(request):
    games = Game.objects.all()
    return render(request, 'games_list.html', {'games': games})