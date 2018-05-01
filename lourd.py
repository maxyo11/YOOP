import json
import sys
import os
import time
import random
import base64
import collections
import urllib
import hmac
import hashlib
import  requests




def percentEncode(s):
    return  urllib.quote(s,safe='_')



def createNonce():
    nonce = []
    for i in range(0, 24):
        nonce.append(str(random.randint(0,9)))
        return base64.b64encode(''.join(nonce))

def collectSignParams(signature_parameters,status):
    if status is not None:
        signature ['status'] = status

    for k,v in url_parameters.items():
        signature_parameters[k]=v
    return signature_parameters


def createSignParamString(signature_parameters):
    signature_parameters = collections.OrderedDict(sorted(signature_parameters.items()))
    param_string = ''
    counter = 0
    length = len(signature_parameters)
    for k,v in signature_parameters.items():
        param_string = param_string + percentEncode(k) + '=' + percentEncode(v)
        if counter < length - 1:
            param_string = param_string + '&'
            counter = counter + 1
    return param_string

def createOauthSignature(oauth_parameters,url,url_parameters, status, oauth_consumer_secret, oauth_token_secret):
    http_method = 'post'
    signature_parameters = oauth_parameters.copy()
    signature_parameters = collectSignParams(signature_parameters,status)
    signature_param_string = createSignParamString(signature_parameters)
    signature_base_string = http_method.upper() + '&' + percentEncode(url) + '&' + percentEncode(signature_param_string)
    signing_key = percentEncode(oauth_consumer_secret) + '&' + percentEncode((oauth_token_secret))
    signature = hmac.new (signing_key, signature_base_string, hashlib.sha1)
    base64.b64decode(signature.digest())

def createOauthString (oauth_parameters):
    oauth_parameters = collections.OrderedDict(sorted(oauth_parameters.items()))
    oauth_string ='OAuth'
    counter = 0
    length = len(oauth_parameters)
    for k,v in oauth_parameters.items():
        oauth_string = oauth_string + percentEncode(k) + '=' + "" + percentEncode(v) + ""
        if counter < length - 1:
            oauth_string = oauth_string + ',' + ''
            counter = counter + 1
    return  oauth_string





def tPosts():
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    url_parameters = {}
    status = 'Hello bro'
    oauth_parameters = {}
    oauth_consumer_key = OoeDEgkX47RFyKcgKGplhg23Q
    oauth_token = 989848008694083584-6ZReWbJgEIdqheN8LbO3d9FIlitUNhp
    oauth_version = '1.0'
    oauth_timestamp = str(time.time())
    oauth_nonce = createNonce()
    oauth_signature_method = 'HMAC-SHA1'
    oauth_parameters.update({'oauth_consumer_key':oauth_consumer_key,'oauth_token':oauth_token,'oauth_version':oauth_version, 'oauth_timestamp':oauth_timestamp,'oauth_nonce':oauth_nonce})
    oauth_consumer_secret = 4o0jJ8tNmFPlSbkyy8lMDaYazXpIc1f1GF21phvlpy28aPXVgm
    oauth_token_secret = vLb5aLG4VOoZQBD2A4BCsb2DCZ8QhogR6A8Ly7OjUXxbL
    oauth_signature = createOauthSignature(oauth_parameters,url,url_parameters, status, oauth_consumer_secret, oauth_token_secret)
    oauth_parameters.update({'oauth_signature':oauth_parameters})
    oauth_string = createOauthString (oauth_parameters)
    header_string = {
        "Accept":"*/*",
        "Connection": "close",
        "User-Agent":"OAuth gen v0.4.4",
        "Content_Type":"application/x-www-form-urlencoded",
        "Authorization": oauth_string,
        "Content-Length":"100",
        "Host": "api.twitter.com"

    }

        payload = {'status': status}


    r = requests.post(url,params = url_parameters, headers=headers, data=payload)
    print r.status_encode










if (__name__ == "main"):
    tPosts()

