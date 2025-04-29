# Mr Robot CTF

first step in every CTF **nmap**

- 80 , 443 ports are open , both are the same web app , 22 -> ssh
  - giving us a shell with certain commands
        - prepare
        - fsociety
        - inform
        - question
        - wakeup
        - joing
whoismrrobot.com
- tech the web app using
  - php 5.5.29
  - wordpress 4.3.1 -> seems to be vulnerable to RCE -> authenticated users
  - db : mysql
  - web server : apache
  - jquery 1.11.3   /  1.2.1
  - os : linux
- ENDPOINT /xmlrpc.php -> faultCode:32700
- robots.txt -> `fsocity.dic` , `key-1-of-3.txt`
- an interesting header `X-Mod-Pagespeed: 1.9.32.3-4523`
- sending POST request ro /xmlrpc.php -> `faultCode` : 32700 -> line number:32700 in the wordlist "6756"
- i have noticed that the login page returns a explicit error message but didn't tought that i should brute force the user name , i was stuck there for like 2hrs
  - brute forcing the username&password using hydra
    -`hydra -L fsocity.dic -p P@$sw0Rd 10.10.141.211 http-post-form "/wp-login.php:log=^USER^&pwd=^PWD^:Invalid username" -t 50`
    - `hydra -l elliot -P ./fsocity.dic 10.10.141.211 http-post-form "/wp-login.php:log=^USER^&pwd=^PWD^:is incorrect." -t 50`
    - essintially what this commands doing is
      - using tool called *hydra* and pass to it list of usernames one (-L flag) and static username (-l elliot)
      - the same for the password , ip -> for the destination , http-post-form to use this credentials in post request
      - `"/path_to_form:paramter_one=^USER^&parameter_two=^PWD^:value for invalid login attempt"` -t 50 -> number of threads i think
      - the ^USER^&^PWD^ are placeholders for the values the are currently used for current login attempt,
- after cracking the username and the password we got an access to the wp-admin panel (we have access to the editor tab)
  - configuring editor to run custom php code gives us a reverse shell
- moving to /home -> we found that there is a user with username `robot` and have backup password-hashed which is publicly accessible
- john md5.hash --wordlist=fsocity.dic --format=Raw-MD5 -> cracking the rawd password using john the ripper
- `python -c 'import pty;pty.spawn("/bin/bash")'` -> to get interactive shell (terminal) -> su robot -> we got the second key
- in a typical case i would use linux-exploit-suggester to try to escalate my privilages to root but the home directory is owend by the root so we can't write into it :"
- find / -perm +6000 2>/dev/null | grep '/bin/'
- [GTFOBins](https://gtfobins.github.io/) -> a great resource to abuse binaries that you find in the system

X-Powered-By: PHP/5.5.29
X-Pingback: <https://10.10.141.211/xmlrpc.php>
