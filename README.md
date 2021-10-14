# Ecommerce-website
This is an online store where you can purchase product. I also integrated online payment with it and yes! It has webhook. I didn't really use the webhook as the API server I use automatically sends mail to customers for each successful transaction 

# Installation 
All you have to do is to install Django(hoping you have python installed already) and ngrok(to test your webhook)

# Usage 
Firstly, startup your ngrok server. If you dont't know how to do so, head over to https://ngrok.com/download for proper tutorial. After yve gotten your tunnel link, head on to your flutterwave dashboard and insert it to your Webhook under your settings<img width="1440" alt="Screenshot 2021-10-14 at 8 12 44 AM" src="https://user-images.githubusercontent.com/63419117/137269128-f7cbd9a9-5c64-4d1c-9a11-b8825779e8fc.png">

After that, insert the link into your `ALLOWED_HOST` in your settings.py file and your orders app views.py redirect_url above the flutterwave endpoint for your charges transaction. Also go back to your flutterwave dashboard and copy your test api secret key and put it in your orders app .env file.

# Webhook
Since yve all this up and running, after all your successful transaction, your webhook will be printed as long as your ngrok server is up and running <img width="660" alt="Screenshot 2021-10-14 at 8 17 16 AM" src="https://user-images.githubusercontent.com/63419117/137269872-3157fa81-626c-4541-8fff-c18ad3763b03.png">
