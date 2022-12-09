import json

from datetime import datetime

from typing import List

from ...splat3_stage_helper.utils.common import fetch

from ...splat3_stage_helper.pojo.bankara import Bankara
from ...splat3_stage_helper.pojo.regular import Regular
from ...splat3_stage_helper.pojo.fest_stage import FestStage
from ...splat3_stage_helper.pojo.salmon_run import SalmonRun

from ...splat3_stage_helper.utils.api_parse import *


def parse_time(iso_from) -> str:
    time = datetime.fromisoformat(iso_from)
    return str(time.month) + '.' + str(time.day) + ' ' + str(time.hour - 1) + ':00'


def bankara_to_string(start, end, rule, stage1, stage2) -> str:
    start = parse_time(start)
    end = parse_time(end)
    return Bankara(start, end, rule, stage1, stage2).to_string()


def regular_to_string(start, end, stage1, stage2) -> str:
    start = parse_time(start)
    end = parse_time(end)
    return Regular(start, end, stage1, stage2).to_string()


def fest_to_string(start, end, stage1, stage2, tricolor) -> str:
    start = parse_time(start)
    end = parse_time(end)
    return FestStage(start, end, stage1, stage2, tricolor).to_string()


def salmon_run_to_string(start, end, stage, weapon1, weapon2, weapon3, weapon4) -> str:
    start = parse_time(start)
    end = parse_time(end)
    return SalmonRun(start, end, stage, weapon1, weapon2, weapon3, weapon4).to_string()


async def list_stage(stage_type, time) -> List[str]:
    url = baseUrl + parse_p1(stage_type) + parse_p2(time)
    results = json.loads(await fetch(url))['results']
    data: List[str] = []
    n = len(results)

    if stage_type == 'regular':
        for (index, result) in enumerate(results):
            data.append(
                regular_to_string(result['start_time'], result['end_time'], result['stages'][0]['name'],
                                  result['stages'][1]['name']))
            if n > 1 and index < 2:
                data.append('\n\n')
            if index == 2:
                break

    elif stage_type == 'salmon_run':
        for (index, result) in enumerate(results):
            weapons = [weapon['name'] for weapon in result['weapons']]
            data.append(
                salmon_run_to_string(result['start_time'], result['end_time'], result['stage']['name'], weapons[0],
                                     weapons[1], weapons[2], weapons[3]))
            if n > 1 and index < 2:
                data.append('\n\n')
            if index == 2:
                break

    elif stage_type == 'fest':
        for (index, result) in enumerate(results):
            if not result['is_tricolor']:
                result['tricolor_stage'] = ''
            data.append(
                fest_to_string(result['start_time'], result['end_time'], result['stages'][0]['name'],
                               result['stages'][1]['name'],
                               result['tricolor_stage']))
            if n > 1 and index < 2:
                data.append('\n\n')
            if index == 2:
                break

    else:
        for (index, result) in enumerate(results):
            data.append(
                bankara_to_string(result['start_time'], result['end_time'], result['rule']['key'],
                                  result['stages'][0]['name'], result['stages'][1]['name']))
            if n > 1 and index < 2:
                data.append('\n\n')
            if index == 2:
                break

    return data
