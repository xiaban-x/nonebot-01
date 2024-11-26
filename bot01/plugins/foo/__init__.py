from nonebot import get_plugin_config   
from nonebot.plugin import PluginMetadata, on_command
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import CommandArg

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="foo",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

weather = on_command("天气", rule=to_me(), aliases={"weather", "查天气"}, priority=100, block=True)

@weather.handle()
async def handle_function(args: Message = CommandArg()):
    if location := args.extract_plain_text():
        await weather.finish(f"今天{location}的天气是...")
    else:
        await weather.finish("请输入地名")

