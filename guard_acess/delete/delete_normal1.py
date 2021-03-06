from usslib.egs.guard_template.lib.guard_fun import *

from testbase.testcase import TestCase
from testbase import datadrive

test_data = {"holiday_data": holiday}


@datadrive.DataDrive(test_data)
class Test(TestCase):
    """删除假日"""
    owner = "czs"
    timeout = 5
    priority = TestCase.EnumPriority.High
    status = TestCase.EnumStatus.Ready
    tags = "egs_holiday_2"

    def pre_test(self):
        # 初始化各类资源
        pre_guard_template(is_online=False)
        add_guard_holiday(self.casedata)
        pass

    def run_test(self):
        self.start_step("删除假日")
        status_code, content, is_true = delete_guard_holiday(holiday_group_name=self.casedata)
        self.assert_("校验状态码", status_code == status_200)
        self.assert_("校验内容值为1", int(content) == 1)
        self.assert_("检查是否已被删除", is_true)
        self.start_step("检查删除假日是否成功")

    def post_test(self):
        pass


if __name__ == '__main__':
    Test().debug_run()
