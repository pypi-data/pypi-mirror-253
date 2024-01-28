from itertools import product
from enum import StrEnum
import re


class Timebase:
    def __init__(self, rate, drop_frame=None):
        self.fps = int(round(rate))
        self.drop_frame = drop_frame if drop_frame is not None else self.fps == float(rate)
        self.input = rate

    def __repr__(self):
        return 'Timebase({0}{1})'.format(self.fps, 'DF' if self.drop_frame else '')

    def __int__(self):
        return self.fps


class TCMode(StrEnum):
    TC = "time_code"
    TS = "time_stamp"


class TimeCode:
    __TEMPLATES = {TCMode.TS: '{0[0]:0>2}:{0[1]:0>2}:{0[2]:0>2}{sep}{0[3]:0>3}',
                   TCMode.TC: '{0[0]:0>2}:{0[1]:0>2}:{0[2]:0>2}{sep}{0[3]:0>2}'}

    def __init__(self, tc_parts: list[int] = None, drop_frame=False, mode=TCMode.TC, custom_sep=None):
        self.__parts = [0, 0, 0, 0]
        self.drop_frame = drop_frame
        self.mode = mode
        self.custom_sep = custom_sep

        if tc_parts is not None:
            for i, v in product(range(4), tc_parts):
                assert isinstance(v, (int | float))
                __max = 999 if i == 3 else 99
                assert 0 <= v <= __max
                self.__parts[i] = int(v)

    @property
    def sep(self):
        if self.custom_sep is not None:
            return self.custom_sep
        if self.mode is TCMode.TS:
            return ','
        return ';' if self.drop_frame else ':'

    @property
    def segments(self):
        return tuple(self.__parts)

    def __str__(self):
        return TimeCode.__TEMPLATES[self.mode].format(self.__parts, self.sep)

    def __repr__(self):
        return 'TimeCode{0}{1}'.format(self.__parts, 'DF' if self.drop_frame else '')


TC_PATTERN = re.compile(r'(\d\d):(\d\d):(\d\d)([:;,\.])(\d\d\d?)')


def is_tc(string: str):
    return TC_PATTERN.fullmatch(string) is not None


_EMPTY_TC_INFO_ = {'parts': (0, 0, 0, 0), 'drop_frame': False, 'mode': TCMode.TS}


def parse_tc_parts(tc: str):
    match = TC_PATTERN.fullmatch(tc.strip())
    if match is None:
        return _EMPTY_TC_INFO_
    sep = match.group(4)
    parts = (int(x) for x in match.group(1, 2, 3, 5))
    return {
        'parts': parts,
        'drop_frame': sep == ';',
        'mode': TCMode.TC if sep in ':;' else TCMode.TS
    }


def make_tc_parts(millisecond: int, mode=TCMode.TS, timebase: Timebase = None):
    assert millisecond >= 0
    seconds = millisecond // 1000
    ss = seconds % 60
    minutes = seconds // 60
    mm = minutes % 60
    hours = minutes // 60
    hh = hours % 24
    fff = millisecond % 1000
    if mode is TCMode.TC:
        if timebase is None:
            timebase = Timebase(24, False)
        rate = timebase.fps
        fff = int((millisecond / 1000) * rate) % rate
    return {'parts': (hh, mm, ss, fff), 'drop_frame': timebase.drop_frame, 'mode': mode}
