import sys
import os

import mns_common.api.kpl.selection.kpl_selection_plate_api as selection_plate_api
from mns_common.db.MongodbUtil import MongodbUtil
from loguru import logger
import mns_common.api.kpl.constant.kpl_constant as kpl_constant
import mns_common.utils.data_frame_util as data_frame_util
import mns_scheduler.kpl.selection.index.sync_best_choose_index as sync_best_choose_first_index
import mns_scheduler.kpl.selection.symbol.sync_best_choose_symbol as sync_best_choose_symbol
import threading

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 17
project_path = file_path[0:end]
sys.path.append(project_path)

mongodb_util = MongodbUtil('27017')

# 分页大小
MAX_PAGE_NUMBER = 10


# 同步开票啦精选概念股票组成
def sync_best_choose_symbol_detail(first_index_df, page_number):
    for stock_one in first_index_df.itertuples():
        try:
            # 保存一级精选指数股票组成
            sync_best_choose_symbol.save_one_plate_detail_data(stock_one.plate_code,
                                                               stock_one.plate_name,
                                                               kpl_constant.FIRST_INDEX,
                                                               stock_one.plate_code,
                                                               stock_one.plate_name)

            kpl_best_choose_sub_index_detail = selection_plate_api.best_choose_sub_index(stock_one.plate_code)

            if data_frame_util.is_not_empty(kpl_best_choose_sub_index_detail):
                for sub_one in kpl_best_choose_sub_index_detail.itertuples():
                    try:
                        sync_best_choose_symbol.save_one_plate_detail_data(sub_one.plate_code,
                                                                           sub_one.plate_name,
                                                                           kpl_constant.SUB_INDEX,
                                                                           stock_one.plate_code,
                                                                           stock_one.plate_name)
                    except BaseException as e:
                        logger.error("同步开盘啦精选板块二级指数详情异常:{},{}", sub_one.plate_code, e)

        except BaseException as e:
            logger.error("同步开盘啦精选板块二级指数异常:{},{}", stock_one.plate_code, e)


def multi_thread_sync_kpl_best_choose_detail():
    first_index_df = sync_best_choose_first_index.choose_field_choose_first_index()
    count = first_index_df.shape[0]
    page_number = round(count / MAX_PAGE_NUMBER, 0) + 1
    page_number = int(page_number)
    threads = []
    # 创建多个线程来获取数据
    for page in range(page_number):  # 0到100页
        end_count = (page + 1) * MAX_PAGE_NUMBER
        begin_count = page * MAX_PAGE_NUMBER
        page_df = first_index_df.iloc[begin_count:end_count]
        thread = threading.Thread(target=sync_best_choose_symbol_detail, args=(page_df, page_number))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()


# 同步所有精选指数信息
def sync_all_plate_info():
    # 同步第一和第二级别精选指数
    # 更新一级和二级之间的关联关系
    # 找出新增精选指数
    sync_best_choose_first_index.sync_best_choose_index()
    logger.info("同步开票啦精选概念指数完成")
    # 同步精选概念股票组成
    multi_thread_sync_kpl_best_choose_detail()
    logger.info("同步开票啦精选概念股票组成完成")


if __name__ == '__main__':
    # 同步第一和第二级别精选指数
    sync_all_plate_info()
