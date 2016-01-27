import json
from twython import Twython
import random

def auth():
    with open("access.json", 'r') as f:
        db = json.load(f)
    return Twython(db["API_Key"], db["API_Secret"], db["Access_Token"], db["Access_Token_Secret"])

def get_tweet_text():
    us = random.randint(1,138)*"u"
    space = 140 - (len(us)+2)
    exclam = random.randint(0,space)*"!"
    fuck = "f"+us+"ck"+exclam
    if random.random() > 0.5:
        fuck.upper()
    return fuck


def main():
    twitter = auth()
    tweet = get_tweet_text()
    twitter.update_status(status=tweet)

if __name__ == "__main__":
    main()
