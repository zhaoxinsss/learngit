from usslib.egs.guard_template.lib.guard_fun import *

from testbase.testcase import TestCase
from testbase import datadrive

test_data = guard_name_list


@datadrive.DataDrive(test_data)
class Test(TestCase):
    """添加假日"""
    owner = "czs"
    timeout = 5
    priority = TestCase.EnumPriority.High
    status = TestCase.EnumStatus.Ready
    tags = "egs_holiday_1"

    def pre_test(self):
        # 初始化各类资源
        pass

    def run_test(self):
        self.start_step("添加假日")
        json_data = self.casedata
        print(json_data)
        status_code, content = add_guard_holiday(template_name=json_data)
        self.assert_("校验状态码", status_code == status_200)
        self.assert_("校验内容值为1", int(content) == 1)
        self.start_step("检查添加假日是否成功")

    def post_test(self):
        self.start_step("清理数据")
        delete_guard_holiday(PageSize=len(test_data))


if __name__ == '__main__':
    Test().debug_run()
