from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.


def home(request):


    if request.method == "POST":

        print(request.FILES)
        myfiles = request.FILES.getlist('files')
        
        fs = FileSystemStorage()

        
        if fs.exists("Kunal"):
            files = fs.listdir("Kunal")[1]

            for f in files:
                fs.delete(f"Kunal/{f}")

        for file in myfiles:


            filename = fs.save(f"Kunal/{file.name}", file)

    return render(request,"home.html")