# pytest入门教学
https://www.bilibili.com/video/BV1py4y1t7bJ/?p=2&spm_id_from=pageDriver&vd_source=0d0be4827220d10b42080ec061114bb1
## Chapter 1: pytest单元测试框架
1. 单元测试框架
    单元测试之软件开发中针对软件最小单位（函数、方法）进行正确性测试。
2. 主流框架
    java: junit, testng
    python: unittest, pytest
3. 功能
    1. 测试发现：多个文件找到测试用例
    2. 测试执行：按照一定顺序和规则执行，生成结果
    3. 测试判断：通过断言判断预期结果和实际结果的差异
    4. 测试报告：统计测试进度，耗时，通过率，生成测试报告
## Chapter 2: 单元测试框架VS自动化测试框架
1. 自动化测试框架
2. 作用
    1. 提高测试效率，降低维护成本
    2. 减少人工干预，提高测试准确性，增加代码复用性
    3. 核心思想：让不懂程序的人能够是哦那个并进行自动化测试
3. pytest单元测试框架VS自动化测试框架
    1. 单元测试框架是自动化测试框架组分之一
    2. pom设计模式
    3. 数据驱动
    4. 关键字驱动
    5. 全局配准文件的封装
    6. 日志监控
    7. selenium，requests二次封装
    8. 断言
    9. 报告邮件
    10. ...
## Chapter 3: pytest简介
1. pytest成熟的python单元框架，易上手
2. pytest可与selenium，requests，appium结合实现web自动化，接口自动化，app自动化
3. 可实现测试用例跳过及reruns失败用例重试
4. 和allure生成美观的测试报告
5. 与jenkins持续集成
6. 插件丰富，有很多使用操作
    1. pytest
    2. pytest-html（生成html格式自动化测试报告）
    3. pytest-xdist，分布式执行测试用例，多cpu分发
    4. pytest-ordering 改变测试用例执行顺序
    5. pytest-rerunfailures 用例失败后重跑
    6. allure-pytest 生成美观的测试用例
## Chapter 4: pytest默认的测试用例规则和基础应用
1. 模块名需以test_开头或_test结尾（文件名）
2. 测试类必须以Test开头，不可以有init方法
3. 测试方法必须以test开头
## Chapter 5: pytest测试用例运行方式
1. 主函数模式:直接点击常规的运行即可执行所有用例或部分用例
    ```python
    import pytest
    class TestLogin:
        def test_01(self):
            print("test 1")

    if __name__ == "__main__":
        pytest.main(['-vs', 'test_login.py', 'test_login.py'])
    ```
    1. 任意文件下运行pytest.main()都会运行所有测试用例
    2. 在pytest.main中可传入参数
    3. 运行指定模块：默认情况下运行所有测试用例
       1. 运行所有：`pytest.main()`
       2. 指定模块：`pytest.main(['-vs', 'test_login.py'])`
       3. 指定目录：`pytest.main(['-vs', './test_folder'])`
       4. 通过nodeid指定用例运行：nodeid由模块名+分隔符+类名/方法名/函数名组成。
          ```python
          pytest.main(['-vs', './test_folder/test_folder_set_call.py::TestFolder::test_folder_main'])
          pytest.main(['-vs', './test_folder/test_folder_set_call.py::test_04_func'])
          ```
2. 命令行模式:使用`pytest`即可执行
   ```
   pytest -vs test_login.py
   ```
   也可以输入参数，参数列表同上,后面跟的是测试的例子，同样可以选择运行指定的文件或者目录。
    1. 运行所有：`pytest`
    2. 指定文件：`pytest -vs test_login.py`
    3. 指定目录：`pytest -vs ./test_folder`
    4. 通过nodeid指定用例运行：`pytest -vs ./test_folder/test_folder_set_call.py::test_04_func`
3. **读取pytest.ini配置文件运行**
   1. 位置：一般放在项目根目录
   2. 编码：必须是`ANSI`，可使用notepad++修改编码格式
   3. 作用：改变pytest的默认行为
   4. 运行规则：主函数运行模式/命令行模式均需参考该文件的修改产生默认的参数
   ```python
   [pytest]
   addopts = -vs               # 命令行参数，用空格分隔
   testpaths = ./test_folder   # 测试用例路径
   python_files = test_*.py    # 模块名规则
   python_classes = Test*      # 类名规则
   python_functions = test     # 方法名规则
   ```
4. 参数说明
    1. -s: 输出调试信息以及print的输出
    2. -v: 输出更详细信息（模块名+类名+方法名）
    3. -n: 支持多线程或者分布式运行测试用例
       1. 命令行执行：`pytest -vs ./test_folder -n 2`，其中2表示对应的线程数量。
       2. 主函数运行：`pytest.main(['-vs', './test_folder', '-n=2'])`
    4. 失败用例重跑：`'--reruns=2'`
       1. 命令行执行：末尾添加`--reruns 2`
       2. 主函数运行：添加参数`'--reruns=2'`
    5. -x：存在一个用例报错，程序停止，后续的例子不会继续运行
    6. --maxfail=NUM：出现NUM个错误时程序停止
    7. -k：只执行包含指定字符串的函数或方法：`pytest -vs ./test_folder -k "ao"`
    8. --html file_name：生成报告
    9. pytest --version：检测版本及是否安装成功
## Chapter 6: 执行测试用例的顺序
1. 默认执行顺序为`从上到下`
2. 改变顺序：装饰器标记
    ```python
    @pytest.mark.run(order=1)
    def test_folder_main4(self):
        time.sleep(3)
        print("folder entered!")
    ```
## Chapter 7: 分组执行(分模块、分接口、web执行)
通过装饰器标记+.ini，在执行中添加指令
```
pytest -m "smoke or mana"
```
对应的在.ini中也需要进行修改，添加上对应的marker类别
```ini
[pytest]
addopts = -vsx --html ./report/report.html
testpaths = 
python_files = test_*.py
python_classes = Test*
python_functions = test
markers =
    smoke: 用例1
    usermana: 用例2
    mana: 用例3
```

## Chapter 8: 跳过测试用例
作为装饰器标记在方法名前。
1. 无条件跳过
    ```python
    @pytest.mark.skip(reason="喜欢仙交林黛玉而不是大明星小舞")
    ```
2. 有条件跳过
    ```python
    @pytest.mark.skipif(age <= 28, reason="我大抵是已经释怀了")
    ```

# 