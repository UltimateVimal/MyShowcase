from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def FileUploadHome(request):
    if request.method=='POST':
        uploaded_file=request.FILES['ctrlUserFile']
        fs=FileSystemStorage()
        filename_onserver=fs.save(uploaded_file.name,uploaded_file)
        file_url=fs.url(filename_onserver)
        return render(request,'sfu/sfu_home.html',{'FileUrl':file_url})
    else:
        return render(request,'sfu/sfu_home.html')
