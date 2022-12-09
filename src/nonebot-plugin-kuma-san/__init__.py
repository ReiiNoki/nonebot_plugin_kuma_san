from nonebot import on_command, logger

from nonebot.adapters.onebot.v11 import Bot, MessageEvent

from .utils.common import ServiceException
from .services.stage_service import list_stage

__plugin_meta__ = nonebot.plugin.PluginMetadata(
    name='熊老板-喷喷喷场地信息查询',
    description='一个查询斯普拉遁3场地信息的插件',
    usage='用法： 对我说 “reg(涂地)/chal(真格挑战)/open(真格区域)/baito(打工)/fest(祭典)/x(x段) + (可选)now/next\n例如‘baito‘直接查询打工的场地；’baito now‘查询现在打工的场地',
    extra={'version': '1.0.0'}
)

baito = on_command('baito', aliases={'打工'}, priority=2, block=True)


@baito.handle()
async def _(bot: Bot, event: MessageEvent):
    args = event.get_message().extract_plain_text().split(' ')
    n = len(args)

    if n == 1:
        result_str = '以下是接下来的鲑鱼跑场地：\n' + await request('salmon_run', 'schedule')
    elif args[1] == 'now':
        result_str = '现在的鲑鱼跑场地：\n' + await request('salmon_run', args[1])
    elif args[1] == 'next':
        result_str = '接下来的鲑鱼跑场地：\n' + await request('salmon_run', args[1])
    else:
        result_str = '你发错命令了！多来打工锻炼锻炼吧！'

    await baito.send(message='快来给我打工，成为传说打工人吧，少年！\n' + result_str, at_sender=True)


regular_stage = on_command('reg', aliases={'涂地'}, priority=2, block=True)


@regular_stage.handle()
async def _(bot: Bot, event: MessageEvent):
    args = event.get_message().extract_plain_text().split(' ')
    n = len(args)

    if n == 1:
        result_str = '以下是接下来的涂地场地：\n' + await request('regular', 'schedule')
    elif args[1] == 'now':
        result_str = '现在的涂地场地：\n' + await request('regular', args[1])
    elif args[1] == 'next':
        result_str = '接下来的涂地场地：\n' + await request('regular', args[1])
    else:
        result_str = '你发错命令了！多来打工锻炼锻炼吧！'

    await regular_stage.send(message=result_str, at_sender=True)


open_stage = on_command('open', aliases={'开放'}, priority=2, block=True)


@open_stage.handle()
async def _(bot: Bot, event: MessageEvent):
    args = event.get_message().extract_plain_text().split(' ')
    n = len(args)

    if n == 1:
        result_str = '以下是接下来的真格开放场地：\n' + await request('open', 'schedule')
    elif args[1] == 'now':
        result_str = '现在的真格开放场地：\n' + await request('open', args[1])
    elif args[1] == 'next':
        result_str = '接下来的真格开放场地：\n' + await request('open', args[1])
    else:
        result_str = '你发错命令了！多来打工锻炼锻炼吧！'

    await open_stage.send(message=result_str, at_sender=True)


challenge_stage = on_command('chal', aliases={'挑战'}, priority=2, block=True)


@challenge_stage.handle()
async def _(bot: Bot, event: MessageEvent):
    logger.info('message => ' + event.get_message().extract_plain_text())
    args = event.get_message().extract_plain_text().split(' ')
    n = len(args)
    if n == 1:
        result_str = '以下是接下来的真格挑战场地：\n' + await request('challenge', 'schedule')
    elif args[1] == 'now':
        result_str = '现在的真格挑战场地：\n' + await request('challenge', args[1])
    elif args[1] == 'next':
        result_str = '接下来的真格挑战场地：\n' + await request('challenge', args[1])
    else:
        result_str = '你发错命令了！多来打工锻炼锻炼吧！'

    await challenge_stage.send(message=result_str, at_sender=True)


x_stage = on_command('x', aliases={'x段赛'}, priority=2, block=True)


@x_stage.handle()
async def _(bot: Bot, event: MessageEvent):
    logger.info('message => ' + event.get_message().extract_plain_text())
    args = event.get_message().extract_plain_text().split(' ')
    n = len(args)
    if n == 1:
        result_str = '以下是接下来的x段赛场地：\n' + await request('x', 'schedule')
    elif args[1] == 'now':
        result_str = '现在的x段赛场地：\n' + await request('x', args[1])
    elif args[1] == 'next':
        result_str = '接下来的x段赛场地：\n' + await request('x', args[1])
    else:
        result_str = '你发错命令了！多来打工锻炼锻炼吧！'

    await x_stage.send(message=result_str, at_sender=True)


fest_stage = on_command('fest', aliases={'祭典'}, priority=2, block=True)


@fest_stage.handle()
async def _(bot: Bot, event: MessageEvent):
    logger.info('message => ' + event.get_message().extract_plain_text())
    args = event.get_message().extract_plain_text().split(' ')
    n = len(args)
    if n == 1:
        result_str = '以下是接下来的祭典场地：\n' + await request('fest', 'schedule')
    elif args[1] == 'now':
        result_str = '现在的祭典场地：\n' + await request('fest', args[1])
    elif args[1] == 'next':
        result_str = '接下来的祭典场地：\n' + await request('fest', args[1])
    else:
        result_str = '你发错命令了！多来打工锻炼锻炼吧！'

    await fest_stage.send(message=result_str, at_sender=True)


help_command = on_command('help', priority=2, block=True)


@help_command.handle()
async def _(bot: Bot, event: MessageEvent):
    text = get_help_text()
    await help_command.send(message=text, at_sender=True)


async def request(name, time):
    try:
        results = await list_stage(name, time)
        result_str = ''
        for result in results:
            result_str += result
        return result_str
    except ServiceException as e:
        results = e.message


def parse_time(time):
    if time == 'now' or time == 'next':
        return time
    elif time == 'plan':
        return 'schedule'
    else:
        return None


def get_help_text() -> str:
    with open("./src/plugins/splat3_stage_helper/help.txt", 'r', encoding="utf-8") as f:
        help_text = f.read()
    return help_text

