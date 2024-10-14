import requests
import time
from loguru import logger

class PageName:
    def __init__(self):
        self.cookies = {
            'sb': 'Dg8NZxdJZmI2I6DnH4hUygDT',
            'dpr': '0.71875',
            'c_user': '61566949410348',
            'datr': 'Dg8NZxvvKLDDkToNIWtypsWj',
            'xs': '45%3AyCqa3qgRG3xJpA%3A2%3A1728909077%3A-1%3A-1',
            'fr': '0BcY8xnPAZuFHyULF.AWXwwVghVZfF9BhQ0OInYCMTtkA.BnDQ8N..AAA.0.0.BnDQ8e.AWVjRnyVQuw',
            'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728909091186%2C%22v%22%3A1%7D',
            'wd': '1072x955',
        }

        self.headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'sb=Dg8NZxdJZmI2I6DnH4hUygDT; dpr=0.71875; c_user=61566949410348; datr=Dg8NZxvvKLDDkToNIWtypsWj; xs=45%3AyCqa3qgRG3xJpA%3A2%3A1728909077%3A-1%3A-1; fr=0BcY8xnPAZuFHyULF.AWXwwVghVZfF9BhQ0OInYCMTtkA.BnDQ8N..AAA.0.0.BnDQ8e.AWVjRnyVQuw; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728909091186%2C%22v%22%3A1%7D; wd=1072x955',
            'origin': 'https://www.facebook.com',
            'priority': 'u=1, i',
            'referer': 'https://www.facebook.com/search/groups/?q=jual%20beli&locale=id_ID',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.137", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.137"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '"6.8.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'x-asbd-id': '129477',
            'x-fb-friendly-name': 'SearchCometResultsInitialResultsQuery',
            'x-fb-lsd': 'J28c-jbBj9d-msqcmfXJkp',
        }

    def get_data(self, cursor=None, page_name=None):
        data = {
            'av': '61566949410348',
            '__aaid': '0',
            '__user': '61566949410348',
            '__a': '1',
            '__req': '2b',
            '__hs': '20010.HYP:comet_pkg.2.1..2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1017313430',
            '__s': '5mhtr6:sg4naq:yuyqy1',
            '__hsi': '7425607983457742862',
            '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17yUJ3odE98K360CEboG0x8bo6u3y4o2Gwn82nwb-q7oc81xoswMwto886C11wBz83WwgEcEhwGxu782lwv89kbxS1Fwc61awkovwRwlE-U2exi4UaEW2G1jwUBwJK14xm3y11xfxmu3W3jU8o4Wm7-2K1yw9q2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE4WVU-4EdrxG1fBG2-2K0UE',
            '__csr': 'gbBMvNcnd9kJgRv7Rid9kYj99ishKlp4-B4lqnjb_qvWFkKDESNftHAAJqBLIBIKBgD9j_t9cx4V9fVFrybWKFtvK8nVVdFepaaALCKcxdJ2oXGtaiaAx-mmUKVeiEiGbGGBCK8zA7Q8DDx6td2oymWzAUkxuEpBUSfg4pry85a2m2iq3m7EyEoxe4ob4fwDxm13xm2K18wiFUS0wU5q7Ud9Q3OE5G1swTw-w9G13xO1GwExS1Lwh8qw5zw3X81oU1187p00LcF1e00kNCawi8G05r814U2Gwfy1qw4UwDw6ptwdG6E0aSU0TC19w29o0-G01N8wlbw',
            '__comet_req': '15',
            'locale': 'id_ID',
            'fb_dtsg': 'NAcN38j5YMacbUdFO1mvuwxKbLCsoBqJ1fjJOqI3G8fePPqI4E8TYgQ:45:1728909077',
            'jazoest': '25415',
            'lsd': 'J28c-jbBj9d-msqcmfXJkp',
            '__spin_r': '1017313430',
            '__spin_b': 'trunk',
            '__spin_t': '1728909086',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'SearchCometResultsInitialResultsQuery',
            'variables': '{"count":5,"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"0180c764-9964-4808-b0e8-28ef21fc9cb5","tsid":"0.5728625956156839"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"PAGES_TAB"},"filters":[],"text":"'+(page_name or '')+'"},"cursor":"'+(cursor or '')+'","feedbackSource":23,"fetch_filters":true,"renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '9916418588442949',
        }

        response = requests.post('https://web.facebook.com/api/graphql/', cookies=self.cookies, headers=self.headers, data=data)
        try:
            return response.json()
        except ValueError as e:
            logger.error(f"Failed to parse JSON response: {e}")
            return None
        
    async def process(self, page_name=None, cursor=None):
        logger.info(f"Processing batch with cursor {cursor}")
        data = self.get_data(cursor, page_name=page_name)
        if not data or 'data' not in data or 'serpResponse' not in data['data']:
            logger.warning("No more data to fetch or error in response.")
            return None

        #menampilkan hasil pertama dengan seluruh field (Raw Data)
        results = data
        return results