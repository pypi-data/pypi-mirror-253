#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Date: 2024/01/15 20:00
Desc: 基金基本信息
"""
import pandas as pd
import requests
import json


def fund_basic(fields: str = "fund_code", **kwargs) -> pd.DataFrame:
    """
    基金数据-基金基本信息
    https://fund.eastmoney.com/manager/default.html
    :return: 基金经理大全
    :rtype: pandas.DataFrame
    """

    url = "http://192.168.0.77:8010/fund/fund_basic?fields={}".format(fields)
    response = requests.post(url, json=kwargs)
    # 解析JSON数据
    data = json.loads(response.text)["data"]
    # 将JSON数据转换为DataFrame
    df = pd.DataFrame(data)
    # print(df)
    return df


if __name__ == "__main__":
    df = fund_basic(fields="fund_code,fund_short_name", **{
  "fund_code": "",
  "td_mkt": "E",
  "fund_listed_type": "正常上市"
})
    # print(df)