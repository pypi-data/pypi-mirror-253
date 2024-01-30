from typing import Tuple, Callable, List
from datetime import datetime
from time import sleep
import logging

import nanovicky.helper.cron as cronhelper
from nanovicky.components.base_component import BaseComponent


class SchedulerComponent(BaseComponent):
    def __init__(
        self, name: str, tasks: List[Tuple[str, Callable]], execution_mode: int = 1
    ):
        super().__init__(execution_mode=execution_mode, name=name)
        self._tasks: List[Tuple[str, Callable]] = tasks

    def initiate(self):
        for index, task in enumerate(self._tasks):
            cron, _ = task
            test_cron = cron.split(" ")
            if len(test_cron) != 5:
                logging.warning(
                    self.log_message(f"{cron} is not valid cron, will be removed")
                )
                self._tasks.pop(index)

        current_time = datetime.now()
        second = current_time.second

        if second != 0:
            sleep(60 - second)

    def parse_cron_unit(self, time: int, unit: str) -> List[List[Callable]]:
        if unit == "*":
            return cronhelper.every_unit()

        # Case */value
        elif unit[0:2] == "*/":
            # print(int("".join(unit[2:])))
            return cronhelper.each_unit(time, int("".join(unit[2:])))

        # Case value-value
        elif len(unit.split("-")) == 2:
            min, max = unit.split("-")
            return cronhelper.between_units(int(min), int(max), time)

        elif unit.isdigit():
            return cronhelper.at_unit(time, int(unit))

        else:
            print("Error in cron scheduler : cron unit not managed")

    def do(self):
        current_time = datetime.now()

        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour
        day = current_time.day
        month = current_time.month
        weekday = current_time.isoweekday()

        # logging.info(f"Minute = {minute}, Hour = {hour}, Day = {day}, Month = {month}, Weekday = {weekday}")

        for cron_index, cron in enumerate(self._tasks):
            job_allowed = True
            units = cron[0].split(" ")
            for index, time in enumerate([minute, hour, day, month, weekday]):
                is_valid = self.parse_cron_unit(time, units[index])
                if not is_valid:
                    job_allowed = False
                    break
            if job_allowed:
                logging.info(self.log_message(f"Running cron number {cron_index + 1}"))
                cron[1]()

        sleep(60 - second)
