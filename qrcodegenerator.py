import qrcode
import PIL

# Taking the users upi id
upi_ID=input("---- Enter your UPI ID ----\n")
qr_url=int(input("Do you want to generate QR-code or a URL for payment ?\nEnter 1 for QRcode\nEnter 2 for URL genration\nEnter 3 for Both QR code and URL\n"))
url_app=None


# Setting the upi url for the apps
qrcode_url= f'upi://pay?pa={upi_ID}&pn=Recipient%20Name'  #Only this URL can generate working QRcode


# This URL cannot generate Working QR code
phonepe_url = f'intent://upi/pay?pa={upi_ID}&pn=Recipient%20Name#Intent;scheme=upi;package=com.phonepe.app;end'
google_pay_url = f'intent://upi/pay?pa={upi_ID}&pn=Recipient%20Name#Intent;scheme=upi;package=com.google.android.apps.nbu.paisa.user;end'
paytm_url = f'intent://upi/pay?pa={upi_ID}&pn=Recipient%20Name#Intent;scheme=upi;package=net.one97.paytm;end'




# Making the QRcode or URL
if(qr_url==1):
    qrcode_qr=qrcode.make(qrcode_url)# This is the only working QR code
    qrcode_qr.show()
elif(qr_url==2):
    url_app=int(input("For which app you want to generate the url?\n1.Phonepe\n2.Google_pay\n3.Paytem\n4.Universal Url"))
    if(url_app==1):
        print("This is your URL for Phonepe Payment :-",phonepe_url)
    elif(url_app==2):
        print("This is your URL for Google pay Payment :-",google_pay_url)
    elif(url_app==3):
        print("This is your URL for Paytm Payment :-",paytm_url)
    elif(url_app==4):
        print("This is your Universal URL for Payments :-",qrcode_url)
elif(qr_url==3):
    qrcode_qr=qrcode.make(qrcode_url)
    qrcode_qr.show()
    print("This is your Universal URL for Payments :-",qrcode_url)
    
