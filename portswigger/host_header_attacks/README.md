# Host header attacks

this should be a general methodology for testting for it

- if the target is reseting password old way (press this link to reset ur password) or other functionality using this way -> we might test it here
  - we might try direct host header manipulattion or try adding header like `X-Host` and so on

## Hight level methodology

1. Supply an arbitrary Host header
2. Check for flawed validation
    - u might be able to insert ur payload via the port
3. Send ambiguous requests
    - inject duplicate Host headers
4. Supply an absolute URL

    ``` text
    GET https://vulnerable-website.com/ HTTP/1.1
    Host: bad-stuff-here
    ```

5. Add line wrapping
    - u might not be able to do it via brup  -> try curl

    ```text
    GET /example HTTP/1.1
        Host: bad-stuff-here
    Host: vulnerable-website.com
    ```

6. Inject host override headers
    - X-Forwarded-Host
    - X-Host
    - X-HTTP-Host-Override
    - Forwarded
7. HTTP Request smuggling techniques

## Portswigger labs

1. Password reset poisoning
2. Web cache poisoning
3. Exploiting classic server-side vulnerabilities
4. Bypassing authentication
5. Virtual host brute-forcing
6. Routing-based SSRF
7. Connection state attacks
