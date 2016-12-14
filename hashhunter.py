import time
import mraa
from twython import TwythonStreamer

# Search terms
TERMS = '#Hastag1, #Hastag2'

# GPIO pin number of LED
relay = mraa.Gpio(17)
relay.dir(mraa.DIR_OUT)
# Twitter application authentication
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        twit = data['text'].encode('utf-8')
                        print twit
                        print "ok"
                        if '#Hastag1' in twit:
                                relay.write(1)
                        #time.sleep(2)
                        else:
                                relay.write(0)

# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_S$
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        print "done"
