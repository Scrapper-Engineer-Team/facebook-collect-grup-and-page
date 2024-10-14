import requests
import time
from loguru import logger

class GrupName:
    def __init__(self):
        self.cookies = {
            'sb': 'Sd0EZyd1ZLFTH1DgFE17E4Nu',
            'datr': 'Sd0EZ6_llVPt6h1Plmpmd3gI',
            'locale': 'id_ID',
            'ps_l': '1',
            'ps_n': '1',
            'vpd': 'v1%3B868x648x2.000000037252903',
            'dpr': '0.71875',
            'wd': '1072x955',
            'c_user': '61566949410348',
            'fr': '1tvPrlTk8OifjG2uC.AWUnkl_QxfS6PmqH4VeodUkU88I.BnDQHK..AAA.0.0.BnDQRx.AWWe6QDc9Sg',
            'xs': '8%3AKwNvnG539Ti0MQ%3A2%3A1728906353%3A-1%3A-1',
            'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728906358630%2C%22v%22%3A1%7D',
        }

        self.headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'sb=Sd0EZyd1ZLFTH1DgFE17E4Nu; datr=Sd0EZ6_llVPt6h1Plmpmd3gI; locale=id_ID; ps_l=1; ps_n=1; vpd=v1%3B868x648x2.000000037252903; dpr=0.71875; wd=1072x955; c_user=61566949410348; fr=1tvPrlTk8OifjG2uC.AWUnkl_QxfS6PmqH4VeodUkU88I.BnDQHK..AAA.0.0.BnDQRx.AWWe6QDc9Sg; xs=8%3AKwNvnG539Ti0MQ%3A2%3A1728906353%3A-1%3A-1; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728906358630%2C%22v%22%3A1%7D',
            'origin': 'https://www.facebook.com',
            'priority': 'u=1, i',
            'referer': 'https://www.facebook.com/search/top?q=jual%20beli',
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
            'x-fb-lsd': 'jCDBmptHpJ08o4EFkMKiOm',
        }

    def get_data(self, cursor=None, grup_name=None):
        
        data = {
            'av': '61566949410348',
            '__aaid': '0',
            '__user': '61566949410348',
            '__a': '1',
            '__req': '1x',
            '__hs': '20010.HYP:comet_pkg.2.1..2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1017312134',
            '__s': 'g0v85g:p32o27:4c7fi1',
            '__hsi': '7425600153475752828',
            '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C1jyUW3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320om78c87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewGwkUe9obrwh8lwuEjUlDw-wUwxwjFovUaU6a0BEbXCwLyESE2KwwwOg2cwMwhEkxebwHwNxe6Uak0zU8oC1hxB0qo4e16wWwjHDzUiwRK6E4-mEbUaU3yw',
            '__csr': 'gdcIBcAQQkD5gF9jIAJOi-zONytJ_iQmmWuHsyECndZrmXvuWl5jlWnOACTjt4mjBp4bHK-jKdQmiJeqteVoO8zemiJ2EC4aQiElh8kLBgzXyoWicUc8SiGAK8xuEnz9US2yQaJ2EF2-m2m3KewiFopwhUao4Oq5Ec9UWewqUgwpU2gw8e3O6U1lE20yEnwaW0Fo4G0y84K0Jopw1-200mcS09Qw2QE0jdwkE0qiwey06p80m7g0A50',
            '__comet_req': '15',
            'fb_dtsg': 'NAcPIUOIDtZcSZgfhNBCrcm-dCHqv23Dcb4X1jLZ5X7hf5ao04QxQAw:8:1728907261',
            'jazoest': '25286',
            'lsd': '60BcJV0KflrF7siRyJhqDB',
            '__spin_r': '1017312134',
            '__spin_b': 'trunk',
            '__spin_t': '1728907263',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'SearchCometResultsInitialResultsQuery',
            'variables': '{"count":5,"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"d1f6476b-2d94-443f-ad40-40330e1fc73a","tsid":"0.42319510911874514"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"GROUPS_TAB"},"filters":[],"text":"'+(grup_name or '')+'"},"cursor":"'+(cursor or '')+'","feedbackSource":23,"fetch_filters":true,"renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '9916418588442949',
        }

        response = requests.post('https://web.facebook.com/api/graphql/', cookies=self.cookies, headers=self.headers, data=data)
        try:
            return response.json()
        except ValueError as e:
            logger.error(f"Failed to parse JSON response: {e}")
            return None

    async def process(self, grup_name=None, cursor=None):
        logger.info(f"Processing batch with cursor {cursor}")
        data = self.get_data(cursor, grup_name=grup_name)
        if not data or 'data' not in data or 'serpResponse' not in data['data']:
            logger.warning("No more data to fetch or error in response.")
            return None
	
	#menampilkan hasil pertama dengan seluruh field (Raw Data)
        results = data
        return results
