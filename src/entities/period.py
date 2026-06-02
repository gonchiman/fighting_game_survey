from src.constants.months import MONTH_NUMS


class Period:
    def __init__(self, start_year: int, start_month: str, duration: int):
        self.start_year = start_year
        self.start_month = start_month
        self.duration = duration

    @property
    def start(self) -> str:
        return f"{self.start_month} {self.start_year}"

    @property
    def end(self) -> str:
        month_num_to_name = {v: k for k, v in MONTH_NUMS.items()}

        start_month_num = MONTH_NUMS[self.start_month]

        # 0始まりで計算する
        end_month_index = start_month_num - 1 + self.duration - 1

        end_year = self.start_year + end_month_index // 12
        end_month_num = end_month_index % 12 + 1
        end_month = month_num_to_name[end_month_num]

        return f"{end_month} {end_year}"