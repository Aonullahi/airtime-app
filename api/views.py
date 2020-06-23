from django.http import HttpResponse
from django.shortcuts import render, redirect
from api.forms import ContactFormset
import requests

def display_result(request, data, **kwargs):
    return render(request, 'api/result.html', dict(data=result, **kwargs))

def home(request):
    if request.method == 'POST':
        formset = ContactFormset(request.POST)
        if formset.is_valid():
            data = formset.cleaned_data
            print(len(data))
            print(data)
            send_aritime(request, data)
            print(result)
            return display_result(request, data=result)
    else:
        formset = ContactFormset()
    return render(request, 'api/home.html', {'formset': formset})


def send_aritime(request, data):
    url = "https://sandbox.wallets.africa/bills/airtime/purchase"

    rnds =len(data)
    global result
    result = []

    for i in range(rnds):
    
        access_token = 'uvjqzm5xl6bw'
        username = data[i]['username']
        network = data[i]['network'].lower()
        amount = data[i]['amount']
        phone_number = data[i]['phone_number']
        secret_key = 'hfucj5jatq8h'

        d = {"Code":"{}".format(network),"Amount":"{}".format(amount),"PhoneNumber":"{}".format(phone_number),"SecretKey":"{}".format(secret_key)}
        payload = "{" "\n" + "\n".join("{!r}: {!r},".format(k, v) for k, v in d.items()) + "\n" "}"

        headers = {
        'Authorization': 'Bearer {}'.format(access_token),  
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data = payload)
        
        result.append([username, response.json()]) 
        #print(response.text.encode('utf8'))
        #print(response.json())
    
   # return render(request, 'result.html', {'result': res})


