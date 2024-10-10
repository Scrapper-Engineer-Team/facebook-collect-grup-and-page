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
            'usida': 'eyJ2ZXIiOjEsImlkIjoiQXNsMTJ2OTE1amhmc3oiLCJ0aW1lIjoxNzI4Mzc3MDE4fQ%3D%3D',
            'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728377896982%2C%22v%22%3A1%7D',
            'wd': '1901x955',
            'fr': '1i6uKnaQ0hm55cKlf.AWUA3qFe_I0DcebbI5dtMuhi0a8.BnBPgG..AAA.0.0.BnBPgG.AWWuXbCt5do',
            'xs': '41%3AvLFumcRD-SS7uQ%3A2%3A1728373764%3A-1%3A-1%3A%3AAcWp8raZD3rZIsEE3qvcn4BKWAJYU5qllXmYvLsJnQ',
        }

        self.headers = {
            'accept': '*/*',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'sb=Sd0EZyd1ZLFTH1DgFE17E4Nu; datr=Sd0EZ6_llVPt6h1Plmpmd3gI; locale=id_ID; ps_l=1; ps_n=1; c_user=61566949410348; fbl_st=101536515%3BT%3A28806236; vpd=v1%3B868x648x2.000000037252903; dpr=0.71875; usida=eyJ2ZXIiOjEsImlkIjoiQXNsMTJ2OTE1amhmc3oiLCJ0aW1lIjoxNzI4Mzc3MDE4fQ%3D%3D; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1728377896982%2C%22v%22%3A1%7D; wd=1901x955; fr=1i6uKnaQ0hm55cKlf.AWUA3qFe_I0DcebbI5dtMuhi0a8.BnBPgG..AAA.0.0.BnBPgG.AWWuXbCt5do; xs=41%3AvLFumcRD-SS7uQ%3A2%3A1728373764%3A-1%3A-1%3A%3AAcWp8raZD3rZIsEE3qvcn4BKWAJYU5qllXmYvLsJnQ',
            'origin': 'https://web.facebook.com',
            'priority': 'u=1, i',
            'referer': 'https://web.facebook.com/search/pages/?q=pecinta%20kucing',
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

    def get_data(self, cursor=None, page_name=None):
        data = {
            'av': '61566949410348',
            '__aaid': '0',
            '__user': '61566949410348',
            '__a': '1',
            '__req': '6e',
            '__hs': '20004.HYP:comet_pkg.2.1..2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1017142191',
            '__s': 'ib7tzi:nu1rv9:trtlcb',
            '__hsi': '7423326526314549929',
            '__dyn': '7AzHK4HwkEng5K8G6EjBAg5S3G2O5U4e2C1jyUW3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320om78c87m221Fwgo9oO0-E4a3a4oaEnxO0Bo7O2l2Utwqo31wiE567Udo5qfK0zEkxe2GewGwkUe9obrwh8lwUwgojUlDw-wUwxwjFovUaU3VwLKq2-azqwaW223908O3216xi4UK2K364UrwFg2fwxyo566k1FwgU4q3G1eKufxa3mUqwjVqwLwHw',
            '__csr': 'g9v0xYA44yR25dNkIIt4SB5KRiFrqlFkz9kBOb8AhZOsLZr4YgBjV5AWqOOrDGDXD8FlJJd95J9V9pmQFFUJoyAGZ5y9eUPUGczGDzHGbiCx2l0-AADAyEtx29xa3vAyXK4FESteu8y88XVonxiu7Ehxi784i1xxO5o8oy15xicxC5UK8wbyE9UcEC0FofU13U26wio1WU0SG05tE2PwDw0kmo0129k0bLg1No1H85102QEdo3iw1Ie0ki3m019ex601W5w2cA0sWUiw',
            '__comet_req': '15',
            'fb_dtsg': 'NAcP_bN-6DoAMluHrFrjqk01H-3i1rnc7GL-w5olG_Dnz7GKWFMwNqA:41:1728373764',
            'jazoest': '25335',
            'lsd': 'JpFwBoI34LT29ntJvA5nJu',
            '__spin_r': '1017142191',
            '__spin_b': 'trunk',
            '__spin_t': '1728377893',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'SearchCometResultsPaginatedResultsQuery',
            'variables': '{"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"35a2912c-3433-4960-9b9d-655f35c5d5e9","tsid":"0.4556642246912965"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"PAGES_TAB"},"filters":[],"text":"'+(page_name or '')+'"},"count":5,"cursor":"'+ (cursor or '') +'","feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider":true,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":false,"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '8659071750823469',
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

        results = data
        return results