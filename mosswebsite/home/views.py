from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
import os
import subprocess

def run(cmd):

    proc = subprocess.Popen(cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
 
    return proc.returncode, stdout, stderr
 
def get_results_url(dict_map, lang):
    
    users = []

    #array of users
    for key in dict_map:
        users.append(key)

    stream = os.popen(f'media/moss.pl -l {lang} -d media/{users[0]}/* media/{users[1]}/*')
    output = stream.read()
    op = output.split("\n")
    print(op)
    url = op[len(op)-2]

    return url


def home(request):

   
   
    if request.method == "POST":

        #extract attributes from post request
        myfiles1 = request.FILES.getlist('files1')
        myfiles2 = request.FILES.getlist('files2')
        user1 = request.POST['user1']
        user2 = request.POST['user2']
        lang = request.POST['lang']

        print(lang)
        #create a dictionary of params
        dict_map = {}
        dict_map[user1] = myfiles1
        dict_map[user2] = myfiles2


        fs = FileSystemStorage()

        for key in dict_map:

            user  = key
            myfiles = dict_map[user]

            if fs.exists(user):
                files = fs.listdir(user)[1]

                for f in files:
                    fs.delete(f"{user}/{f}")

            for file in myfiles:
                filename = fs.save(f"{user}/{file.name}", file)

        res_url = get_results_url(dict_map,lang)
        return render(request,"home.html", {'result':res_url})

    return render(request,"home.html")