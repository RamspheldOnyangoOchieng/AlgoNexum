from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
   
def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,login.html,{"error:","invalid credentials"})
        return render(request,login.html)
    
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Id = request.POST['ID']
        user = user.objects.create_user(username=username, email=email, password=password, id=Id)
        if user.object.filter(username=username).exit():
            return render(request,register.html,{"error:","user already exists"})
        if user.object.filter(email=email).exit():
            return render(request,register.html,{"error:","email already exists"})
        user.save()
        return render(request,register.html,{"success:","user created successfully"})
    return render(request,"register.html")

def contact(request):
    return render(request,contact.html)

        
