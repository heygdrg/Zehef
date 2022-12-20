import requests
from pystyle import * 
import threading
import os 

banner = """
                                ______ _______ _     _ _______ _______
                                 ____/ |______ |_____| |______ |______
                                /_____ |______ |     | |______ |                                    
"""
message = 'made with <3 by BKS'

def startup():
    print(Colorate.Vertical(Colors.blue_to_white, Center.XCenter(banner)))
    print(Colorate.Vertical(Colors.blue_to_white, Center.XCenter(message)))


def getheaders(token):
    headers = {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    }
    
    if token: 
        headers.update({"Authorization": token})
    return headers


def spam_message():
    
    try:
        channel = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    
    except:
        print(Colorate.Horizontal(Colors.red_to_white,f"[-] An error occured while scraping user {channel['message']}" , 1))   
    
    for erl in channel:
        id_channel = erl['id']
        
        try:
            requests.post(f'https://discord.com/api/v9/channels/{id_channel}/messages',
            data={"content": f"{content}"},
            headers={'Authorization': token})
            
            if 'message' == 'Unknown Channel':
                print(Colorate.Horizontal(Colors.red_to_white, f"[-] An error occured while sending mp ", 1))
            
            else:
                print(Colorate.Horizontal(Colors.green_to_white, f"[+] Scraping dm : {id_channel}", 1))
            
        except:
            print(Colorate.Horizontal(Colors.red_to_white, f"[-] An error occured while sending mp ", 1))


def spam_guild():
    
    
    
    dm_create = 0
    guild_scrap = 0
    id_scrap = 0
    channel_scrap = 0
    
    os.system(f'Title - ZEHEF mass DM - Guild scrap : {guild_scrap}  Channel scrap : {channel_scrap}  ID scrap : {id_scrap}  DM create : {dm_create}')
    
    try:
        guilds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    
    except:
        print(Colorate.Horizontal(Colors.red_to_white,f"[-] An error occured while scraping user : {t['message']}" , 1))



    for guild in guilds:
        
        guild_name = guild['name']
        print(Colorate.Horizontal(Colors.green_to_white, f'[+] Scraping  : {guild_name}', 1))
        
        guild_scrap = guild_scrap + 1
        os.system(f'Title - ZEHEF mass DM - Guild scrap : {guild_scrap}  Channel scrap : {channel_scrap}  ID scrap : {id_scrap}  DM create : {dm_create}')
    
    id_list = []
    
    for chanel in guilds:
        
        id_guild = chanel['id']
        
        try:
            t = requests.get(f'https://discord.com/api/v8/guilds/{id_guild}/channels', headers=getheaders(token)).json()
            
        except:
            print(Colorate.Horizontal(Colors.red_to_white,f"[-] An error occured while scraping guilds {t['message']}" , 1))
            
        for chan in t:
            chan = chan['name']
            print(Colorate.Horizontal(Colors.green_to_white,f'[+] Scraping channel : {chan}' , 1))
            channel_scrap = channel_scrap + 1
            os.system(f'Title - ZEHEF mass DM - Guild scrap : {guild_scrap}  Channel scrap : {channel_scrap}  ID scrap : {id_scrap}  DM create : {dm_create}')


        for elr in t:
            id_channel = elr['id']
            try:
                
                r = requests.get(f'https://discord.com/api/v8/channels/{id_channel}/messages', headers=getheaders(token)).json()
            except:
                
                print(Colorate.Horizontal(Colors.red_to_white,f"[-] An error occured while scraping user " , 1))
            

            for message in r:
                        
                try:
                    id = message['author']['id']
                            
                    if id in id_list:
                        pass
                            
                    else:
                        print(Colorate.Horizontal(Colors.green_to_white,f'[+] Scraping user : {id}' , 1))
                        id_list.append(f'{id}\n')
                        id_scrap = id_scrap + 1
                        os.system(f'Title - ZEHEF mass DM - Guild scrap : {guild_scrap}  Channel scrap : {channel_scrap}  ID scrap : {id_scrap}  DM create : {dm_create}')


                except Exception as e:
                    print(Colorate.Horizontal(Colors.red_to_white, "[-] An error ocured while scraping user id ", 1))

    
    for iid in id_list: 

        payload =  {'recipients': [iid]}
        headers = { 
            'Cookie': '__dcfduid=30b25b30bdb811eca9acdd9d360ada08',
            'authorization': token,
            'Content-Type': 'application/json',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJkaXNjb3JkLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiJodHRwczovL2Rpc2NvcmQuY29tLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2NvcmQuY29tIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTYwNjQ1LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
        }
        
        response = requests.post("https://discord.com/api/v8/users/@me/channels", headers=headers, json=payload).json()                
      
        try: 
            channel_id_message = response['id']
                    
            print(Colorate.Horizontal(Colors.green_to_white,f'[+] Channel : {channel_id_message} create with : {iid}' , 1))
            dm_create = dm_create + 1
            os.system(f'Title - ZEHEF mass DM - Guild scrap : {guild_scrap}  Channel scrap : {channel_scrap}  ID scrap : {id_scrap}  DM create : {dm_create}')

                    
                    
                
            r = requests.post(f'https://discord.com/api/v9/channels/{channel_id_message}/messages',
                    data={"content": f'{content}'},
                    headers={'Authorization': token}).json()
            
            r = requests.post(f'https://discord.com/api/v9/channels/{r["channel_id"]}/messages',
                    data={"content": f'{content}'},
                    headers={'Authorization': token})

            print(Colorate.Horizontal(Colors.green_to_white,f'[+] message sent to {r["author"]["username"]}' , 1))    
        
        except:
            print(Colorate.Horizontal(Colors.red_to_white, f'[-] An error happened with {iid} ', 1))

def main():
    
    global content
    global token
    
    startup()
    print('\n\n')
    
    message_1 = ' [?] Enter the token to Mass DM : '
    token = input(Colorate.Vertical(Colors.blue_to_white, Center.XCenter(message_1)))
        
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
        
    if r.status_code == 200:
        pass
            
    else:
        print(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"[!] Invalid Token") , 1))
        input(Colorate.Horizontal(Colors.red_to_white, Center.XCenter(f"[!] Enter anything to continue. . . ") , 1))
        os.system('cls')
        main()
        
    content_1 = '[?] Enter the message you want to send : '
    content = input(Colorate.Vertical(Colors.blue_to_white, Center.XCenter(content_1)))

    threading.Thread(target = spam_message(), args=(content, token)).start()
    threading.Thread(target = spam_guild(), args=(content, token)).start()

#print(r[0]['author']['username'])
#print(r['author'])
#print(r[0]['author']['id'])

main()
