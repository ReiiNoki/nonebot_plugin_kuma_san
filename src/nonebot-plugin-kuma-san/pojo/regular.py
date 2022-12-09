from ...splat3_stage_helper.utils.translate import translate


class Regular(object):
    def __init__(self, start, end, stage1, stage2) -> None:
        self.start = start
        self.end = end
        self.stage1 = translate(stage1)
        self.stage2 = translate(stage2)

    def to_string(self) -> str:
        return self.start + ' - ' + self.end + '\n' + self.stage1 + ' ' + self.stage2
