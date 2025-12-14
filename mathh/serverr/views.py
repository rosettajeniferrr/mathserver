from django.shortcuts import render

def home(request):
    power = ""
    intensity = ""
    resistance = ""

    if request.method == "POST":
        intensity = request.POST.get("intensity", "")
        resistance = request.POST.get("resistance", "")

        if intensity and resistance:
            I = float(intensity)
            R = float(resistance)
            power = (I ** 2) * R
        
        else:
             intensity = ""
             resistance = ""

    return render(request, "power.html", {
        "intensity": intensity,
        "resistance": resistance,
        "power": power
    })