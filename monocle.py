import requests
import socket
import time
import json
import argparse

def args_handler():
    parser = argparse.ArgumentParser(prog="Monocle.py", formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="Search usernames in various websites.")
    parser.add_argument("-u", "--username", help='Username to search for', required=True)
    parser.add_argument("-f", "--failed", action='store_true', help='Print failed request', required=False)
    return parser.parse_args()


class Monocle:

    def __init__(self):
        with open("sites.json") as _sites:
            self.sites = json.load(_sites)

        self.site_to_test = None
        self.args = args_handler()
        self.requests = requests

        self.SUCCESS = []
        self.FAILED = []
        self.WEBSITE = []

        self.banner = '''
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@*                           (@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@,                                     #@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@                                         ,@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@                                             @@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@                                               @@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@                                                 @@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@,                                                 &@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@                                                   @@@@@@@@@@@@@@
        @@@@@@@@@@@@@@&                                                   @@@@@@@@@@@@@@
        @@@@@@@@@@@@@@.                                                   &@@@@@@@@@@@@@
        @@@@@@@@@@@@@@                                                    .@@@@@@@@@@@@@
        @@(*/@@@@@@@@@                                                     @@@@@@@@&**#@
        @           .@                                                     &            
        @@.                                                                           (@
        @@@@@                                                                       @@@@
        @@@@@@@@@%                                                             &@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@%%%%%##(((((////***///((((((##%%%&&@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@&.&@@@@@@%*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@, @@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@%@%#@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@%@@@& @@@@@@@@@/(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@,        /@@/        /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@&  @@@@@@@@@&                            @@@@@@@@@   &@@@@@@@@@@@@@
        @@@@@@@@@@& &@@@@@@@@@&                                 (@@@@@@@@@@% &@@@@@@@@@@
        @@@@@@@@@@  &@@@@@@(                                        @@@@@@@,  @@@@@@@@@@
        @@@@@@@@@@(                                                          %@@@@@@@@@@
        @@@@@@@@@@@@@*                       #@@@@@                        @@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@%(**/#&@@@@@@@@@@@@@@@@@@@@%(*****%@@@@@@@@@@@@@@@@@@@@@@
        \n\n\n'''

    def outer_func(self, color):
        def inner_func(msg):
            print(f'{color}{msg}')
        return inner_func

    def _get_username(self):
        self.username = self.args.username

    def sites_reeval(self):
        print(f'[+] Searching for:\t{self.username}')

        for url in self.sites['sites']:
            self.site_to_test = eval(self.sites['sites'][url])
            try:
                _request = self.requests.get(self.site_to_test, timeout=2)
                if _request.status_code == 200:
                    print(f"[+] {_request.status_code} {self.site_to_test} - Valid! ")
                    self.SUCCESS.append(self.site_to_test)

                else:
                    if self.args.failed is True:
                        self.FAILED.append(self.site_to_test)
                        print(f"[-] {_request.status_code} {self.site_to_test} -  User Dose not exist")

            except:
                print(f"[+] {_request.status_code} {self.site_to_test} - Request timed out ")

    def main(self):
        print(self.banner)
        self._get_username()
        self.sites_reeval()

        print(f'[X] TOTAL = {len(self.sites["sites"])}')
        print(f'[X] SUCCESS = {len(self.SUCCESS)}')
        print(f'[X] FAILED = {len(self.FAILED)}')


if __name__ == '__main__':
    Monocle().main()
