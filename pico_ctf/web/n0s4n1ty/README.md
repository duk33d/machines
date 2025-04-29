# n0s4n1ty 1 (easy)

description : A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area.

Goal: `/root` ( Root RCE)

Takeaway from this ctf is
Whenever you get a shell on a remote machine, check `sudo -l`

- we all know that the famous command sudo which allows normal user to run commands/code with high privilegs
- using `sudo --help`

```text
...
-l, --list                    list user's privileges or check a specific
...
```

- so , by taking the hint from the ctf and running it we get ->

```text
Matching Defaults entries for www-data on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User www-data may run the following commands on challenge:
    (ALL) NOPASSWD: ALL
```
