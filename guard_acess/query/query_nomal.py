from usslib.egs.guard_template.lib.guard_fun import *

from testbase.testcase import TestCase
from testbase import datadrive

test_data = {"template_data": template}


@datadrive.DataDrive(test_data)
class Test(TestCase):
    """查询计划模板"""
    owner = "czs"
    timeout = 5
    priority = TestCase.EnumPriority.High
    status = TestCase.EnumStatus.Ready
    tags = "egs_template_7"

    def pre_test(self):
        # 初始化各类资源
        pre_guard_template()
        add_guard_template(self.casedata)
        pass

    def run_test(self):
        self.start_step("查询计划模板")
        content = query_template("pageSize=5&curPage=1&domain_name=%s" % self.casedata["template_name"], "template_name")
        self.startStep("查询计划模板校验")
        is_flag = check_data_true(self.casedata["template_name"], content)
        self.assert_("校验状态码", is_flag is False)
        print(content)


    def post_test(self):
        self.start_step("清理数据")
        delete_guard_template()



if __name__ == '__main__':
    Test().debug_run()
