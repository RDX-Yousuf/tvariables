from django.shortcuts import render

def home(request):
    name='Raju'
    marks=[90,90,88,88,44]
    dict={'total':500,'obtained':400}

    percentage=(dict['obtained']/dict['total'])*100

    student={
        'percentage':percentage
    }


    return render(request, 'home.html',context={'name':name,'marks':marks,'dict':dict ,'student':student}) 