from django.shortcuts import render

# Home page
def home(request):
    return render(request, 'main/home.html')

# Result page
def result(request):
    name = request.GET.get('name')
    goal = request.GET.get('goal')

    message = f"Keep going {name}! You can achieve your goal of {goal}."

    return render(request, 'main/result.html', {
        'message': message
    })

# Tips page
def tips(request):
    tips_list = [
        "Study a little every day.",
        "Practice coding consistently.",
        "Take breaks to avoid burnout.",
        "Ask questions when confused."
    ]

    return render(request, 'main/tips.html', {
        'tips': tips_list
    })