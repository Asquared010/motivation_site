from django.shortcuts import render, redirect
from .models import MotivationEntry

# This view handles the home page where users submit their motivation entries.
# It supports both displaying the form (GET request) and processing form submissions (POST request).
def home(request):

    # If the user submits the form, process the incoming data
    if request.method == "POST":
        
        # Retrieve user input from the submitted form
        name = request.POST.get("name")
        message = request.POST.get("message")

        # Create and save a new MotivationEntry object in the database
        MotivationEntry.objects.create(
            name=name,
            message=message
        )

        # Redirect the user to the list page after saving data
        return redirect("list")

    # If request is GET, simply display the home page form
    return render(request, "tracker/home.html")


# This view displays all saved motivation entries from the database.
# Entries are ordered from newest to oldest based on creation time.
def list_entries(request):
    
    # Fetch all entries from the database and sort them in descending order
    entries = MotivationEntry.objects.all().order_by("-created_at")

    # Pass the entries into the template for rendering
    return render(request, "tracker/list.html", {"entries": entries})