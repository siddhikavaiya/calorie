from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        weight = request.POST['weight']
        height = request.POST['height']
        age = request.POST['age']
        gender = request.POST['gender']
        print("weight: ",weight)
        print("height: ",height)
        print("age: ",age)
        print("gender: ",gender)
        if gender == 'male':
            result = 66.47 + (13.75 * int(weight)) + (5.003 * int(height)) - (6.755 * int(age))
            print(result,"######################")
            return render(request,'index.html',{'result':result})
        if gender == 'female':
            result = 655.1 + (9.563 * int(weight)) + (1.850 * int(height)) - (4.676 * int(age))
            print(result,"######################") 
            return render(request,'index.html',{'result':result})

    return render(request,'index.html')