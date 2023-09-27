# Plotly-and-Razorpay
Multi-app small Django project with Plotly and Razorpay Integration.
## Project Structure.

![plotly and razorpay project structure](https://github.com/krsatyam99/Plotly-and-Razorpay/assets/103446420/67f4d108-e1bf-4bc3-b3b8-dc33fa785c41)


### Must Requirements
Django==4.2.5
plotly==5.17.0
razorpay==1.4.1
requests==2.31.0
sqlparse==0.4.4


## Plotly Graph 
Plotly, is an interactive, open-source, and browser-based graphing library. It offers Python-based charting, powered by plotly. js. The library ships with over 30 chart types, including scientific charts, 3D graphs, statistical charts, SVG maps, financial charts, and more.
#####  Demo video 

### Basic bar graph plotly code:
import plotly.express as px 

data_canada = px.data.gapminder().query("country == 'Canada'")


fig = px.bar(data_canada, x='year', y='pop')

fig.show()

Plotly  Docs link :-https://plotly.com/python/

### Sequence diagram for the  Plotly integration .
![Plotly Graph](https://github.com/krsatyam99/Plotly-and-Razorpay/assets/103446420/20150294-357b-443c-8585-e7a066e87ed5)



## Razorpay Payment gateway Integration.
https://razorpay.com/docs/payments/server-integration/python/payment-gateway/build-integration/

Integrate Razorpay Standard Checkout with your website to start accepting payments. You can start accepting payments from customers on your website using the Razorpay Web Standard Checkout. Razorpay has developed the Standard Checkout method and manages it.
#### Benefits:
1. Easily add payments to your website or app
2. Access a wide range of payment solutions and services

3. Manage and track money movements to vendors
4. Get reliable fraud prevention and security

 
#####  Demo video 


#### Note:- 
For acessing the PG in razorpay you need the secret key and Id .
Here, I'm integrating in test mode.
##### Steps to get Client Id, Live Secret Key from Razorpay :
Step 1: Go to Razorpay.

Step 2: If you have a Razorpay account , login, else Signup.

Step 3: Click on Settings.
  
![a33](https://github.com/krsatyam99/Plotly-and-Razorpay/assets/103446420/256baf0a-531e-4d5b-8392-2696e88f0e57)

Step 4: Click on API Keys


![a34](https://github.com/krsatyam99/Plotly-and-Razorpay/assets/103446420/01122554-c747-444c-b7e8-3214477b43bd)

Step 5: Click on Generate Test Key
![a35](https://github.com/krsatyam99/Plotly-and-Razorpay/assets/103446420/aebf5465-3ea1-4e51-bd09-3a3990c1432e)

Step 6: The Client Id and Secret Key will appear. Copy these keys and click on OK or you can download in your local PC.

![a36](https://github.com/krsatyam99/Plotly-and-Razorpay/assets/103446420/4e34bac7-5e7d-4a37-8bdc-146e178a966b)

### Sequence Diagram for razorpay integration in my project.

![razorpay](https://github.com/krsatyam99/Plotly-and-Razorpay/assets/103446420/5e84c91b-2135-4533-b44d-6dc13f61b305)
