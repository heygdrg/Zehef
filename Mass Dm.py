import requests
from pystyle import * 
import threading

banner = """
                                ______ _______ _     _ _______ _______
                                 ____/ |______ |_____| |______ |______
                                /_____ |______ |     | |______ |                                    
"""
message = 'made with <3 by BKS'

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


def spam_message(content):
    try:
        channel = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    except:
        print(f"an error occured while scraping user {channel['message']}")
    
    for erl in channel:
        id_channel = erl['id']
        try:
            requests.post(f'https://discord.com/api/v9/channels/{id_channel}/messages',
            data={"content": f"{content}"},
            headers={'Authorization': token})
            print(id_channel)
        except:
            print(f"an error occured while sending mp ")

def spam_guild(content):
    
    try:
        guilds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    except:
        print(f"an error occured while scraping user {t['message']}")
    
    for guild in guilds:
        guild_name = guild['name']
        print(f'scraping {guild_name}')
        with open('id.txt', 'w')as file:
            file.write(f'scraping {guild_name}\n')
    
    id_list = []
    
    for chanel in guilds:
            id_guild = chanel['id']
            
            try:
                t = requests.get(f'https://discord.com/api/v8/guilds/{id_guild}/channels', headers=getheaders(token)).json()
            
            except:
                print(f"an error occured while scraping guilds {t['message']}")
            
            for chan in t:
                chan = chan['name']
                print(f'scraping channel {chan}')
                with open('server channel.txt', 'w')as file:
                    file.write(f'scraping channel {chan}\n')
            
            for elr in t:
                id_channel = elr['id']
                try:
                    r = requests.get(f'https://discord.com/api/v8/channels/{id_channel}/messages', headers=getheaders(token)).json()
                except:
                    print(f"an error occured while scraping channel {r['message']}")
                
                for message in r:
                    
                    try:
                        id = message['author']['id']
                        
                        if id in id_list:
                            pass
                        
                        else:
                            print(f'scraping users {id}')
                            id_list.append(id)
                        with open('id.txt', 'w')as file:
                            for id in id_list:
                                file.write(f'scraping users {id}\n')

                    except Exception as e:
                        print(e)
    print(id_list)

    for iid in id_list:
        payload =  {'recipients': [iid]}
        headers = { 
            'Cookie': '__dcfduid=30b25b30bdb811eca9acdd9d360ada08',
            'authorization': token,
            'Content-Type': 'application/json',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJkaXNjb3JkLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiJodHRwczovL2Rpc2NvcmQuY29tLyIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6ImRpc2NvcmQuY29tIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTYwNjQ1LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
        }
        
        response = requests.post("https://discord.com/api/v8/users/@me/channels", headers=headers, json=payload).json()                
        print(response)
        
        try: 
            channel_id_message = response['id']
            print(f'channel {channel_id_message} create with {iid}')
            
            requests.post(f'https://discord.com/api/v9/channels/{channel_id_message}/messages',
            data={"content": f'{content}'},
            headers={'Authorization': token})
        
        except:
            print(f'an error happened with {iid} {response["message"]}')


token = ''
content = 'test bot mass dm '
threading.Thread(target = spam_message()).start()
#threading.Thread(target = spam_guild()).start()


#print(r[0]['author']['username'])
#print(r['author'])
#print(r[0]['author']['id'])