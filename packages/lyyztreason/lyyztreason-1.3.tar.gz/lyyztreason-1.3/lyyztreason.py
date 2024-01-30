import sys, os
import requests, json
from datetime import datetime
import pymysql
from sqlalchemy import create_engine, text
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import select, func
from sqlalchemy.orm import sessionmaker
import requests
import time
import pandas as pd
import lyytools
import lyycalendar
from lyystkcode import get_code_name_dict
import sqlite3

stkcode_name_dict = get_code_name_dict()
print(f"stkcode_name字典获取成功，长度为{len(stkcode_name_dict)}")
# pyinstaller -D -n ztreason_jiucai --distpath  "D:\Soft\_lyysoft" D:\UserData\Documents\PythonCode\archive\ztreason_jiucai.py --noconfirm

sqlite_db = "sqlite:///D:/UserData/resource/data/ztreason.db"
engine_sqlite = create_engine(sqlite_db)
conn_sqlite = engine_sqlite.connect()
INFO_DICT = {}


def get_reason_kpl(stkcode, debug=False):
    def find_closest_item_by_date(json_text):
        # 解析JSON文本
        data = json.loads(json_text)
        current_time = datetime.now()

        # 初始化最小差值和对应的item
        min_diff = float("inf")
        closest_item = None

        # 遍历List中的每个item
        for item in data["List"]:
            # 获取item中的日期
            item_date_str = item["Date"]

            # 转换为datetime对象
            item_date = datetime.strptime(item_date_str, "%Y-%m-%d")

            # 计算日期差值
            diff = (current_time - item_date).days

            # 更新最小差值和对应的item
            if abs(diff) < min_diff:
                min_diff = abs(diff)
                closest_item = item

        #         {'ZSCode': ['801267', '801211'], 'Reason': '乳业+新疆；新疆最大的原奶供应商；A股唯一原料乳输出标的；乳制品加工占营收73%,畜牧业占营收23%；2018年9月当月资产生鲜乳2918吨；拥有新疆目前仅有的两张婴幼儿配方奶粉生产销售许可证。', 'Date': '2023-09-01', 'SCDW': '', 'SCLT': '日内龙一', 'GNSM': '新疆最大的原奶供应商；A股唯一原料乳输出标的；乳
        # 制品加工占营收73%,畜牧业占营收23%；2018年9月当月资产生鲜乳2918吨；拥有新疆目前仅有的两张婴幼儿配方奶粉生产销售许可证。', 'Type': '0', 'PZSCode': '0'}
        # ['801267', '801211']
        # 返回最接近当前时间的item
        return closest_item["ZSCode"], closest_item["Date"], closest_item["Reason"].split("；", 1)[0], closest_item["GNSM"]

    url = f"https://apphis.longhuvip.com/w1/api/index.php?a=GetDayZhangTing&st=100&apiv=w31&c=HisLimitResumption&StockID={stkcode}&PhoneOSNew=1&UserID=0&DeviceID=00000000-296c-20ad-0000-00003eb74e84&VerSion=5.7.0.12&Token=0&Index=0&"

    response = requests.get(url)
    result_bytes = response.content

    # 为了避免DeprecationWarning: invalid escape sequence '\/'
    result_string = result_bytes.decode("utf-8").replace(r"\/", "/")
    decoded_text = bytes(result_string, "utf-8").decode(r"unicode_escape")
    # 去掉换行符
    decoded_text = decoded_text.replace("\r\n", "").replace("\n", "")
    # 变成json好取值。
    # print(repr(decoded_text))
    data = json.loads(decoded_text)
    zt_reason = find_closest_item_by_date(decoded_text)

    # 解析JSON文本
    # data = json.loads(decoded_text)
    # for item in zt_reason:
    #     print(item)
    # selected_columns = ['code', 'name', 'date', 'plate_name', 'plate_reason', 'reason']  # 选择要提取的列
    dictx = {}
    dictx["code"] = stkcode
    dictx["name"] = " ".join(zt_reason[0])
    dictx["date"] = zt_reason[1]
    dictx["plate_name"] = zt_reason[2]
    dictx["reason"] = zt_reason[3]
    return dictx


def MySql直接查询涨停原因(con, 股票代码):
    query = f"select * from stock_zt_reason where code = '{股票代码.zfill(6)}' order by date desc limit 1"
    print("query=", query)
    df = pd.read_sql(text(query), con)
    if len(df) > 0:
        print("in ztreason", df)
        return df
        # return df.iloc[0]["reason"]
    return ""


@lyytools.get_time
def get_ztreason_from_xgb(conn, code, debug=False):
    # INFO_DICT['code'] = code2name(code)
    text_label = "information"
    title = code
    df = MySql直接查询涨停原因(conn, code)
    if len(df) <= 0:
        return None
    selected_columns = ["code", "name", "date", "plate_name", "plate_reason", "reason"]  # 选择要提取的列
    # 使用 loc 通过列名称选择特定列
    selected_df = df.loc[:, selected_columns]

    # 将选定列转换为字典
    row_dict = selected_df.to_dict(orient="records")
    if len(row_dict) > 0:
        return row_dict[0]
    else:
        return None
    if debug:
        print(row_dict)


@lyytools.get_time
def get_ztreason_from_db_jiucai(conn, code, debug=False):
    print("enter get_ztreason_from_db_jiucai")
    # if len(INFO_DICT) < 1:
    #     print("info is empty")

    try:
        sqlquery = f"SELECT * FROM stock_jiucai WHERE code = {code} order by date desc limit 1"
        df = get_data_from_mysql(sqlquery)

        dict_rows = df.to_dict("records")
        if len(dict_rows) > 0:
            return dict_rows[0]
        else:
            return dict_rows

    except Exception as e:
        print("Inget_ztreason_from_db_jiucai,error = ", e)
    return None


def html2mysql_today(json_str, debug=False):
    total_effect = 0
    # if debug: print(json_str)
    data = json.loads(json_str)
    surge_reason = data["data"]["surge_reason"]
    con = pymysql.connect(host="rm-7xvcw05tn97onu88s7o.mysql.rds.aliyuncs.com", user="cy", passwd="Yc124164", port=3306, db="fpdb", charset="utf8")
    cur = con.cursor()

    for item in range(len(surge_reason)):
        print(" for item in range(len( surge_reason)) item=", item)
        stk_code_num = surge_reason[list(surge_reason)[item]]["symbol"].replace(".", "").replace("S", "").replace("Z", "").replace("H", "")
        stk_code_num = int(stk_code_num)

        stock_reason = surge_reason[list(surge_reason)[item]]["stock_reason"]
        date_int = datetime.now().strftime("%Y%m%d")
        related_plates = surge_reason[list(surge_reason)[item]]["related_plates"]
        for plate in related_plates:
            if "plate_id" in plate:
                plate_id = plate["plate_id"]
            if "plate_name" in plate:
                plate_name = plate["plate_name"]
            if "plate_reason" in plate:
                plate_reason = plate["plate_reason"]
            else:
                plate_reason = ""

        print(f" 取出的数据为：{date_int}：'{stk_code_num}'：{plate_name}: {stock_reason}")

        sql = f"SELECT name FROM stock_all_codes WHERE code='{stk_code_num}'"
        print("查询code,seach=", sql)

        cur.execute(sql)
        result = cur.fetchone()
        if result:
            stk_name = result[0]
            print("数据库中查到的name=", stk_name)
        else:
            stk_name = ""
            print("数据库中查不到名字，请检查是代码错了，还是没更新。：stk_name=", stk_name)

        # 查询数据库表中是否已经存在相同数据
        sql = f"SELECT count(*) FROM stock_zt_reason WHERE code='{stk_code_num}'"
        print("seach=", sql)
        cur.execute(sql)
        result = cur.fetchone()
        print(result, "dfsafdsafdsa")
        if result:
            print("有相同值，尝试删除")
            del_sql = f"delete from stock_zt_reason where code='{stk_code_num}'"
            cur.execute(del_sql)
            print(cur.rowcount, "record(s) removed.")
        else:
            print("无结果")

        # 无论是否相同数据，都执行插入操作
        sql_insert = f"insert into stock_zt_reason(date, code, name, plate_id,plate_name,plate_reason,reason) \
            values({date_int}, '{stk_code_num}', '{stk_name}','{plate_id}','{plate_name}','{plate_reason}', '{stock_reason}')"
        print("insert=", sql_insert)
        cur.execute(sql_insert)
        print(cur.rowcount, "record inserted.")
        total_effect = total_effect + cur.rowcount
        con.commit()
        # import time;time.sleep(3333)
    return total_effect


def get_reason_from_xgb_reason_list(r_list, code_my=None):
    print(r_list, "lenoflsi=", len(r_list), type(r_list))
    code_lis, name_lis, price_lis, expound_lis, share_range_lis, time_lis = [], [], [], [], [], []

    for i in r_list:
        lis = i.get("list")
        for j in lis:
            code = j["code"]
            if code_my in code:
                # print(j)
                name = j["name"]
                price = float(j["article"]["action_info"]["price"]) / 100
                expound = j["article"]["action_info"]["expound"]
                shares_range = float(j["article"]["action_info"]["shares_range"]) / 100
                time_ = j["article"]["action_info"]["time"]
                code_lis.append(code)
                name_lis.append(name)
                price_lis.append(price)
                expound_lis.append(expound)
                share_range_lis.append(shares_range)
                time_lis.append(time_)
    df = pd.DataFrame({"代码": code_lis, "名称": name_lis, "价格": price_lis, "解析": expound_lis, "跌涨幅": share_range_lis, "时间": time_lis})
    # return j
    df.to_csv("200_yidong.csv", index=False, encoding="utf_8_sig")
    return df


def insert_dict_to_table(conn, table_name, data_dict):
    print(data_dict.keys(), "keys()")
    # dict_keys(['code', 'name', 'date', 'plate_name', 'reason']) keys()
    rowcount = 0
    try:
        # 构建插入语句
        keys = ", ".join(data_dict.keys())
        values = ", ".join([":" + key for key in data_dict.keys()])
        insert_statement = text(f"INSERT INTO {table_name} ({keys}) VALUES ({values})")

        columns = ", ".join(data_dict.keys())  # 获取要检查的列名
        query = f"SELECT COUNT(*) FROM {table_name} WHERE code={data_dict['code']} and date={data_dict['date']}"
        result = conn.execute(text(query))  # 使用execute方法执行查询
        rowcount = result.fetchone()[0]
        print("query", query)

        if rowcount > 0:
            print("Duplicate values detected. Skipping insertion.")
            return 0  # 如果存在重复值，则返回已插入的行数，以便稍后进行相应的处理
        else:
            print("in insert_dict_to_table, 重复不存在的，执行插入操作")
            result = conn.execute(insert_statement, data_dict)

            conn.commit()
            return result.rowcount
    except sqlite3.IntegrityError as e:
        print("插入失败，发生了唯一约束错误:", e)

    except Exception as e:
        print(e)
        return 0


def get_last_date_in_db(engine):
    # 创建连接
    conn = engine.connect()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    Stock_Jiucai = Table("stock_jiucai", metadata, autoload_with=engine)

    # 执行SQL查询语句
    result = conn.execute(func.max(Stock_Jiucai.c.date))

    # 获取查询结果
    last_date = result.scalar()
    # 关闭连接
    conn.close()
    return last_date


def data2sqlite():
    engine = create_engine("sqlite:///D:/UserData/resource/data/zt_reason.db")
    conn = engine.connect()
    query = "select * from reason"
    df = pd.read_sql(query, conn)
    print(df)

    # new_user = {"name": "John", "age": 25}
    # session.add(new_user)
    # session.commit()
    # # 更新数据
    # user = session.query("SELECT * FROM users WHERE id=1").first()
    # user["name"] = "Jane"
    # session.commit()
    # # 删除数据
    # session.delete(new_user)
    session.commit()
    # 关闭会话
    session.close()


def get_reason_today_xgb(debug=False):
    """
    {"code":20000,"message":"OK","data":{"surge_reason":{"000037.SZ":{"symbol":"000037.SZ","stock_reason":"1、公司主营生产经营供电供热、从事发电厂（站）的相关技术咨询和技术服务，公司拥有3家全资或
    控股燃机发电厂，下属南山热电厂已进行虚拟电厂备案 ；\n2、公司及控股子电有限公司5%股份，目前江西核电有限公司核电站尚未获得国家核准","related_plates":[{"plate_id":16858654,"p
    late_name":"深圳本地股"}]},"000637.SZ":{"symbol":"0
    """
    url = "https://flash-api.xuangubao.cn/api/surge_stock/reason/today"
    headers = {
        "Host": "flash-api.xuangubao.cn",
        "Connection": "keep-alive",
        "Access-Control-Request-Method": "GET",
        "Access-Control-Request-Headers": "x-ivanka-token",
        "Origin": "<https://xuangubao.cn>",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Dest": "empty",
        "Referer": "<https://xuangubao.cn/zhutiku>",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Accept": "*/*",
    }

    response = requests.get(url, headers=headers)
    if debug:
        print("url=", url, ",headers=", headers)
    if debug:
        print("today_reason_result::", response.text)
    data_json = json.loads(response.text)
    if "data" not in data_json.keys():
        raise Exception("in get_reason_today_xgb, `data` not in data_json.keys()")
    reason = data_json["data"]["surge_reason"]
    print("return reason=", reason, type(reason))
    return reason


def get_last_date_in_sqlite(table_name, engine=None):
    if engine is None:
        engine = create_engine("sqlite:///D:/UserData/resource/data/ztreason.db")
    # 创建连接
    conn = engine.connect()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    Stock_Jiucai = Table(table_name, metadata, autoload_with=engine)

    # 执行SQL查询语句
    result = conn.execute(func.max(Stock_Jiucai.c.date))

    # 获取查询结果
    last_date = result.scalar()
    # 关闭连接
    conn.close()
    return last_date


def 韭菜公社(date_str, debug=False):
    # 在韭菜公社查询某天所有异动和涨停股票
    url = "https://app.jiuyangongshe.com/jystock-app/api/v1/action/field"
    headers = {"cookie": "Hm_lvt_58aa18061df7855800f2a1b32d6da7f4=1696917396; UM_distinctid=18b182899a927d-0fe36fe5c5cc2-26031e51-1fa400-18b182899aa115e; Hm_lpvt_58aa18061df7855800f2a1b32d6da7f4=1696922120", "origin": "https://www.jiuyangongshe.com", "Platform": "3", "Referer": "https://www.jiuyangongshe.com/", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36", "Token": "fd611dcef77bc69b8b83d2c9a17f52c2", "Sec-Ch-Ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"', "Host": "app.jiuyangongshe.com", "Timestamp": f"{int(time.time()*1000)}"}
    data = {"date": date_str, "pc": 1}
    r = requests.post(url, headers=headers, json=data).json()

    r_data = r["data"]
    # print("rdata=", r_data)
    return r_data[1:]


def 韭菜公社查询单个涨停原因(code_my, date_str, return_format="dict", debug=False):
    r_data = 韭菜公社(date_str)
    if debug:
        print(r_data)
    code_lis, name_lis, price_lis, expound_lis, share_range_lis, time_lis = [], [], [], [], [], []

    for i in r_data:
        lis = i.get("list")
        for j in lis:
            code = j["code"]
            if code_my in code:
                # print(j)
                name = j["name"]
                price = float(j["article"]["action_info"]["price"]) / 100
                expound = j["article"]["action_info"]["expound"]
                shares_range = float(j["article"]["action_info"]["shares_range"]) / 100
                time_ = j["article"]["action_info"]["time"]
                code_lis.append(code)
                name_lis.append(name)
                price_lis.append(price)
                expound_lis.append(expound)
                share_range_lis.append(shares_range)
                time_lis.append(time_)
    df = pd.DataFrame({"代码": code_lis, "名称": name_lis, "价格": price_lis, "解析": expound_lis, "跌涨幅": share_range_lis, "时间": time_lis})
    if return_format == "df":
        return df
    else:
        return j
    # df.to_csv("200_yidong.csv",index=False,encoding='utf_8_sig')


def 韭菜公社补数据(days):
    total_effect_rows = 0
    for dayn in reversed(range(days)):
        date = lyycalendar.lyytc.tc_before_today(dayn, return_str=True)
        reasons_list = 韭菜公社(date, debug=True)

        print(f"{date} resason_list=", reasons_list, "type=", type(reasons_list))
        for lst in reasons_list:
            data = lst["list"]
            for item in data:
                print("item=", item)
                new_dict = {}
                new_dict["code"] = item["code"].replace("sh", "").replace("sz", "").replace("bj", "")
                new_dict["name"] = item["name"]
                new_dict["date"] = item["article"]["create_time"][:10].replace("-", "")
                plate_reason_and_reson = item["article"]["action_info"]["expound"].split("\n", 1)
                if len(plate_reason_and_reson) == 2:
                    new_dict["plate_name"], new_dict["reason"] = plate_reason_and_reson
                else:
                    new_dict["plate_name"] = ""
                    new_dict["reason"] = plate_reason_and_reson[0]

                print(new_dict)
                total_effect_rows += insert_dict_to_table(conn_sqlite, "jiucai", new_dict)
        time.sleep(5)
    print(f"Congratulations! Total added {total_effect_rows} row( including existing item)")


def update_jiucai_to_date():
    last_date = get_last_date_in_sqlite("jiucai")
    print("last_date=", last_date)
    today_int = int(datetime.today().strftime("%Y%m%d"))
    相差天数 = lyycalendar.lyytc.计算相隔天数_byIndex(last_date, today_int)
    # 相差天数 = 相差天数 + 1 if 相差天数 == 0 else 相差天数
    print("相差天数=", 相差天数)
    韭菜公社补数据(相差天数)

    print("ztreason_jiucai result=", 相差天数)


def format_xgb_today(result, return_format="df", debug=False):
    # 返回值为dataframe或者dict
    # 把respose.txt加载成json后，最后获取的值为：
    # {'000037.SZ': {'symbol': '000037.SZ', 'stock_reason': '1、公司主营2、...., 'related_plates': [{'plate_id': 16858654, 'plate_name': '深圳本地股'}
    resutl_list = []
    for value in result.values():
        sub_c = {}
        for sub_key, sub_value in value.items():
            if isinstance(sub_value, list):
                if debug:
                    print(sub_value, " is " + "列表,遍历它")
                for i in range(len(sub_value)):
                    if isinstance(sub_value[i], dict):
                        if debug:
                            print("子子元素是字典，拆解它:sub_value[i]=", sub_value[i])
                        for sskey, ssvalue in sub_value[i].items():
                            sub_c[sskey] = ssvalue
                    else:
                        if debug:
                            print("子子元素不是字典？", type(i))
            else:
                if debug:
                    print("子元素不是列表，直接赋值,sub_key] =", sub_key, sub_value)
                # 跟目标标准字段不一样的，symbol改code，并把市场后缀去掉。stock_reason改reason，
                if sub_key == "symbol":
                    sub_key = sub_key.replace("symbol", "code")
                    sub_value = sub_value.replace(".SS", "").replace(".SZ", "").replace(".BJ", "")
                    sub_c["name"] = stkcode_name_dict.get(sub_value)

                else:
                    sub_key = sub_key.replace("stock_", "")
                sub_c[sub_key] = sub_value
                sub_c["date"] = datetime.today().strftime("%Y%m%d")
        resutl_list.append(sub_c)

    if return_format == "df":
        df = pd.DataFrame.from_records(resutl_list)
        df["date"] = datetime.today().strftime("%Y%m%d")
        df.rename(columns={"symbol": "code", "zt_reason": "reason"}, inplace=True)
        df["code"] = df["code"].str.replace(".SS", "").str.replace(".SZ", "").str.replace(".BJ", "")
        return df
    else:
        return resutl_list


def update_xgb_to_date():
    result = get_reason_today_xgb(debug=False)

    result_list = format_xgb_today(result, return_format="list")
    print("-=================", "\n", type(result_list), result_list)
    rows_effect = 0
    for sub_dict in result_list:
        print("sub_dict=", sub_dict)
        rows_effect += insert_dict_to_table(conn_sqlite, "xgb", sub_dict)

    print(f"选股宝更新成功，插入行数为：{rows_effect}")


if __name__ == "__main__":
    update_xgb_to_date()

    sys.exit()
    # get_reason_from_xgb_reason_list(result)

    update_jiucai_to_date()
    update_xgb_to_date()

    # data2sqlite()

    韭菜公社("002584 ")
    get_reason_kpl("300280")

    import lyycalendar

    db_string = "mysql+pymysql://cy:Yc124164@rm-7xvcw05tn97onu88s7o.mysql.rds.aliyuncs.com:3306/fpdb?charset=utf8"

    if not "engine" in locals():
        engine = create_engine(db_string)
        conn = engine.connect()
    #     reasons_list = 韭菜公社("2023-11-06")

    # 创建数据库引擎
    engine = create_engine(db_string)

    # 连接数据库

    conn.close()
    # print(韭菜公社("300280"))
    # 使用已有的engine和conn

    html_today = today_reason()
    print(html_today)
    effected = html2mysql_today(html_today)


"""
def 直接查询涨停原因(con, 股票代码):
    query = f"select * from stock_zt_reason where code = '{股票代码.zfill(6)}' order by date desc limit 1"
    print("query=", query)
    df = f1999cfg.get_data_from_mysql(query)
    if len(df) > 0:
        print("in ztreason", df)
        return df
        # return df.iloc[0]["reason"]
    return ""
"""
