import requests
import sys

banner = """


███████╗██████╗ ███████╗██████╗ ██████╗  ██████╗ ██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝
█████╗  ██████╔╝█████╗  ██║  ██║██║  ██║██║   ██║ ╚███╔╝ 
██╔══╝  ██╔══██╗██╔══╝  ██║  ██║██║  ██║██║   ██║ ██╔██╗ 
██║     ██║  ██║███████╗██████╔╝██████╔╝╚██████╔╝██╔╝ ██╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

"""
def main():
    try:
        print(banner)
        headers = {"X-Forwarded-For":sys.argv[1]}
        origin = "http://httpbin.org/ip"
        url = sys.argv[2]
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            print(res.content)
        if res.status_code == 400:
            print("[ERROR]")
            print(res.content)
        if res.status_code == 401:
            print("[ERROR]401")
            print(res.content)
    except IndexError:
        print("[Example]python3 XFF.py [PORT]8.8.8.8 [URL_TARGET]http://example.com")
        print("[TIP]at the beginning,in url target use http://httpbin.org/ip for see the IPs ")
main()