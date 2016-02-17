import sys
import re
import json
import http #http.py

ENABLE_DEBUG_PRINT = False

def print_usage_and_exit():
    print "Usage: python which-bci-api.py b6525454-19f2-45c6-af32-8b1a795b2d37"
    sys.exit()
    
def print_create_wallet_info_and_exit(api_code):
    print "Your API code, %s, is a valid Create-Wallet API code." % api_code
    print("\tCreate-Wallet API codes are requested here: "
          "https://blockchain.info/api/api_create_code")
    print("\tCreate-Wallet API Documentation can be found here: "
          "https://blockchain.info/api/create_wallet")
    print("\tTo request a Receive-Payments API code instead, visit: "
          "https://api.blockchain.info/v2/apikey/request/")
    sys.exit()

def print_receive_payments2_info_and_exit(api_code):
    print "Your API code, %s, is a valid Receive-Payments API code." % api_code
    print("\tReceive Payments API codes are requested here: "
          "https://api.blockchain.info/v2/apikey/request/")
    print("\tReceive Payments API Documentation can be found here: "
          "https://blockchain.info/api/blockchain_wallet_api")
    sys.exit()

def print_error_and_exit():
    print "Could not parse blockchain.info response -- is it down?"
    sys.exit()
    
def looks_like_uuid(data):
    return re.match(
        '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', data)

def test_create_wallet(api_code):
    url = ("https://blockchain.info/block-height/0?format=json&api_code=%s" %
           api_code)
    resp = http.fetch_url(url)
    dprint("Resp = %s" % str(resp))
    if resp == "Unknown API Key":
        return False
    try:
        if (json.loads(resp)['blocks'][0]['hash'] == 
            '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'):
            return True
        else:
            print_error_and_exit()
    except Exception:
        print_error_and_exit()

def test_receive_payments2(api_code):
    url = (("https://api.blockchain.info/v2/receive?key=%s&xpub=xpub6CDMbK5HbM"
            "5HjqaQq7a8u9icSSS4b8PewjcKtmUakGFQfft6TT9Xow8MScj1F13YWTjLFESkVbs"
            "qvFukKf8msyGLkEAE14ji8o554NPHmca&"
            "callback=http%%3A%%2F%%2Fgoogle.com") %
           api_code)
    resp = http.fetch_url(url)
    json_obj = None
    try:
        json_obj = json.loads(resp)
    except ValueError:
        print_error_and_exit()
    if 'message' in json_obj and json_obj['message'] == 'API Key is not valid':
        return False
    if 'address' in json_obj:
        return True
    else:
        print_error_and_exit()

def main():
    """Get API key as parameter and test it."""
    if len(sys.argv) != 2:
        print_usage_and_exit

    api_code = None
    try:
        api_code = sys.argv[1]
    except Exception:
        print_usage_and_exit()
    
    if looks_like_uuid(api_code):
        print "Your code looks like valid UUID format."
    else:
        print "Your argument is not a valid UUID. Please verify it."
        sys.exit()
    
    if test_create_wallet(api_code):
        print_create_wallet_info_and_exit(api_code)
    else:
        print "Your code is not a valid Create-Wallet API code."
    
    if test_receive_payments2(api_code):
        print_receive_payments2_info_and_exit(api_code)
    else:
        print "Your code is not a valid Receive-Payments API code."
        
def dprint(data):
    if ENABLE_DEBUG_PRINT:
        print "%s" % data

if __name__ == "__main__":
    main()
