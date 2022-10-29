import requests
BASE_URL = "https://api.waifu.im/"
RANDOM_WAIFU_URL = BASE_URL +"random/"
QUERY_PARAMS = {"gif":f'{input("напишите True если хотите гифку и False ecли нет:")}' , "order_by":f'{input("напишите FAVOURITES или UPLOADED_AT:")}', "many": f'{input("напишите True если хотите больше 1 и False ecли нет:")}', "is_nsfw":f'{input("рекомендуется False:")}'}

def get_from_requests(url:str, params:dict):
    return requests.get(
        url,
        params=params
    ).json()
print(get_from_requests(RANDOM_WAIFU_URL, QUERY_PARAMS))