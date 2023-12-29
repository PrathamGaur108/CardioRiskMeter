from django.shortcuts import render
from .models import MLModel

def index(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, "AboutUs.html")

def prediction(request):
    return render(request, "Prediction.html")

def predicted(request):
    if request.method == "POST":
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        chestpain = request.POST.get("chestpain")
        restingbp = request.POST.get("restingbp")
        serumcholestrol = request.POST.get("serumcholestrol")
        fastingbs = request.POST.get("fastingbs")
        restingrelectro = request.POST.get("restingrelectro")
        maxheartrate = request.POST.get("maxheartrate")
        exerciseangia = request.POST.get("exerciseangia")
        oldpeak = request.POST.get("oldpeak")
        slope = request.POST.get("slope")
        majvessels = request.POST.get("noofmajvessels")
        mod = MLModel()
        target, accuracy = mod.model(age,gender,chestpain,restingbp,serumcholestrol,fastingbs,restingrelectro,maxheartrate,exerciseangia,oldpeak,slope,majvessels)
        data = {}
        data['age'] = age
        data['gender'] = gender
        data['chestpain'] = chestpain
        data['restingbp'] = restingbp
        data['serumcholestrol'] = serumcholestrol
        data['fastingbs'] = fastingbs
        data['restingrelectro'] = restingrelectro
        data['maxheartrate'] = maxheartrate
        data['exerciseangia'] = exerciseangia
        data['oldpeak'] = oldpeak
        data['slope'] = slope
        data['majvessels'] = majvessels
        data['result'] = target
        data['accuracy'] = accuracy
        return render(request, "Predicted.html", data)