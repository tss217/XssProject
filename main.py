import argparse
import subprocess
import requests
from time import sleep

class XssBrute:
    def __init__(self, url):
        self.url = url
        self.wordlist = []  # Inicializa como uma lista
        self.urlXss = ""

    def executeCmd(self, command):
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as cmdError:
            print(cmdError)

    def setCmdToOpenBrowser(self):
        command = f"firefox {self.urlXss}"
        self.executeCmd(command)
        

    def setCmdToCloseBrowser(self):
        command = "pkill firefox"
        self.executeCmd(command)

    def openW(self, path):
        with open(path, "r") as file:
            for line in file:
                self.wordlist.append(line.strip())

    def setUrlXss(self, payload):
        self.urlXss = self.url + payload

    def checkUrlStatus(self):
        try:
            response = requests.get(self.urlXss)
            if response.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.RequestException as errorUrl:
            print(errorUrl)
            return False

    def alwayOpenBrowser(self):
        self.setCmdToOpenBrowser()
        sleep(5)
        self.setCmdToCloseBrowser()

def main():
    parser = argparse.ArgumentParser(description="XSS Brute Force")

    parser.add_argument("--url", help="URL to test", required=True)
    parser.add_argument("-w", help="Wordlist to use", required=True)
    parser.add_argument("-oB", help="Open browser", action="store_true")
    parser.add_argument("-t", help="Time to wait", type=int, default=0)
    parser.add_argument("-aOB", help="sempre abrir o browser", action="store_true")

    args = parser.parse_args()

    x = XssBrute(args.url)
    x.openW(args.w)    

    for i in x.wordlist:
        sleep(args.t)
        x.setUrlXss(i)
        if x.checkUrlStatus():
            print(f"XSS found [ok]: {x.urlXss}")
            if args.oB:
                x.setCmdToOpenBrowser()
                break
            elif args.aOB:
                x.alwayOpenBrowser()
        else:
            print(f"XSS not found [x]: {x.urlXss}")
            if args.aOB:
                x.alwayOpenBrowser()

if __name__ == "__main__":
    main()