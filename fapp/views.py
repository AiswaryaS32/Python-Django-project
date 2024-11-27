from django.shortcuts import render, redirect
from fapp.models import category,product
from webapp.models import contact
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime
from django.contrib import messages


# Create your views here.
def index(req):
    date = datetime.datetime.now()
    catno = category.objects.count()
    pdno = product.objects.count()
    return render(req, "index.html",{'date':date,'catno':catno,'pdno': pdno})

def addcat(req):
    return render(req, "addcategory.html")

def save_category(req):
    if req.method=='POST':
        nm = req.POST.get('cname')
        img = req.FILES['pic']
        de = req.POST.get('cdes')
        obj = category(ccname=nm, cimage=img ,cdesc=de)
        obj.save()
        messages.success( req,"Category saved...!")
        return redirect(addcat)

def viewcat(req):
    data = category.objects.all()
    return render(req,"viewcat.html",{'datas':data})

def deletecat(req,c_id):
    cat=category.objects.get(id=c_id)
    cat.delete()
    messages.success(req, "Category deleted...!")
    return redirect(viewcat)

def editcat(req,ca_id):
    cats = category.objects.get(id=ca_id)
    return render(req,"editcat.html",{'cats':cats})

def updatecat(req,cat_id):
    if req.method=="POST":
        nam = req.POST.get('cname')
        dess = req.POST.get('cdes')
        try:
            imgs = req.FILES['pic']
            fs = FileSystemStorage()
            file = fs.save(imgs.name,imgs)
        except MultiValueDictKeyError:
            file = category.objects.get(id=cat_id).cimage
        category.objects.filter(id=cat_id).update(ccname=nam, cdesc=dess, cimage=file)
        return redirect(viewcat)


def add_product(req):
    cats = category.objects.all()
    return render(req,"addpro.html",{'cats':cats})

def save_pro(req):
    if req.method == "POST":
        cnm = req.POST.get('pcat')
        pnm = req.POST.get('pname')
        pp = req.POST.get('pprice')
        quan = req.POST.get('quantity')
        ma = req.POST.get('man')
        co = req.POST.get('con')
        desr = req.POST.get('pdes')
        img1 = req.FILES['pimg1']
        img2 = req.FILES['pimg2']
        img3 = req.FILES['pimg3']
        obj = product(pcat=cnm,pname=pnm,pquan=quan,pprice=pp,pimage1=img1,pimage2=img2,pimage3=img3,pman=ma,coun=co,pdesc=desr)
        obj.save()
        messages.success(req,"Product saved..!")
        return redirect(add_product)

def viewpro(req):
    pro = product.objects.all()
    return render(req,"viewpro.html", {'pro':pro})

def deletepro(req,pd_id):
    pro=product.objects.get(id=pd_id)
    pro.delete()
    messages.success(req, "Product deleted...!")
    return redirect(viewpro)

def editpro(req,p_id):
    cat = category.objects.all()
    pros = product.objects.get(id=p_id)
    return render(req,"editpro.html",{'pros':pros,'cat':cat})


def updatepro(req,pr_id):
    if req.method=="POST":
        c = req.POST.get('pcat')
        p = req.POST.get('pname')
        pr = req.POST.get('pprice')
        qua = req.POST.get('quantity')
        man = req.POST.get('man')
        cor = req.POST.get('con')
        de = req.POST.get('pdes')

        try:
            img1 = req.FILES['pimg1']
            fs = FileSystemStorage()
            file1 = fs.save(img1.name,img1)
        except MultiValueDictKeyError:
            file1 = product.objects.get(id=pr_id).pimage1


        try:
            img2 = req.FILES['pimg2']
            fs = FileSystemStorage()
            file2 = fs.save(img2.name,img2)
        except MultiValueDictKeyError:
            file2 = product.objects.get(id=pr_id).pimage2


        try:
            img3 = req.FILES['pimg3']
            fs = FileSystemStorage()
            file3 = fs.save(img3.name,img3)
        except MultiValueDictKeyError:
            file3 = product.objects.get(id=pr_id).pimage3

        product.objects.filter(id=pr_id).update(pcat=c, pname=p, pquan=qua, pprice=pr, pimage1=file1, pimage2=file2, pimage3=file3, pman=man,coun=cor, pdesc=de)
        return redirect(viewpro)

def loginpage(req):
    return render(req,"adminlogin.html")

def adminlogin(req):
    if req.method== "POST":
        un =req.POST.get('username')
        ps =req.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username = un, password= ps)
            if user is not None:
                login(req,user)
                req.session['username'] = un
                req.session['password'] = ps
                messages.success(req, "Login Successfully!!")
                return redirect(index)
            else:
                messages.warning(req, "Incorrect password!!")
                return redirect(loginpage)
        else:
            messages.warning(req, "Invalid username!!")
            return redirect(loginpage)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully!!")
    return redirect(loginpage)

def display_contact(req):
    cont = contact.objects.all()
    return render(req,"display_contact.html",{'cont':cont})


def delete_contact(req,co_id):
    con = contact.objects.filter(id=co_id)
    con.delete()
    return redirect(display_contact)

