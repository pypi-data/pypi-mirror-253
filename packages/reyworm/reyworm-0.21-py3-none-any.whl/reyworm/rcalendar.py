# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2024-01-10 21:57:08
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Calendar methods.
"""


from typing import List, Dict, Optional
from json import loads as json_loads
from reytool.rcomm import request
from reytool.rtime import now


__all__ = (
    "get_cn_calendar_month",
)


def get_cn_calendar_month(
    year: Optional[int] = None,
    month: Optional[int] = None
) -> List[Dict]:
    """
    Get chinese calendar month table.

    Parameters
    ----------
    year : Given year.
        - `None` : Now year.

    month : Given month.
        - `None` : Now month.

    Returns
    -------
    Chinese calendar month table.
    """

    # Get parameter.
    now_date = now("date")
    if year is None:
        year = now_date.year
    if month is None:
        month = now_date.month
    url = "https://www.rili.com.cn/rili/json/pc_wnl/%s/%02d.js" % (year, month)
    params = {"_": now("timestamp")}

    # Request.
    response = request(url, params)

    # Extract.
    text = response.text.split("{", 1)[1]
    text = text.rsplit("}", 1)[0]
    text = "{%s}" % text
    data = json_loads(text)
    table = data["data"]

    return table