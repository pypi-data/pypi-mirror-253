#!/usr/bin/env bash
# @Project      : AI @by PyCharm
# @Time         : 2023/11/8 08:53
# @Author       : betterme
# @Email        : 313303303@qq.com
# @Software     : PyCharm
# @Description  : https://mp.weixin.qq.com/s/uOcaKQkNROTXqFuKA3hznQ

docker run --name old-oneapi \
  -d --restart always \
  -p 3000:3000 \
  -e TZ=Asia/Shanghai \
  -v /root/one-api:/data \
  justsong/one-api

docker run --name Xoneapi \
  -d --restart always \
  -p 39001:3000 \
  --add-host="host.docker.internal:host-gateway" \
  -e SQL_DSN="root:chatllmchatllm@tcp(host.docker.internal:3306)/oneapi" -e TZ=Asia/Shanghai \
  -v /root/data/xapi:/data \
  justsong/one-api

docker pull calciumion/new-api:latest
docker run --name vip \
  -d --restart always \
  -p 39002:3000 \
  --add-host="host.docker.internal:host-gateway" \
  -e SQL_DSN="root:chatllmchatllm@tcp(host.docker.internal:3306)/oneapi" -e TZ=Asia/Shanghai \
  -v /root/data/xapi:/data \
  calciumion/new-api:latest

docker run --name oneapi \
  -d --restart always \
  -p 39000:3000 \
  --add-host="host.docker.internal:host-gateway" \
  -e SQL_DSN="oneapi:chatllmchatllm@tcp(host.docker.internal:3306)/oneapi" \
  -e MEMORY_CACHE_ENABLED=true -e SYNC_FREQUENCY=60 \
  -e BATCH_UPDATE_ENABLED=true \
  -e TZ=Asia/Shanghai \
  -v /www/data/oneapi:/data \
  justsong/one-api

# 16c32g --network="host"
docker run --name one-api \
  -d --restart always \
  -p 38889:3000 \
  --add-host="host.docker.internal:host-gateway" \
  -e SQL_DSN="root:chatllmchatllm@tcp(host.docker.internal:3306)/oneapi" \
  -e TZ=Asia/Shanghai \
  -v /www/data/oneapi:/data

justsong/one-api

# 16c32g --network="host"
docker run --name new-api \
  -d --restart always \
  -p 38888:3000 \
  --add-host="host.docker.internal:host-gateway" \
  -e SQL_DSN="root:chatllmchatllm@tcp(host.docker.internal:3306)/oneapi" \
  -e TZ=Asia/Shanghai \
  -e MEMORY_CACHE_ENABLED=true -e SYNC_FREQUENCY=60 \
  -e BATCH_UPDATE_ENABLED=true \
  -v /www/data/oneapi:/data \
  calciumion/new-api:latest

docker run --name new-api \
  -d --restart always \
  -p 38888:3000 \
  --add-host="host.docker.internal:host-gateway" \
  -e SQL_DSN="root:chatllmchatllm@tcp(host.docker.internal:3306)/oneapi" \
  -e TZ=Asia/Shanghai \
  -e MEMORY_CACHE_ENABLED=true -e SYNC_FREQUENCY=60 \
  -e BATCH_UPDATE_ENABLED=true \
  -v /www/data/oneapi:/data \
  calciumion/new-api:0.0.9.1

docker run --name new-api \
  -d --restart always \
  -p 39009:3000 \
  --add-host="host.docker.internal:host-gateway" \
  -e SQL_DSN="root:chatllmchatllm@tcp(host.docker.internal:3306)/oneapi" -e TZ=Asia/Shanghai \
  -e MEMORY_CACHE_ENABLED=true -e SYNC_FREQUENCY=60 \
  -e BATCH_UPDATE_ENABLED=true \
  -v /www/data/oneapi:/data \
  calciumion/new-api:latest

# 代理服务
docker run --name gpt3 \
  -d --restart always \
  -p 39003:3000 \
  --add-host="host.docker.internal:host-gateway" \
  -e SQL_DSN="root:chatllmchatllm@tcp(host.docker.internal:3306)/aiapi" -e TZ=Asia/Shanghai \
  -v /root/data/aiapi:/data \
  calciumion/new-api:latest
