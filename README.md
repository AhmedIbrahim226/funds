# Funds


## Step 1
**Open terminal window then..**
```shell
cd /path/to/funds && source start.sh
```
- ***Note*** server run on port **8000**
## Step 2
**Open terminal window then..**

`Must have enabled redis service on system `
```shell
cd /path/to/funds && source queue.sh
```

`Start request on end point`

| Method | End-Point                     | Body                                                                                        |
| ------ | ----------------------------- |:--------------------------------------------------------------------------------------------|
| Get    | http://127.0.0.1/api/articles | {"link": "https://google.com",<br/>"is_read": 1 or 0,<br />"received_decimal": 0.55555<br />}|

