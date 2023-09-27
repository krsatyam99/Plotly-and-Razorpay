from django.shortcuts import render
from Graphs.settings import RAZOR_KEY_ID,RAZOR_KEY_SECRET
import razorpay
# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))

# Create your views here.
def razorpay(request):
  
  
   

    DATA = {
        "amount": 10000, #Razorpay accepts in paise Indian currency. 
        "currency": "INR",
        # "receipt": "receipt#1",
        # "notes": {
        #     "key1": "value3",
        #     "key2": "value2"
        # }
        "payment_capture":1,
    }

    orders= razorpay_client.order.create(data=DATA)
    order_id=orders['id']
    # print(order_id)

    context={
        'api_key':RAZOR_KEY_ID,
        'order_id':order_id,
        'amount':100,
    }



    return render(request,'razorpay.html',context)
