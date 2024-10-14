import requests
import time
from loguru import logger

class GrupName:
    def __init__(self):
        self.cookies = {
            'sb': 'VE0NZ9IdfXRvmsQi-sHI1mP1',
            'ps_l': '1',
            'ps_n': '1',
            'dpr': '0.71875',
            'c_user': '61567323625343',
            'datr': 'VE0NZ9GVivINzaiWdUdyuJbK',
            'xs': '39%3A2NFO8d02hllsCw%3A2%3A1728925031%3A-1%3A-1',
            'fr': '0r40L8IAJTaookKLp.AWWhyiIW31DQcbEGaIvXe2juVFQ.BnDU1U..AAA.0.0.BnDU1p.AWXyeREdwRo',
            'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728925036451%2C%22v%22%3A1%7D',
            'wd': '1072x955',
        }

        self.headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'sb=VE0NZ9IdfXRvmsQi-sHI1mP1; ps_l=1; ps_n=1; dpr=0.71875; c_user=61567323625343; datr=VE0NZ9GVivINzaiWdUdyuJbK; xs=39%3A2NFO8d02hllsCw%3A2%3A1728925031%3A-1%3A-1; fr=0r40L8IAJTaookKLp.AWWhyiIW31DQcbEGaIvXe2juVFQ.BnDU1U..AAA.0.0.BnDU1p.AWXyeREdwRo; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728925036451%2C%22v%22%3A1%7D; wd=1072x955',
            'origin': 'https://www.facebook.com',
            'priority': 'u=1, i',
            'referer': 'https://www.facebook.com/search/groups/?q=jual%20beli',
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
            'x-fb-friendly-name': 'SearchCometResultsPaginatedResultsQuery',
            'x-fb-lsd': 'Q7ykn7yQ5dKl1_yrAD2aiQ',
        }

    def get_data(self, cursor=None, grup_name=None):
        
        data = {
            'av': '61567323625343',
            '__aaid': '0',
            '__user': '61567323625343',
            '__a': '1',
            '__req': '1s',
            '__hs': '20010.HYP:comet_pkg.2.1..2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1017314811',
            '__s': '0cdn3r:0ccfn8:2h7uku',
            '__hsi': '7425676474822099839',
            '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C1jyUW3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81xoswMwto886C11wBz83WwgEcEhwGxu782lwv89kbxS1Fwc61awkovwRwlE-U2exi4UaEW2G1jwUBwJK14xm1Wxfxmu3W3y261eBx_wHwoE2mwLKq2-azqwaW223908O3216xi4UK2K364UrwFg2fwxyo566k1FwgU4q3G1eKufxa3mUqwjVqwLwHwea',
            '__csr': 'gaIInklsp5igVsBl4Z-xZht8TcDRtEJJfaL_ZTbnWtd5EH47HhQPlFQLFnF4Qi4puJ94QJ6JajGkCU-imrCAKmaXrAAx7CCBQFqzotAHJ2CA6oXCxvUgzUeuUjyXXzqxyEKuqeyEkx63q68e8jy8mwloc89pEK2y2u368grwoU3LwrQ0gK0xUaK1twWwkU2twnU19Uow13106_w05AGxm3B01xO0UU0jcw1CO01efw0uK85-1qwro',
            '__comet_req': '15',
            'fb_dtsg': 'NAcOGp2h60DyFgmmbeJKTNwI_mTzLUNI6auXUQFN7KBiI2qMfWAbJLg:39:1728925031',
            'jazoest': '25395',
            'lsd': 'Q7ykn7yQ5dKl1_yrAD2aiQ',
            '__spin_r': '1017314811',
            '__spin_b': 'trunk',
            '__spin_t': '1728925033',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'SearchCometResultsPaginatedResultsQuery',
            'variables': '{"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"6dd38867-99e4-4643-ba88-98f3523db8f1","tsid":"0.9445569633050603"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"GROUPS_TAB"},"filters":[],"text":"'+(grup_name or '')+'"},"count":5,"cursor":"'+(cursor or '')+'","feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false}',
            'server_timestamps': 'true',
            'doc_id': '8668325726557956',
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
