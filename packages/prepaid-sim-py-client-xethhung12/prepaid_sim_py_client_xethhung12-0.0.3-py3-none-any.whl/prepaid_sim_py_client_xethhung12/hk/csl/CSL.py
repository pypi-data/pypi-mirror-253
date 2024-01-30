import requests
from lxml import html
import re
def remainingAmountOfData(mobileNo: str, password: str, debug=False) -> float:
    session = requests.Session()
    user_agent_header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    base_header = {}
    base_header.update(user_agent_header)
    resp = session.get("https://prepaid.hkcsl.com/login", headers=base_header)
    if debug:
        print(resp.status_code)
        print(resp.text)
    HEADERS = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        "Referer": "https://prepaid.hkcsl.com/login"
    }
    HEADERS.update(user_agent_header)

    data = {
        "msisdn": mobileNo,
        "password": password
    }
    resp = session.post("https://prepaid.hkcsl.com/login_add",
                 headers=HEADERS
                 , data=data)
    if debug:
        print(resp.status_code)
        print(resp.text)
    resp = session.get("https://prepaid.hkcsl.com/usage?lang=EN", headers=base_header)
    if debug:
        print(resp.status_code)
        print(resp.text)

    rHtml = resp.text
    tree = html.fromstring(rHtml)
    td = tree.xpath("//td[text()='Local Data']/../following-sibling::tr/following-sibling::tr/td[2]")[0]
    value = td.text_content().replace("\r\n", "").replace("\t", "")
    return float(re.match("([.\\d]+) GB", value.strip())[1])
