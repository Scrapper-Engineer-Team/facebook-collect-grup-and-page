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
            'xs': '41%3AvLFumcRD-SS7uQ%3A2%3A1728373764%3A-1%3A-1%3A%3AAcW4-V0qYRs0MPEiztzLrnYP8X187i1uGRM7xugPtw',
            'fr': '1LWdfKpaq0uVKFKdR.AWWwO2ZUo326LhOx4JzX7XlE1QY.BnBOnP..AAA.0.0.BnBPCg.AWVCIwkTlhY',
            'usida': 'eyJ2ZXIiOjEsImlkIjoiQXNsMTJ2OTE1amhmc3oiLCJ0aW1lIjoxNzI4Mzc3MDE4fQ%3D%3D',
            'wd': '1072x955',
            'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728377896982%2C%22v%22%3A1%7D',
        }

        self.headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://web.facebook.com',
            'priority': 'u=1, i',
            'referer': 'https://web.facebook.com/search/groups?q=jual%20beli%20hp%20second%20bandung%20murah',
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
            'x-fb-lsd': 'JpFwBoI34LT29ntJvA5nJu',
        }

    def get_data(self, cursor=None, grup_name=None):
        data = {
            'av': '61566949410348',
            '__aaid': '0',
            '__user': '61566949410348',
            '__a': '1',
            '__req': '2d',
            '__hs': '20004.HYP:comet_pkg.2.1..2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1017142191',
            '__s': 'z99z9i:nu1rv9:trtlcb',
            '__hsi': '7423326526314549929',
            '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C1jyUW3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81xoswMwto886C11wBz83WwgEcEhwGxu782lwv89kbxS1Fwc61awkovwRwlE-U2exi4UaEW2G1jwUBwJK14xm1Wxfxmu3W3y261eBx_wHwfC2-VEbUGdG0HE88cA0z8c84q58jyUaUcojxK2B08-269wkopg6C13whEeE4WVU-4EdrxG1fBG2-2K',
            '__csr': 'gsgANct2tgDOl3v8Jv9eHsZ9sItkDjnbpRK-QRql8FaGIxmAlqkD8LRIiRaBjVaAVaFuKbBvKsyz8FemVV9pXiCDyWyQnQm8AXzbyEOeGueKeiCx2q3W9DAyEtx29xa3vAyVUpxleu8y89-m5UkDwMxi784i1-xm268whokz8pxuby82UG2u3a9wam3-0g-0xE4C0uK0dGw1nq0IU9U01mvQ0bLg1No1H80Oi3m07BE1h8do04AW01Wnw2cA0sWUiw',
            '__comet_req': '15',
            'fb_dtsg': 'NAcP_bN-6DoAMluHrFrjqk01H-3i1rnc7GL-w5olG_Dnz7GKWFMwNqA:41:1728373764',
            'jazoest': '25335',
            'lsd': 'JpFwBoI34LT29ntJvA5nJu',
            '__spin_r': '1017142191',
            '__spin_b': 'trunk',
            '__spin_t': '1728377893',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'SearchCometResultsPaginatedResultsQuery',
            'variables': '{"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"18909dc6-1a76-4ca0-85ce-9b9065f48f78","tsid":"0.4260696150483687"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"GROUPS_TAB"},"filters":[],"text":"'+(grup_name or '')+'"},"count":5,"cursor":"' + (cursor or '') + '","feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '8659071750823469',
        }

        response = requests.post('https://web.facebook.com/api/graphql/', cookies=self.cookies, headers=self.headers, data=data)
        return response.json()

    def process(self):
        cursor = None
        while True:
            data = self.get_data(cursor)
            if not data or 'data' not in data or 'serpResponse' not in data['data']:
                print("No more data to fetch or error in response.")
                break

            results = data
            if results['data']['serpResponse']['results']['edges']:
                print(results)
                logger.success(results)
                cursor = results['data']['serpResponse']['results']['page_info']['end_cursor']
            else:
                break
            
            # Add a delay to avoid hitting rate limits
            # time.sleep(1)