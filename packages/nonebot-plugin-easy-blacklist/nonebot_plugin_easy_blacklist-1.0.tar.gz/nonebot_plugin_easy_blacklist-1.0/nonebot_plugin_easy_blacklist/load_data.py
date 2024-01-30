from nonebot.log import logger
import json
import aiofiles
from . import api

with open("./data/blacklist_by.json","r",encoding="utf_8") as j:
    j_ = json.load(j)
    j.close()
logger.success("正在初始化黑名单")
for k in j_:
    api.add_black(k,j_[k][1],j_[k][2],j_[k][3])
logger.success("初始化成功")
#print(j_)
async def save_list():
   # print(j_)
    async with aiofiles.open("./data/blacklist_by.json","w+",encoding="utf_8") as f:
        await f.write(json.dumps(j_))
        await f.close()