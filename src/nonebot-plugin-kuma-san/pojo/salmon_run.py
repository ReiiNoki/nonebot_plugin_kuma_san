from ...splat3_stage_helper.utils.translate import translate


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
