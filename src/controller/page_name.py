import requests
import time
from loguru import logger

class PageName:
    def __init__(self):
        self.cookies = {
            'sb': 'Sd0EZyd1ZLFTH1DgFE17E4Nu',
            'datr': 'Sd0EZ6_llVPt6h1Plmpmd3gI',
            'locale': 'id_ID',
            'ps_l': '1',
            'ps_n': '1',
            'c_user': '61566949410348',
            'fbl_st': '101536515%3BT%3A28806236',
            'vpd': 'v1%3B868x648x2.000000037252903',
            'dpr': '0.71875',
            'fr': '14qcuyn423VjDBEpg.AWUbRST2euVKfsG4STFezFBJzfU.BnDNTj..AAA.0.0.BnDNTj.AWWqnFtlx7s',
            'xs': '41%3AvLFumcRD-SS7uQ%3A2%3A1728373764%3A-1%3A-1%3A%3AAcU1fhj_XjfnohyLfadCVO-p3iGh796JXibw5Jg1GA',
            'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728894183598%2C%22v%22%3A1%7D',
            'wd': '1072x955',
        }

        self.headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'sb=Sd0EZyd1ZLFTH1DgFE17E4Nu; datr=Sd0EZ6_llVPt6h1Plmpmd3gI; locale=id_ID; ps_l=1; ps_n=1; c_user=61566949410348; fbl_st=101536515%3BT%3A28806236; vpd=v1%3B868x648x2.000000037252903; dpr=0.71875; fr=14qcuyn423VjDBEpg.AWUbRST2euVKfsG4STFezFBJzfU.BnDNTj..AAA.0.0.BnDNTj.AWWqnFtlx7s; xs=41%3AvLFumcRD-SS7uQ%3A2%3A1728373764%3A-1%3A-1%3A%3AAcU1fhj_XjfnohyLfadCVO-p3iGh796JXibw5Jg1GA; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728894183598%2C%22v%22%3A1%7D; wd=1072x955',
            'origin': 'https://www.facebook.com',
            'priority': 'u=1, i',
            'referer': 'https://www.facebook.com/search/groups/?q=jokowi&locale=id_ID',
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
            'x-fb-lsd': 'vuzyUmbjCxQ8zvxDnMUuwc',
        }

    def get_data(self, cursor=None, page_name=None):
        data = {
            'av': '61566949410348',
            '__aaid': '0',
            '__user': '61566949410348',
            '__a': '1',
            '__req': '2c',
            '__hs': '20010.HYP:comet_pkg.2.1..2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1017311075',
            '__s': 'zfmogr:owd1mk:vvq2ns',
            '__hsi': '7425543944353986802',
            '__dyn': '7AzHK4HwBgDx-5Q1hyoyEqxd4Ag5S3G2O5U4e2C3-ubyQdwSAx-bwNwnof8boG4E762S1DwUx60xU8E5O0BU2_CxS320om78bbwto88422y11wBz822wtU4a3a4oaEnxO0Bo4O2-2l2UtwxwhU31wiE567Udo5qfK0zEkxe2GexeeDwkUtxGm2SU4i5oe8cEW4-5pUfEdK2616DBx_wHwoE7u7EbXCwLyESE2KwwwOg2cwMwhA4UjyUaUcojxK2B08-269wkopg6C13xe3a3G1eKufxa3mUqwjVqwLwHwea',
            '__csr': 'gakQ6Zhkt34RN4JgHknn9i49WObTvMB9A4jivA9eSgLbsp8NHWdZkmyWF6lHQ-rYJ5ih7QqGAA_niFypfqVeiJ97GbqnyECAHCKngynZ4GjLAVV-WiQRGuAVQaDGUGV4qWZoCHxajhVHCGinybgGFfKFdaQUyupeWBGmjwCCDx28xq8xquLyKAiVVVUqCzUSdyui78kBggG5pUhxC8Bglxpy5xOKmVUGbBzpE8qxO6U8U8oy9DKq5EaErz8tyu26axmuUyq8xGmt0iEaQ4EW4poO8ypooCwSwywxyVCUy7E4qi2W3Ku68gwBwGDgy3a58pyEmwOxK11GdK48hwxg998999XVEapEWi3u9ndc0JE248E-1dK1nyUCq0NK0iq0AE4V289oGKFeQS9z6l2QUBBGapV5VeEKlBx3lZZTnauungmAGii2Z5Cw8u8wqEboGi0wvKXG-S310uU94sBAgK2O262t3V9o5H-1Nhk2-0C87S0le0448G2hEElAIxpuF40yU040u8w11G0eJyU0qagO7U0Ky0fZw0hkU7601vhw2kU3kw6sg550fa0eqwb-0_oco8Em81cw9V092ew6dCw5IG4Epo3bwTw55woVBS07RU1qA0diwFw5_w0Hbw1ti6p8nwQ86o15bwUw0DIQfwDweS4o0IGm0gm08Ewn80jBw56w',
            '__comet_req': '15',
            'locale': 'id_ID',
            'fb_dtsg': 'NAcMHLAowIxbdayhBcX9ygcu9paeoHUpVADfgZy2KXhWXmrLwBz0gCA:41:1728373764',
            'jazoest': '25733',
            'lsd': 'vuzyUmbjCxQ8zvxDnMUuwc',
            '__spin_r': '1017311075',
            '__spin_b': 'trunk',
            '__spin_t': '1728894176',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'SearchCometResultsInitialResultsQuery',
            'variables': '{"count":5,"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"4a40ffd3-7eff-4073-8df0-12a6b8e478ca","tsid":"0.29607292314943456"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"PAGES_TAB"},"filters":[],"text":"'+(page_name or '')+'"},"cursor":"'+(cursor or '')+'","feedbackSource":23,"fetch_filters":true,"renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":true}',
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