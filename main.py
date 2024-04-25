import os
import pytest

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./allurepaper -o ./report_allure --clean')
    os.system("allure open ./report_allure ")  # 运行完直接打开报告（直接打开html文件全是404）
