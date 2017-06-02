import json
import sys
import requests
import sconfig

uri = sconfig.slack_credentials("slack-credentials")["slack-webhook"]
slack_token = sconfig.slack_credentials("slack-credentials")["slack-token"]


def slack_status(present):
    base_uri = "https://slack.com/api/users.profile.set?token="
    if present:
        message = "&profile=%7B%22status_text%22%3A%22In%20his%20office%22%2C%22status_emoji%22%3A%22%3Aoffice%3A%22%7D"
    else:
        message = "&profile=%7B%22status_text%22%3A%22Somewhere%20else%22%2C%22status_emoji%22%3A%22%3Aquestion%3A%22" \
                  "%7D "
    full_uri = base_uri + slack_token + message
    try:
        response = requests.get(full_uri)
    except KeyboardInterrupt:
        sys.exit()
    except:
        # e = sys.exc_info()[0]
        # print(e)
        pass

    # print full_uri
    return response.status_code
    # print(response.status_code)


def slack_ip(ip):
    ipmsg = dict(text="FindASlacker system online at " + ip)
    JSONMessage = json.dumps(ipmsg)
    try:
        response = requests.post(url=uri, data=JSONMessage)
    except KeyboardInterrupt:
        sys.exit()
    except:
        # e = sys.exc_info()[0]
        # print(e)
        pass
        # return (response.status_code)


def slack_message(message):
    msg = dict(text=message)
    JSONMessage = json.dumps(msg)
    try:
        response = requests.post(url=uri, data=JSONMessage)
    except KeyboardInterrupt:
        sys.exit()
    except:
        # e = sys.exc_info()[0]
        # print(e)
        pass
        # return (response.status_code)
