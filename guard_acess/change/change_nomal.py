from usslib.egs.guard_template.lib.guard_fun import *

from testbase.testcase import TestCase
from testbase import datadrive

test_data = change_template_dict


@datadrive.DataDrive(test_data)
class Test(TestCase):
    """修改计划模板"""
    owner = "czs"
    timeout = 5
    priority = TestCase.EnumPriority.High
    status = TestCase.EnumStatus.Ready
    tags = "egs_template_4"

    def pre_test(self):
        # 初始化各类资源
        pre_guard_template(data=add_device_guard_wg, is_online=False)
        Test.json_data = copy.deepcopy(add_guard_template(is_return=True))
        pass

    def run_test(self):
        self.start_step("修改计划模板%s" % self.casedata[1])
        id_list = query_template()
        Test.json_data["id"] = id_list[0]
        status_code, content = change_guard_template(Test.json_data, {self.casedataname: self.casedata[0]})
        self.assert_("校验状态码", status_code == status_200)
        self.assert_("校验内容值为1", int(content) == 1)
        self.assert_("校验内容值为1", int(content) == 1)
        self.start_step("修改是否成功")
        content = check_template_success(id_list[0])
        print = content
        self.assert_("校验内容是否修改成功", content["template_name"] == self.casedata[0])

    def post_test(self):
        self.start_step("清理数据")
        delete_guard_template()
        delete_guard_point()


if __name__ == '__main__':
    Test().debug_run()
