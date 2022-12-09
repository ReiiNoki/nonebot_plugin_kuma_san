from ...splat3_stage_helper.utils.constants import *


def parse_p1(stage_type) -> str:
    if stage_type == 'regular':
        return regular
    elif stage_type == 'open':
        return bankara_open
    elif stage_type == 'challenge':
        return bankara_challenge
    elif stage_type == 'fest':
        return fest
    elif stage_type == 'x':
        return x
    else:
        return samonrun


def parse_p2(time) -> str:
    if time == 'now':
        return now
    elif time == 'next':
        return next
    else:
        return schedule
