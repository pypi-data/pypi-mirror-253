from requests import get
from urllib import request

def download(url:str, file_name:str):
    request.urlretrieve(url, file_name)

def ephoto(id:int, text:str, file_name:str):
    download(f"https://haji-api.ir/ephoto360?type=text&id={id}&text={text}", file_name)

def angizeshi():
    return get("https://haji-api.ir/angizeshi")

def ketab():
    return get("https://haji-api.ir/ketab")

def date():
    return get("https://haji-api.ir/date")

def photography(file_name:str):
    download("https://haji-api.ir/photography", file_name)

def owghat(city:str):
    return get(f"https://haji-api.ir/owghat?city={city}")

def gang():
    return get("https://haji-api.ir/gang")

def barcode(text:str, file_name:str):
    download(f"https://haji-api.ir/barcode?text={text}", file_name)

def makeemail():
    return get("https://haji-api.ir/email?method=getNewMail")

def getemails(email:str):
    return get(f"https://haji-api.ir/email?method=getMessages&email={email}")

def deghat():
    return get("https://haji-api.ir/deghat")

def drweb(url:str):
    return get(f"https://haji-api.ir/drweb?url={url}")

def font(design:str, text:str):
    return get(f"https://haji-api.ir/font?design={design}&text={text}")

def zekr():
    return get("https://haji-api.ir/zekr")

def mobile(name:str):
    return get(f"https://haji-api.ir/mobile?name={name}")

def tiktok(url:str, file_name:str):
    download(f"https://haji-api.ir/tiktokDOWNLOAD?url={url}", file_name)

def arz():
    return get("https://haji-api.ir/arz")

def arzdigital():
    return get("https://haji-api.ir/arzDigital")

def instainfo(id:str):
    return get(f"https://haji-api.ir/instainfo?url={id}")

def gpt(question:str):
    return get(f"https://haji-api.ir/majid/gpt/4?q={question}")