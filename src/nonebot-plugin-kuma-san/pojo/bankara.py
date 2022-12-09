from ...splat3_stage_helper.utils.translate import translate
from ...splat3_stage_helper.utils.constants import get_rule


class Bankara(object):
    def __init__(self, start, end, rule, stage1, stage2) -> None:
        self.start = start
        self.end = end
        self.rule = get_rule(rule)
        self.stage1 = translate(stage1)
        self.stage2 = translate(stage2)

    def to_string(self) -> str:
        return self.start + ' - ' + self.end + ' ' + self.rule + '\n' + self.stage1 + ' ' + self.stage2
