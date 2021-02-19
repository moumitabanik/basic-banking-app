from django.shortcuts import render
from piggy_bank_app.models import UserData, Transactions
from django.http import HttpResponse
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
import json

def landing(request):
    return render(request, 'landing.html', {})

def view_all_customers(request):
    userDataViewObjArr =  []
    try:
        userDataArr = UserData.objects.all()
        
        for i in range(0, len(userDataArr)):
            name = ""
            for key, value in userDataArr[i].name.items():
                name=name+" "+value
            userDataViewObj ={
                "name":name,
                "cif":userDataArr[i].cif,
                "email":userDataArr[i].email_id,
                "accountType":userDataArr[i].acc_type,
                "balance":userDataArr[i].balance
            }
            userDataViewObjArr.append(userDataViewObj)
        print(userDataViewObjArr)
    except Exception as ex:
        print(ex)

    return render(request, 'view_customers.html', {"userData":userDataViewObjArr})

def txn_history(request):
    txnViewObjArr = []   
    try:
        txnHistArr = Transactions.objects.all()         
        for i in range(0, len(txnHistArr)):        
            fromUserCif = txnHistArr[i].fromCif
            toUserCif = txnHistArr[i].toCif
            fromUserData = UserData.objects.get(cif=str(fromUserCif))
            toUserData = UserData.objects.get(cif=str(toUserCif))
            fromUserName = ""
            toUserName = ""
            name = ""
            for key, value in fromUserData.name.items():
                name=name+" "+value
                fromUserName = name
            name = ""
            for key, value in toUserData.name.items():
                name=name+" "+value
                toUserName = name
            timestamp = txnHistArr[i].timestamp
            timestamp.replace(tzinfo=None)
            txnViewObj={
                "from":fromUserName,
                "to":toUserName,
                "amount":txnHistArr[i].amount,
                "timestamp":timestamp.strftime("%c")
            }
            txnViewObjArr.append(txnViewObj)
        print(txnViewObjArr)
    except Exception as ex:
        print(ex)


    return render(request, 'txn_history.html', {"txnData":txnViewObjArr})

def money_trans(request):
    userDataArr = UserData.objects.all()
    fromUserArr = []
    for i in range(0,len(userDataArr)):
        userObj = userDataArr[i].name
        name=""
        for key, value in userObj.items():
            name=name+" "+value
        fromUserObj = {
            "cif":userDataArr[i].cif,
            "name":name
        }
        fromUserArr.append(fromUserObj)
    #print(fromUserArr)
    
    #userDataArr = UserData.objects.all()
    toUserArr = []
    for i in range(0,len(userDataArr)):
        userObj = userDataArr[i].name
        name=""
        for key, value in userObj.items():
            name=name+" "+value
        toUserObj = {
            "cif":userDataArr[i].cif,
            "name":name
        }
        toUserArr.append(toUserObj)
    #print(toUserArr)

    return render(request, 'money_trans.html', {"fromUserData":fromUserArr,"toUserData":toUserArr})


def submitTxn(request):  
    try:
        print(request)  
        json_data = json.loads(request.body)
        print(json_data["from"])
        fromUser = UserData.objects.get(cif=json_data["from"])
        toUser =  UserData.objects.get(cif=json_data["to"])
        txn = Transactions.objects.create(fromCif = json_data["from"], toCif = json_data["to"], amount = json_data["amount"])    
        print(type(fromUser.balance))
        print(type(json_data["amount"]))
        print(toUser.balance)
        print(txn)
        fromUser.balance = fromUser.balance - int(json_data["amount"])
        toUser.balance = int(json_data["amount"]) + toUser.balance
        txn.save()
        fromUser.save()
        toUser.save()
        response = {"response":"Txn completed successfully"}
        #return render(request, 'transaction_successful.html', json_data)
        return JsonResponse(response)

    except Exception as ex:
        print(ex)

def customer_details(request, email):
    #get all data to be displayed in the html
    user=UserData.objects.get(email_id="banikmoumita922@mgila.com")
    firstname = ""
    for key, value in user.name.items():
        if(key == 'first_name'):
            firstname = value
    user = {
        "user":firstname
    }
    print(user)
    return render(request, 'customer_details.html', user)

def transaction_successful(request):
    print("from txn_success")
    print(request.GET["amount"])
    return render(request, 'transaction_successful.html', {"from":request.GET["from"],"to":request.GET["to"],"amount":request.GET["amount"]})


def getTxnData(request, emailId):
    user=UserData.objects.get(email_id=emailId)
    userData = user.name
    return HttpResponse(userData)