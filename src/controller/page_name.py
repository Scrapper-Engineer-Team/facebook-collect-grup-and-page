import requests
import time
from loguru import logger
from src.controller.config_manager import ConfigManager

class PageName:
    def __init__(self):
        # self.cookies = {
        #     'sb': 'Sd0EZyd1ZLFTH1DgFE17E4Nu',
        #     'datr': 'Sd0EZ6_llVPt6h1Plmpmd3gI',
        #     'vpd': 'v1%3B868x648x2.000000037252903',
        #     'ps_l': '1',
        #     'ps_n': '1',
        #     'dpr': '0.71875',
        #     'c_user': '61567323625343',
        #     'datr': 'VE0NZ9GVivINzaiWdUdyuJbK',
        #     'xs': '39%3A2NFO8d02hllsCw%3A2%3A1728925031%3A-1%3A-1',
        #     'fr': '1tvPrlTk8OifjG2uC.AWXiZ5CS7XNYzgBM8p1r8N6Hhr8.BnDQHK..AAA.0.0.BnDU1B.AWWsEvI8pLA',
        #     'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728925036451%2C%22v%22%3A1%7D',
        #     'wd': '1072x955',
        #     'locale': 'id_ID',
        # }

        config_manager = ConfigManager()
        self.cookies = config_manager.get_cookies()

    def get_data(self, cursor=None, page_name=None):
        headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'sb=M48QZ8b8XXRPyMD9gYtiJKvr; dpr=0.71875; datr=M48QZ3KbJOKJ7EwHKetLOgMI; c_user=61566949410348; xs=13%3ACWnYUdbBbBkczg%3A2%3A1729138496%3A-1%3A-1; fr=0L2Iow2DSyHXBEUFa.AWXnG-PiuHy5jBJIlYQQ2srBooQ.BnEI84..AAA.0.0.BnEI9C.AWVB-GziGuk; ps_l=1; ps_n=1; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1729138499696%2C%22v%22%3A1%7D; wd=1072x944',
            'origin': 'https://www.facebook.com',
            'priority': 'u=1, i',
            'referer': 'https://www.facebook.com/search/top?q={page_name}'.format(page_name=page_name),
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
            'x-fb-lsd': 'Ywht0ZNdz7JOU0x_9gryxM',
        }

        data = {
            'av': '61566949410348',
            '__aaid': '0',
            '__user': '61566949410348',
            '__a': '1',
            '__req': '3a',
            '__hs': '20013.HYP:comet_pkg.2.1..2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1017421435',
            '__s': 'eesy65:vt6k4z:slpe1t',
            '__hsi': '7426593300476128583',
            '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C1jyUW3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320om78c87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewGwkUe9obrwh8lwuEjUlDw-wSU8o4Wm7-2K1yw9q2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE4WVU-4EdrxG1fBG2-2K0UE',
            '__csr': 'gacv7NYIn1p9fb4RO8j5i9h4Bls_vanBFlleXWdR5TniOd9Hip2nTZmWhaqChfsyGeKAWLnGt7HGBgkCHJ2ZdpVeGCKi4UNd2HDK9BzQQaCCh9qAUHUix524ih2oqzEGi596i3rQ4apEaC4oixm326p8S3jxGi685GU6iawwxy2K1ewxK3q1HwgEa8aUy2-1Aw4jxS1jwZweHwSwlE4m0QE1i80rjw5Ow2DU01jE40_k02LO0sa06y80k8w0BFz80Ka01Vpw7sw',
            '__comet_req': '15',
            'fb_dtsg': 'NAcOqjZ4MzZ9ZkcO2VI4EDtl3zUAhTdP_eDEPzSYTbhlJkLqAp_f5wg:13:1729138496',
            'jazoest': '25582',
            'lsd': 'Ywht0ZNdz7JOU0x_9gryxM',
            '__spin_r': '1017421435',
            '__spin_b': 'trunk',
            '__spin_t': '1729138498',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'SearchCometResultsPaginatedResultsQuery',
            'variables': '{"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"ad414d8d-fe2c-432d-88c4-d9a78f4528ff","tsid":"0.6978615152259975"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"PAGES_TAB"},"filters":[],"text":"'+(page_name or '')+'"},"count":5,"cursor":"'+(page_name or '')+'","feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":false,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":true,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '8301557076558301',
        }

        response = requests.post('https://web.facebook.com/api/graphql/', cookies=self.cookies, headers=headers, data=data)
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