import razorpay
from django.shortcuts import render, redirect
from fapp.models import product, category
from webapp.models import contact,signup_db,cartdb, orderdb
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

# Create your views here.
def homepage(req):
    ct = category.objects.all()
    cpd = cartdb.objects.filter(Uname=req.session['Username1'])
    cn = cpd.count()
    return render(req,"homepage.html",{'ct':ct,'cn':cn})

def product_page(req):
    pd = product.objects.all()
    return render(req,"product.html",{'pd':pd})

def contact_page(req):
    return render(req,"contact.html")

def about_page(req):
    return render(req,"about.html")

def product_filter(req,cat_name):
    pd = product.objects.filter(pcat=cat_name)  #like id=pro_id
    return render(req,"product_filter.html",{'pd':pd})

def save_contact(req):
    if req.method=="POST":
        nm = req.POST.get('name')
        em = req.POST.get('email')
        sub = req.POST.get('subject')
        msg = req.POST.get('message')
        obj = contact(Name=nm, Email=em, Subject=sub, Message=msg)
        obj.save()
        return redirect(contact_page)

def single_product(req,pro_id):
    pro = product.objects.get(id=pro_id)
    return render(req,"single_product.html",{'pro':pro})

def signup_page(req):
    return render(req,"signup.html")

def save_signup(req):
    if req.method =="POST":
        uname=req.POST.get('username1')
        con=req.POST.get('contact1')
        email=req.POST.get('email1')
        pass1 =req.POST.get('password1')
        pass2 =req.POST.get('password2')
        obj = signup_db(Username1=uname, Contact=con, Password1=pass1, Password2=pass2, Email=email)
        if signup_db.objects.filter(Username1=uname).exists():
            messages.warning(req,"User already exists !!")
            return redirect(signup_page)
        elif signup_db.objects.filter(Email=email).exists():
            messages.warning(req,"Email already exists")
            return redirect(signup_page)
        obj.save()
        messages.success(req, "Registered successfully!!")
        return redirect(login_page)

def login_page(req):
    return render(req,"login.html")

def userlogin(req):
    if req.method == "POST":
        un = req.POST.get('username3')
        ps = req.POST.get('password3')
        if signup_db.objects.filter(Username1=un, Password1=ps).exists():
            req.session['Username1'] = un
            req.session['Password1'] =ps
            messages.success(req,"Login successfully!!")
            return redirect(homepage)
        else:
            messages.success(req,"Incorrect password!")
            return redirect(login_page)
    else:
        messages.success(req,"Invalid credentials!")
        return redirect(login_page)

def logout(req):
    del req.session['Username1']
    del req.session['Password1']
    messages.success(req, "Logout successfully!!")
    return redirect(homepage)

def save_cart(req,pro_id):
    proid=product.objects.get(id=pro_id)
    if req.method =="POST":
        qt = req.POST.get('quantity')
        pn = req.POST.get('pdname')
        pr = req.POST.get('prices')
        uu = req.POST.get('uuname')
        tp = req.POST.get('total')
        try:
           x= product.objects.get(pname=pn)
           img = x.pimage1
        except product.DoesNotExist:
            img = None
        obj = cartdb(Quantity=qt,Product=pn,Price=pr,Tprice=tp,Uname=uu,Pro_Image=img)
        obj.save()
        return redirect(cart_page)

def cart_page(request):
    cpd = cartdb.objects.filter(Uname=request.session['Username1'])
    ct = cpd.count()
    subtotal=0
    shipping_amount=0
    total_amount=0
    for i in cpd:
        subtotal+=i.Tprice
    if subtotal > 50000:
        shipping_amount = 100
    else:
        shipping_amount=250
    total_amount = shipping_amount+subtotal
    return render(request,"cart_page.html",{'ct':ct,'cpd':cpd,'subtotal':subtotal,'shipping_amount':shipping_amount,'total_amount':total_amount})

def checkout_page(req):
    cpd = cartdb.objects.filter(Uname=req.session['Username1'])
    ct = cpd.count()
    subtotal = 0
    shipping_amount = 0
    total_amount = 0
    for i in cpd:
        subtotal += i.Tprice
    if subtotal > 50000:
        shipping_amount = 100
    else:
        shipping_amount = 250
    total_amount = shipping_amount + subtotal
    return render(req,"checkout.html",{'ct':ct,'cpd':cpd,'subtotal':subtotal,'shipping_amount':shipping_amount,'total_amount':total_amount})

def remove_cart(req,ct_id):
    rm = cartdb.objects.filter(id=ct_id)
    rm.delete()
    return redirect(cart_page)

def save_placeorder(req):
    if req.method =="POST":
        fn = req.POST.get('fname')
        ln = req.POST.get('lname')
        em = req.POST.get('email')
        co = req.POST.get('country')
        ad = req.POST.get('address')
        to = req.POST.get('town')
        zi = req.POST.get('zip')
        tt = req.POST.get('tprice')
        ph = req.POST.get('phone')
        cm = req.POST.get('comment')
        obj = orderdb(Fname=fn,Lname=ln,Country=co,Address=ad, Email=em,Town=to, Zip=zi, Phone=ph, Comment=cm, Total=tt)
        obj.save()
        return redirect(payment)

def payment(req):

    #Retrieve the data from the orderdb withthe specified id
    customer = orderdb.objects.order_by('-id').first()        #last entered user will be the first one #reverse using id

    #Get the payment amount of the specified customer
    payy=customer.Total

    #Convert the amount into paisa (Smallest currency unit)
    amount=int(payy*100)   #Assuming the payment amount in rupees

    payy_strr = str(amount)

    for i in payy_strr:
        print(i)

    if req.method=="POST":
        order_currency='INR'
        client = razorpay.Client(auth=('rzp_test_JvjyjpAbolAtIN','3C2SqhjMFLeQXytWTxgch5Go'))
        payment = client.order.create({'amount':amount,'currency':order_currency})

    return render(req,"payment.html",{'customer':customer,'payy_strr':payy_strr,})




    return render(req,"payment.html")