from usslib.egs.guard_template.lib.guard_fun import *
from usslib.egs.guard_acess.lib.access_fun import *
from usslib.base.person.lib.person_fun import *
from usslib.egs.guard_acess.data.access_data import *

from testbase.testcase import TestCase
from testbase import datadrive

test_data = access_add_dict


@datadrive.DataDrive(test_data)
class Test(TestCase):
    """按门禁组添加权限"""
    owner = "czs"
    timeout = 5
    priority = TestCase.EnumPriority.High
    status = TestCase.EnumStatus.Ready
    tags = "egs_access_1"

    def pre_test(self):
        # 初始化各类资源
        Test.data = re_test_access_data()
        pass

    # person_list, class_list, holiday_list, point_list
    def run_test(self):
        self.start_step("按门禁组添加权限")
        json_data = self.casedata
        status_code, content = add_access_fun(json_data, Test.data)
        print(content)
        self.assert_("校验状态码", status_code == status_200)

    def post_test(self):
        self.start_step("清理数据")
        delete_access(one_url="page_size=5&cur_page=1&name=%s&query_way=access" % self.casedata["id"])
        post_test_access_data()


if __name__ == '__main__':
    Test().debug_run()