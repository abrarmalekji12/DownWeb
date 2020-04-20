from django.shortcuts import render,HttpResponse,redirect
import os
import django.core.files.storage as fs
from DownWeb import settings
# Create your views here.
class Desc :
    name:str
    dup:str 
    def __init__(self,n,d):
        self.name=n
        self.dup=d
def home(req) :
    main = fs.FileSystemStorage()
    dirs,files=main.listdir("")
    des=[]
    for file in files :
        des.append(Desc(file,str(file).replace(".","_dot_")))
    return render(req,'camtest.html',{'data':des})
def download(req,title:str) :
    file_path = os.path.join(settings.MEDIA_ROOT,title.replace("_dot_","."))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return redirect("/")

def upload(req) :
    myfile=req.FILES['myfile']
    main=fs.FileSystemStorage()
    name=main.save(myfile.name,myfile)
    return HttpResponse("ok {0}".format(len))
    