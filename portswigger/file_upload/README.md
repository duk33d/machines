# Testing For File Upload  Methodology

## things u need to obesrve while u testing file upload vulnerablity

- Is the response time that the server takes to responde to ur request, some times servers sends ur file to a sandbaox to check if the file doesn't contain any malicious code before actually saving it to actuall file system of the server
- may the application is only validating content type
- we might try to upload xml file -> testing xxe
- we might try to get ssrf via file meta data

## Defense Techniques (Bypassing Techniques)

- Black list : -> use many different extensions till one gets bypass
- White list : -> use null byte technique : %00.jpg
- validating the content of the image : the server usually validating the magic bytes, in this case u might insert ur shell inside the image

  -----------------------
  - `ÿØÿá??Exif␀␀`      |
  - `ÿØÿî`               |-> jpeg , jpg
  - `ÿØÿà␀␐JFIF␀␁`      |
  - `ÿØÿÛ`               |
  -----------------------
  - `ÿØÿà` -> jpg
  - `‰PNG␍␊␚␊` -> png
  - [list of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
