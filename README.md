# Funds


## Step 1
**Open terminal window then..**
```shell
cd /path/to/base_dir && source start.sh
```
- ***Note*** server run on port **8000**
## Step 2
**Open terminal window then..**

`Must have enabled redis service on system `
```shell
cd /path/to/base_dir && source queue.sh
```

`Start request on end point`

| Method | End-Point                                                                                   |
| ------ |---------------------------------------------------------------------------------------------|
| Get    | http://127.0.0.1:8000/api/articles/?link=http://example.com&is_read=1or0&received_decimal=5 |

