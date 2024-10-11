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
            'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728620310681%2C%22v%22%3A1%7D',
            'wd': '1072x955',
            'fr': '1dvtcLYkzY5zQiWrP.AWWtrrV7YYBaoYz3pkH_UdIGQQ4.BnCKoZ..AAA.0.0.BnCKoZ.AWVgz2ALFhY',
            'xs': '41%3AvLFumcRD-SS7uQ%3A2%3A1728373764%3A-1%3A-1%3A%3AAcUaEuelDUtKNwefyZvxiqtTGZAGgXg49eYMb5zkgg',
        }

        self.headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'sb=Sd0EZyd1ZLFTH1DgFE17E4Nu; datr=Sd0EZ6_llVPt6h1Plmpmd3gI; locale=id_ID; ps_l=1; ps_n=1; c_user=61566949410348; fbl_st=101536515%3BT%3A28806236; vpd=v1%3B868x648x2.000000037252903; dpr=0.71875; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728620310681%2C%22v%22%3A1%7D; wd=1072x955; fr=1dvtcLYkzY5zQiWrP.AWWtrrV7YYBaoYz3pkH_UdIGQQ4.BnCKoZ..AAA.0.0.BnCKoZ.AWVgz2ALFhY; xs=41%3AvLFumcRD-SS7uQ%3A2%3A1728373764%3A-1%3A-1%3A%3AAcUaEuelDUtKNwefyZvxiqtTGZAGgXg49eYMb5zkgg',
            'origin': 'https://www.facebook.com',
            'priority': 'u=1, i',
            'referer': 'https://www.facebook.com/search/top?q=bobotoh&locale=id_ID',
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
            'x-fb-lsd': 'cRvHIYBhU4mvq30V-4qd1G',
        }

    def get_data(self, cursor=None, page_name=None):
        data = {
            'av': '61566949410348',
            '__aaid': '0',
            '__user': '61566949410348',
            '__a': '1',
            '__req': '36',
            '__hs': '20007.HYP:comet_pkg.2.1..2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1017254469',
            '__s': '60vehe:ee5yar:756sgl',
            '__hsi': '7424367682417721373',
            '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17yUJ3odE98K361twYwJyE24wJwpUe8hwaG1sw9u0LVEtwMw65xO2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwh8lwUwgojUlDw-wQ-261eBx_wHwoE7u7EbXCwLyESE2KwwwOg2cwMwhEkxebwHwNxe6Uak0zU8oC1hxB0qo4e4UcEeE4WVU-4EdrxG1fBG2-2K0UE',
            '__csr': 'gugvsbh4QdsAtZFEpfbeIJjnqh2Ti99ktlON3lEzbtnRi8G4AZFkD9nsGO8OaAGuq8XjWr9ilHWrzBGaJehrXgH8heehoXWmnUPAUTK8iK8y6vyUmxi8gSeDDCAKrypuamUGEOi8jgC2Cu49EymAm4A5Kq9wn8K4kii6Gw-xO2C58e8G5-cwjHxi2a7oWawuoaU9oco4m1CAwkoaU6u0Vo4C1iwxxGeBU2-woo0iiwlU27g0gcwZw1oPxy59801hwQ1eg0nAyE3mw1gy06i826ix91m0xU04ve1Kw0tVo4y1kK0PU2Ww1rS',
            '__comet_req': '15',
            'locale': 'id_ID',
            'fb_dtsg': 'NAcMRPWckZAJDNbCjywt0TkkMEt13YrGI8fZpAYpdjBviNHGQ42Jo-Q:41:1728373764',
            'jazoest': '25412',
            'lsd': 'cRvHIYBhU4mvq30V-4qd1G',
            '__spin_r': '1017254469',
            '__spin_b': 'trunk',
            '__spin_t': '1728620306',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'SearchCometResultsInitialResultsQuery',
            'variables': '{"count":5,"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"5c14e1fe-5a20-4646-b508-dd1e8fa87f48","tsid":"0.421474136883075"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"PAGES_TAB"},"filters":[],"text":"'+(page_name or '')+'"},"cursor":"'+(cursor or '')+'","feedbackSource":23,"fetch_filters":true,"renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '8029399013832562',
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