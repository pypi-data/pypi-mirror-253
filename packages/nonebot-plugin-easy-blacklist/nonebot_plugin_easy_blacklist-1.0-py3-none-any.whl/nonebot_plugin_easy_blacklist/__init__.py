import os
from .config import Config
from nonebot.log import logger
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="黑名单插件",
    description="一个轻量级的黑名单插件,支持api接入全平台,内存占用优化中",
    usage="高效率,支持多消息场景",
    type="application",
    config=Config,
    homepage="https://github.com/bingqiu456/nonebot-plugin-easy-blacklist",
    supported_adapters={"~onebot.v11"}
)

if not os.path.isdir("data"):
    os.mkdir("data")
    logger.warning("检测到资源文件夹data不存在,已为你创建")

if not os.path.isfile("./data/blacklist_by.json"):
    logger.warning("检测到黑名单存储文件不存在,已创建")
    with open("./data/blacklist_by.json","w+",encoding="utf_8") as f:
        f.write("{}")
        f.close()