import sys
import requests
import sconfig

slack_token = sconfig.slack_credentials("slack-credentials")["slack-token"]
messageURI = "https://slack.com/api/chat.postMessage?token=" + slack_token
getStatusURI = "https://slack.com/api/users.profile.get?token=" + slack_token
postStatusURI = "https://slack.com/api/users.profile.set?token=" + slack_token
channelParam = "&channel=%23find-a-slacker"


def slack_status(present):
    if present:
        message = "&profile=%7B%22status_text%22%3A%22At%20his%20desk%22%2C%22status_emoji%22%3A%22%3Aoffice%3A%22%7D"
    else:
        message = "&profile=%7B%22status_text%22%3A%22Somewhere%20else%22%2C%22status_emoji%22%3A%22%3Aquestion%3A%22" \
                  "%7D "
    full_uri = postStatusURI + message
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
    ipmsg = "FindASlacker system online at " + ip
    uri = messageURI + channelParam + "&text=" + ipmsg
    try:
        response = requests.post(url=uri)
    except KeyboardInterrupt:
        sys.exit()
    except:
        # e = sys.exc_info()[0]
        # print(e)
        pass
        # return (response.status_code)


def slack_message(message):
    uri = messageURI + channelParam + "&text=" + message
    try:
        response = requests.post(url=uri)
    except KeyboardInterrupt:
        sys.exit()
    except:
        # e = sys.exc_info()[0]
        # print(e)
        pass
        # return (response.status_code)


def slack_get_status_emoji():
    uri = getStatusURI
    try:
        response = requests.get(url=uri)
        responseData = response.json()
        statusEmoji = responseData['profile']['status_emoji']
    except:
        pass
    return statusEmoji

