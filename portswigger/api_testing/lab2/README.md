# Lab: Finding and exploiting an unused API endpoint

description : To solve the lab, exploit a hidden API endpoint to buy a Lightweight l33t Leather Jacket. You can log in to your own account using the following credentials: `wiener:peter`.

analysis:

- inspecting the requests , i noticed paramter `redir=PRODUCT` -> which i thought it's might be added to the URL and we could manipulate it making the vulnerable server making undesired actions
- after several trials -> nothing
- inspecting js files -> nothing
- inspecting the request that retrives the price for product
`/api/products/1/price`
- Changing the METHOD -> `PATCH` and using the verbose errors -> updating it to 0$ -> lab solved
