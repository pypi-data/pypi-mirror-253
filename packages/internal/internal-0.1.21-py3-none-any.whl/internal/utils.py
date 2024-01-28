# -*- coding: utf-8 -*-
import hashlib
import json

import arrow

from .base_config import get_app_config, BaseConfig
from .const import STR_EMPTY, ARR_EXPORT_DATETIME_FMT


def is_today(time):
    if not time:
        return False
    time_zone = get_app_config().TIME_ZONE
    return arrow.now(time_zone).floor("day") == arrow.get(time).to(time_zone).floor("day")


def get_tz_day_boundary(date_time=None, dt_tz=None, out_tz="UTC"):
    """
    傳入date_time，取其在dt_tz時區的當天的floor與ceil，以out_tz時區回傳
    比對區間需使用gte/lte
    """
    dt_tz = dt_tz or get_app_config().TIME_ZONE
    date_time = arrow.get(date_time) if date_time else arrow.get()
    tz_time = date_time.to(dt_tz)
    return tz_time.floor("day").to(out_tz), tz_time.ceil("day").to(out_tz)


def timestamp_interval(start, end, interval_sec):
    while start < end:
        yield start
        start += interval_sec


def export_time_format(date, fmt=ARR_EXPORT_DATETIME_FMT):
    if not date:
        return STR_EMPTY

    return arrow.get(date).to(get_app_config().TIME_ZONE).format(fmt)


def update_dict_with_cast(curr_settings: BaseConfig, new_conf: dict):
    for key, value in new_conf.items():
        if hasattr(curr_settings, key):
            key_type = type(getattr(curr_settings, key))
            cast_func = key_type if key_type in (str, int) else json.loads
            setattr(curr_settings, key, cast_func(value))
