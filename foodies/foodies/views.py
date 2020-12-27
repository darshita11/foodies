import pyrebase
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

i1=''

config={
    'apiKey': "AIzaSyAzHxBdaAzMIAfc2QQmVMV3txrnOslJigU",
    'authDomain': "foodies-ece08.firebaseapp.com",
    'databaseURL': "https://foodies-ece08-default-rtdb.firebaseio.com",
    'projectId': "foodies-ece08",
    'storageBucket': "foodies-ece08.appspot.com",
    'messagingSenderId': "466114442489",
    'appId': "1:466114442489:web:0b5a2b53a4f1d21d3e9e28",
    'measurementId': "G-XEYB3QG1Z8"
  }

firebase=pyrebase.initialize_app(config)

db=firebase.database()
auth = firebase.auth()

def registration(HttpRequest):
    return render(HttpRequest,'registration.html')

def registrationdata(HttpRequest):
    firstname=HttpRequest.POST.get('inputfname')
    lastname=HttpRequest.POST.get('inputlname')
    email=HttpRequest.POST.get('inputEmail4')
    password=HttpRequest.POST.get('inputPassword')
    birhdate=HttpRequest.POST.get('inputdob')
    gender=HttpRequest.POST.get('inlineRadioOptions')
    address=HttpRequest.POST.get('inputAddress')
    city=HttpRequest.POST.get('inputCity')
    state=HttpRequest.POST.get('inputState')

    # db.child('users').set({'firstname':'abc'})
    #create id ...used push
    db.child('users').push({'FirstName':firstname,'LastName':lastname,'Email':email,'Password':password,'Date Of Birth':birhdate,'Gender':gender,'Address':address,'City':city,'State':state})
    auth.create_user_with_email_and_password(email,password)
    return HttpResponse(firstname)

def login(HttpRequest):
    return render(HttpRequest,'login.html')

def logindata(HttpRequest):
    email=HttpRequest.POST.get('inputEmail')
    password=HttpRequest.POST.get('inputPassword')
    try:
       a= auth.sign_in_with_email_and_password(email,password)
       auth.send_email_verification(a['idToken'])
       return HttpResponse('Login successfully')

    except:
        return HttpResponse('Invalid Email or Password')

def forgetpass(HttpRequest):
    return render(HttpRequest,'forgotpass.html')

def forgetdata(HttpRequest):
    email=HttpRequest.POST.get('inputEmail')
    auth.send_password_reset_email(email)
    return HttpResponse('verify')

def indexdata(HttpRequest):
    return render(HttpRequest,'index.html')

def formelement(HttpRequest):
    return render(HttpRequest,'basic_elements.html')

def formdataelement(HttpRequest):
    category=HttpRequest.POST.get('category')
    name=HttpRequest.POST.get('foodname')
    price=HttpRequest.POST.get('price')
    image=HttpRequest.POST.get('url')
    hotelname=HttpRequest.POST.get('hotelname')
    ingredients=HttpRequest.POST.get('ingrediants')

    db.child('fooddata').push({
        'category':category,'name':name,'price':price,'files':image,'hotelname':hotelname,'ingredients':ingredients
    })
    #showfooddetail(HttpRequest)
    return showfooddetail(HttpRequest)

def showfooddetail(HttpRequest):
    data=db.child('fooddata').shallow().get().val()

    datalist=[]
    for i in data:
        datalist.append(i)

    datalist.sort(reverse=True)
    # print(datalist)

    category=[]
    foodname=[]
    pric=[]
    imagefile=[]
    hotelnames=[]
    ingrediant=[]

    for i in datalist:
        cate=db.child('fooddata').child(i).child('category').get().val()
        category.append(cate)

        fname=db.child('fooddata').child(i).child('name').get().val()
        foodname.append(fname)

        pri=db.child('fooddata').child(i).child('price').get().val()
        pric.append(pri)

        image=db.child('fooddata').child(i).child('files').get().val()
        imagefile.append(image)

        hotelname=db.child('fooddata').child(i).child('hotelname').get().val()
        hotelnames.append(hotelname)

        ingrediants=db.child('fooddata').child(i).child('ingredients').get().val()
        ingrediant.append(ingrediants)

    # print("hh",category)
    # print("j",foodname)
    # print('k',pric)
    # print('jjk',imagefile)
    print('jk',hotelnames)
    print('jkk',ingrediant)

    showop=zip(category,foodname,pric,hotelnames,ingrediant,imagefile)
    print(showop)
    return render(HttpRequest,'showfooddetail.html',{'data':showop})

def adminedit(HttpRequest):
    data = db.child('fooddata').shallow().get().val()
    print(data)
    datalist = []
    for i in data:
        datalist.append(i)

    datalist.sort(reverse=True)
    # print(datalist)

    category = []
    foodname = []
    pric = []
    imagefile = []
    hotelnames = []
    ingrediant = []

    for i in datalist:
        cate = db.child('fooddata').child(i).child('category').get().val()
        category.append(cate)

        fname = db.child('fooddata').child(i).child('name').get().val()
        foodname.append(fname)

        pri = db.child('fooddata').child(i).child('price').get().val()
        pric.append(pri)

        image = db.child('fooddata').child(i).child('files').get().val()
        imagefile.append(image)

        hotelname = db.child('fooddata').child(i).child('hotelname').get().val()
        hotelnames.append(hotelname)

        ingrediants = db.child('fooddata').child(i).child('ingredients').get().val()
        ingrediant.append(ingrediants)

    # print("hh",category)
    # print("j",foodname)
    # print('k',pric)
    # print('jjk',imagefile)
    print('jk', hotelnames)
    print('jkk', ingrediant)

    showop = zip(category, foodname, pric, hotelnames, ingrediant, imagefile,datalist)
    print(showop)
    return render(HttpRequest, 'AdminEdit.html', {'data': showop})

def adminupdate(HttpRequest,tid):
    global i1
    i1=tid
    # pid = HttpRequest.GET.get('id')
    # print(pid)
    cate = db.child('fooddata').child(tid).child('category').get().val()
    fname = db.child('fooddata').child(tid).child('name').get().val()
    pri = db.child('fooddata').child(tid).child('price').get().val()
    image = db.child('fooddata').child(tid).child('files').get().val()
    hotelname = db.child('fooddata').child(tid).child('hotelname').get().val()
    ingrediants = db.child('fooddata').child(tid).child('ingredients').get().val()
    print(cate,fname,pri,image,hotelname,ingrediants)
    return render(HttpRequest,'Adminupdate.html',{'category':cate,'foodname':fname,'price':pri,'image':image,'hotelname':hotelname,'ingrediants':ingrediants})

def updatedata(HttpRequest):
    category = HttpRequest.POST.get('category')
    name = HttpRequest.POST.get('foodname')
    price = HttpRequest.POST.get('price')
    image = HttpRequest.POST.get('url')
    hotelname = HttpRequest.POST.get('hotelname')
    ingredients = HttpRequest.POST.get('ingrediants')
    print(category,name,price,image,hotelname,ingredients)

    db.child('fooddata').child(i1).update({'category':category,'name':name,'price':price,'files':image,'hotelname':hotelname,'ingredients':ingredients})
    return adminedit(HttpRequest)

def delete(HttpRequest,tid):
     db.child('fooddata').child(tid).remove()
    # print(i1)

     return showfooddetail(HttpRequest)
