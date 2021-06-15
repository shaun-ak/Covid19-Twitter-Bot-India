import tweepy
import logging

logger = logging.getLogger()

def create_api():
    consumer_key = "DC4IiQslAcPw8cCP2aQAzhiKm"
    consumer_secret = "3JKL7gTxinLeICRuLj4R0rH2aMyaio8NpfpwBMHsno87n2Wo3P"
    access_token = "1388032984809283593-z8mmgLcp3mkHmWEWpfYpWgrWpMpQJm"
    access_token_secret = "QDh8w8TC2LlfmkdI3Ax5bt8QT7TB8Sd8iG7BEGbvgINzS"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api