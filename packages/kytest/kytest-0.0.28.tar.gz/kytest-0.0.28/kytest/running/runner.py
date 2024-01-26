import inspect
import os
import re
import shutil
import subprocess

import pytest
from kytest.running.conf import App
from kytest.utils.log import logger
from kytest.utils.config import config
from multiprocessing import Process


def _get_case_list(path: str):
    # 获取所有用例文件的完整路径列表
    _total_file_list = []
    for root, dirs, files in os.walk(path):
        if 'pycache' in root:
            continue
        files_str = ''.join(files)
        if '.py' not in files_str:
            continue
        files = [item for item in files if item != '__init__.py']
        if files:
            for _file in files:
                _total_file_list.append(os.path.join(root, _file))

    # 获取path目录下的用例原始字符串
    cases_str = subprocess.run(['pytest', path, '--collect-only'], capture_output=True, text=True).stdout

    # 把所有的标签拿出来
    lines = cases_str.split("\n")
    result = []

    for line in lines:
        match = re.search(r"<(.*?)>", line)
        if match:
            item = match.group(1)
            result.append(item)

    # 解析成用例列表
    case_list = []
    current_package = ''
    current_module = ''
    current_class = ''
    for item in result:
        if 'Package' in item:
            current_package = item.split(" ")[1]
        if 'Module' in item:
            current_module = item.split(" ")[1]
        if 'Class' in item:
            current_class = item.split(" ")[1]
        if 'Function' in item:
            _function = item.split(" ")[1].split("[")[0]
            _file_path = f"{current_package}/{current_module}"
            for item in _total_file_list:
                if _file_path in item:
                    _file_path = item
                    break
            print(f"{_file_path}::{current_class}::{_function}")
            case_list.append(f"{_file_path}::{current_class}::{_function}")

    # 去重
    print("去重后：")
    case_list = sorted(list(set(case_list)))
    for case in case_list:
        print(case)

    return case_list


def _app_main(path, serial, package, udid, bundle_id, ocr_api, start):
    # 修改配置
    App.serial = serial
    App.package = package
    App.udid = udid
    App.bundle_id = bundle_id
    App.ocr_service = ocr_api
    App.auto_start = start

    # 执行用例
    # 由于是多设备并发执行，所以要对报告目录进行区分，后面增加合并的能力(有空调研一下pytest-xdist的报告合并实现方式)
    report_path = 'report'
    if serial:
        report_path = f'report-{serial}'
    if udid:
        report_path = f'report-{udid}'
    cmd_list = [
        path,
        '-sv',
        '--alluredir', report_path
    ]

    logger.info(cmd_list)
    pytest.main(cmd_list)


class TestMain(object):
    """
    Support for app、web、http
    """

    def __init__(
            self,
            path: str = None,
            api_host: str = None,
            headers: dict = None,
            package: str = None,
            serial: str = None,
            bundle_id: str = None,
            udid: str = None,
            ocr_api: str = None,
            start: bool = True,
            random: str = False,
            web_host: str = None,
            cookies: list = None,
            state: str = None,
            browser: str = None,
            headless: bool = False,
            maximized: bool = False,
            window_size: list = None,
            rerun: int = 0,
            xdist: bool = False
    ):
        """
        @param path: 用例路径
        @param api_host: 域名，用于接口测试和web测试
        @param headers: 请求头，用于接口测试和web测试
        @param package: 安卓包名，通过adb shell pm list packages | grep 'xxx'获取
        @param serial：安卓设备序列号，通过adb devices获取
        @param bundle_id：IOS应用包名，通过tidevice applist | grep 'xxx'获取
        @param udid：IOS设备uuid，通过tidevice list获取
        @param ocr_api: ocr识别服务api，用于安卓和ios测试
        @param start: 是否自动启动应用，用于安卓和ios测试
        @param web_host: 域名，用于接口测试和web测试
        @param cookies: 用于带上登录态
        @param state: 用户带上登录态，其实就是把cookies存到一个文件中
        @param browser: 浏览器类型，支持chrome、webkit、firefox
        @param headless: 是否开启无头模式，默认不开启
        @param maximized: 浏览器是否全屏
        @param window_size: 屏幕分辨率，[1920, 1080]
        @param rerun: 失败重试次数
        @param xdist: 是否并发执行，应该是多进程
        """
        # 公共参数保存
        common_data = {
            "base_url": api_host,
            "web_base_url": web_host,
            "headers": headers,
            "ocr_service": ocr_api
        }
        config.set_common_dict(common_data)
        # app参数保存
        # app_data = {
        #     "udid": udid,
        #     "bundle_id": bundle_id,
        #     "serial": serial,
        #     "package": package,
        #     "auto_start": start
        # }
        # config.set_app_dict(app_data)
        App.serial = serial
        App.package = package
        App.udid = udid
        App.bundle_id = bundle_id
        App.ocr_service = ocr_api
        App.auto_start = start
        # web参数保存
        web_data = {
            "cookies": cookies,
            "state_file": state,
            "browser_name": browser,
            "headless": headless,
            "maximized": maximized,
            "window_size": window_size
        }
        config.set_web_dict(web_data)

        if isinstance(serial, list) or isinstance(udid, list):
            # app多设备场景
            params = []
            if isinstance(serial, list) and not isinstance(udid, list):
                # 清空上次执行的目录
                for device in serial:
                    shutil.rmtree(f"report-{device}", ignore_errors=True)
                if not random:
                    for device in serial:
                        params.append((path, device, package, udid, bundle_id, ocr_api, start))
                else:
                    _path_list = [{item: []} for item in serial]
                    test_cases = _get_case_list(path)
                    print(test_cases)
                    # 把用例均分成设备数量的份数
                    n = len(serial)
                    lists = [[] for _ in range(n)]
                    for i, item in enumerate(test_cases):
                        index = i % n  # 计算元素应该分配给哪个列表
                        lists[index].append(item)

                    for i in range(n):
                        params.append((lists[i], serial[i], package, udid, bundle_id, ocr_api, start))

            elif isinstance(udid, list) and not isinstance(serial, list):
                for device in udid:
                    shutil.rmtree(f"report-{device}", ignore_errors=True)
                if not random:
                    if isinstance(udid, list):
                        for device in udid:
                            params.append((path, serial, package, device, bundle_id, ocr_api, start))
                else:
                    _path_list = [{item: []} for item in udid]
                    test_cases = _get_case_list(path)
                    print(test_cases)
                    # 把用例均分成设备数量的份数
                    n = len(udid)
                    lists = [[] for _ in range(n)]
                    for i, item in enumerate(test_cases):
                        index = i % n  # 计算元素应该分配给哪个列表
                        lists[index].append(item)

                    for i in range(n):
                        params.append((lists[i], serial, package, udid[i], bundle_id, ocr_api, start))
            elif isinstance(serial, list) and isinstance(udid, list):
                raise KeyError('不支持安卓和IOS同时有多个设备')

            # 多进程执
            if params:
                for param in params:
                    pr = Process(target=_app_main, args=param)
                    pr.start()
        else:
            # 执行用例
            cmd_list = [
                '-sv',
                '--reruns', str(rerun),
                '--alluredir', 'report', '--clean-alluredir'
            ]

            if path is None:
                stack_t = inspect.stack()
                ins = inspect.getframeinfo(stack_t[1][0])
                file_dir = os.path.dirname(os.path.abspath(ins.filename))
                file_path = ins.filename
                if "\\" in file_path:
                    this_file = file_path.split("\\")[-1]
                elif "/" in file_path:
                    this_file = file_path.split("/")[-1]
                else:
                    this_file = file_path
                path = os.path.join(file_dir, this_file)

            cmd_list.insert(0, path)

            if xdist:
                cmd_list.insert(1, '-n')
                cmd_list.insert(2, 'auto')

            logger.info(cmd_list)
            pytest.main(cmd_list)

        # 公共参数保存
        common_data = {
            "base_url": None,
            "web_base_url": None,
            "headers": None,
            "ocr_service": None
        }
        config.set_common_dict(common_data)
        # app参数保存
        # app_data = {
        #     "udid": None,
        #     "bundle_id": None,
        #     "serial": None,
        #     "package": None,
        #     "auto_start": False
        # }
        # config.set_app_dict(app_data)
        App.serial = None
        App.package = None
        App.udid = None
        App.bundle_id = None
        App.ocr_service = None
        App.auto_start = False
        # web参数保存
        web_data = {
            "cookies": None,
            "state_file": None,
            "browser_name": None,
            "headless": False,
            "maximized": False,
            "window_size": None
        }
        config.set_web_dict(web_data)


main = TestMain

if __name__ == '__main__':
    main()
