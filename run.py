import sys
sys.path.append(r"E:\自动化\new_enovate_interface_auto")

import os
import pytest
import zmail


if __name__ == '__main__':
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 report/temp 目录
    pytest.main(['--alluredir', './report/temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate --clean ./report/temp -o ./report/report')

    # pytest.main()
    mail_content = {
        "subject": "哈哈",
        "content_text": "测试测试,测试报告链接为\nhttp://localhost:63342/new_test_enovate_interface/report/report/index.html",
        # "attachments": r"E:\自动化\new_enovate_interface_auto\report\report\index.html"  # 邮件附件（路径）
    }
    server = zmail.server("souldmly@163.com", "VREUQQHJPYSFWQDY")
    server.send_mail("1356798645@qq.com", mail_content)
