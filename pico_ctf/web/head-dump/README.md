# head-dump (easy)

summary : misconfigured API allow access to heap

Analysis :

- just exploring the posts -> find swager docs
- misconfigured API allow public users to dump the heap
- dowload the heap file and  `strings ~/Desktop/machines/machines/pico_ctf/web/head-dump/heapdump-1743272085585.heapsnapshot | grep -i "pico"` ( cat would work as well )
- we found the flag
