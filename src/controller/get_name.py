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
            'c_user': '61566949410348',
            'fbl_st': '101536515%3BT%3A28806236',
            'vpd': 'v1%3B868x648x2.000000037252903',
            'dpr': '0.71875',
            'fr': '14qcuyn423VjDBEpg.AWUbRST2euVKfsG4STFezFBJzfU.BnDNTj..AAA.0.0.BnDNTj.AWWqnFtlx7s',
            'xs': '41%3AvLFumcRD-SS7uQ%3A2%3A1728373764%3A-1%3A-1%3A%3AAcU1fhj_XjfnohyLfadCVO-p3iGh796JXibw5Jg1GA',
            'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728894183598%2C%22v%22%3A1%7D',
            'wd': '1901x569',
        }

        self.headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'sb=Sd0EZyd1ZLFTH1DgFE17E4Nu; datr=Sd0EZ6_llVPt6h1Plmpmd3gI; locale=id_ID; ps_l=1; ps_n=1; c_user=61566949410348; fbl_st=101536515%3BT%3A28806236; vpd=v1%3B868x648x2.000000037252903; dpr=0.71875; fr=14qcuyn423VjDBEpg.AWUbRST2euVKfsG4STFezFBJzfU.BnDNTj..AAA.0.0.BnDNTj.AWWqnFtlx7s; xs=41%3AvLFumcRD-SS7uQ%3A2%3A1728373764%3A-1%3A-1%3A%3AAcU1fhj_XjfnohyLfadCVO-p3iGh796JXibw5Jg1GA; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728894183598%2C%22v%22%3A1%7D; wd=1901x569',
            'origin': 'https://www.facebook.com',
            'priority': 'u=1, i',
            'referer': 'https://www.facebook.com/search/top?q=jokowi&locale=id_ID',
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

    def get_data(self, cursor=None, grup_name=None):
        
        data = {
            'av': '61566949410348',
            '__aaid': '0',
            '__user': '61566949410348',
            '__a': '1',
            '__req': '1p',
            '__hs': '20010.HYP:comet_pkg.2.1..2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1017311075',
            '__s': '61yulo:owd1mk:vvq2ns',
            '__hsi': '7425543944353986802',
            '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C17yUJ3odE98K361twYwJyE24wJwpUe8hwaG1sw9u0LVEtwMw65xO2OU7m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewyDwkUe9obrwh8lwUwgojUlDw-wSU8o4Wm7-2K1ywtUuwLKq2-azqwaW223908O3216xi4UK2K364UrwFg2fwxyo566k1FwgUjwOwWwjHDzUiwRK6E4-mEbUaU3yw',
            '__csr': 'gakQ6Zhkt34RPEJgHkZRZkx2-GqZTY9ip14QzV2l8SgLbsYBA4ifETRhqbGApmLhpLQJ6F4LhGDCZtaC9A_HACBKuEJFuayqDCKngyn-mF8WuvDAheEF38ix6UOWWyVEiCy8hGinz4aGqmFeUy8DDKUmwLDx28xq2uHyF9rDwNxS5-i36q4U6-2bwDyUmBxi260yEhKq11wk84OcCwzw8l0xwno7K4Q1OwPwgU2cwOxi0PawQw8a0aEw2AU1tQ0cSw05PXg55018S0LU1bU29w4MzE1zpE1raxa6m0OUdU0a-A0diwFw08uWm0gm',
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
            'variables': '{"count":5,"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"28163fb4-1f71-4039-9f7a-45273a7cc8aa","tsid":"0.29607292314943456"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"GROUPS_TAB"},"filters":[],"text":"'+(grup_name or '')+'"},"cursor":"'+(cursor or '')+'","feedbackSource":23,"fetch_filters":true,"renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":true}',
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
