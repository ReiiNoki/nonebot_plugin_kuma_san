from .utils.translate import translate
from .utils.constants import get_rule


class Bankara(object):
    def __init__(self, start, end, rule, stage1, stage2) -> None:
        self.start = start
        self.end = end
        self.rule = get_rule(rule)
        self.stage1 = translate(stage1)
        self.stage2 = translate(stage2)

    def to_string(self) -> str:
        return self.start + ' - ' + self.end + ' ' + self.rule + '\n' + self.stage1 + ' ' + self.stage2


class FestStage(object):
    def __init__(self, start, end, stage1, stage2, tricolor) -> None:
        self.start = start
        self.end = end
        self.stage1 = translate(stage1)
        self.stage2 = translate(stage2)
        self.tricolor = translate(tricolor)

    def to_string(self) -> str:
        return self.start + ' - ' + self.end + '\n' + self.stage1 + ' ' + self.stage2


class Regular(object):
    def __init__(self, start, end, stage1, stage2) -> None:
        self.start = start
        self.end = end
        self.stage1 = translate(stage1)
        self.stage2 = translate(stage2)

    def to_string(self) -> str:
        return self.start + ' - ' + self.end + '\n' + self.stage1 + ' ' + self.stage2


class SalmonRun(object):
    def __init__(self, start, end, stage, weapon1, weapon2, weapon3, weapon4) -> None:
        self.start = start
        self.end = end
        self.stage = translate(stage)
        self.weapon1 = translate(weapon1)
        self.weapon2 = translate(weapon2)
        self.weapon3 = translate(weapon3)
        self.weapon4 = translate(weapon4)

    def to_string(self) -> str:
        return self.start + ' - ' + self.end + '\n' + self.stage + '\n' + self.weapon1 + ' ' + self.weapon2 + '\n' + self.weapon3 + ' ' + self.weapon4
