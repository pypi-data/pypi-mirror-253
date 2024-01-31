from .config import Config
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

