import requests




def get_guild_name(guild_name : str) -> str:
    headers = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    }
    
    search_url = f"https://gameinfo-sgp.albiononline.com/api/gameinfo/search?q={guild_name}"
    resp = requests.get(search_url, headers=headers)
    if resp.status_code != 200:
        raise Exception("Failed to fetch guild name. Please check the guild name and try again.")
    guild_data = resp.json()
    for i in guild_data.get("guilds"):
        if guild_name == i.get("Name"):
            return i.get("Id")
        

def get_all_members(guild_id : str) -> list:
    headers = {
        'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    if not guild_id:
        raise ValueError("Guild ID cannot be empty. Please provide a valid guild ID.")

    search_url = f"https://gameinfo-sgp.albiononline.com/api/gameinfo/guilds/{guild_id}/members"

    resp = requests.get(search_url,headers=headers)
    data = resp.json()
    player_list = [i.get("Name") for i in data]

    return player_list