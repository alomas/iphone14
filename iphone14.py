import json

import requests


def getphones():
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)"
    }

    response = requests.get(
        url="https://www.apple.com/shop/pickup-message-recommendations?mts.0=regular&mts.1=compact&cppart=UNLOCKED/US"
            "&searchNearby=true&store=R182&product=MQ303LL/A",
        headers=headers)
    response.encoding = 'utf-8'
    content = response.content
    phonesdict = json.loads(content)
    return phonesdict


def main():
    phonesdict = getphones()
    pickupmessage = phonesdict["body"]["PickupMessage"]
    stores = pickupmessage["stores"]
    for store in stores:
        partsavailability = store["partsAvailability"]
        for part in partsavailability:
            partdetail = partsavailability[part]
            if partdetail["storePickEligible"]:
                proddetail = partdetail["messageTypes"]["regular"]
                prodname = proddetail["storePickupProductTitle"]
                storequote = proddetail["storePickupQuote"]
                print(f'{prodname} ({part}) - {storequote}')


if __name__ == '__main__':
    main()
