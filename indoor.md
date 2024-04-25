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
    1. pytest单元测试框架是自动化测试框架组分之一（pytest是unitest的封装和改进，unitest也需要学）
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
2. pytest可与selenium，requests，appium结合分别实现web自动化，接口自动化，app自动化
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
       1. 命令行指令补上：`--html file_name`
       2. 主函数模式补上参数：`--html=file_name`
    9.  pytest --version：检测版本及是否安装成功
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

# Pytest框架实现前后置处理
前后置 = 固件 = 夹具，几种说法而已。

web自动化执行前，是否需要打开浏览器？执行后，是否需要打开浏览器？通过夹具实现这些功能。
## Chapter 1: setup/teardown, setup_class/teardown_class
(setup对应setup_method，本机使用setup可行但是会有warning，改用method即可)
```python
import pytest

class AaaLearn:
    def setup_class(self):
        """所有用例前仅执行一次"""
        print('\n在执行类前的程序：创建日志对象，创建和数据库连接，创建接口请求对象')

    def setup_method(self):
        """所有用例前都执行一次"""
        print('\n在执行测试用例前的程序：打开浏览器')

    def test_main1(self):
        print('\ntest1')

    def test_main2(self):
        print('\ntest2')
    
    def test_main3(self):
        print('\ntest3')
        # raise Exception('不再回头')
    
    def test_main4(self):
        print('\ntest4')
    
    @pytest.mark.run(order=1)
    def test_main5(self):
        print('\ntest5')
    
    def teardown_method(self):
        print('\n测试用例执行后的程序：关闭浏览器')
    
    def teardown_class(self):
        print('\n测试类后的程序：销毁日志对象，销毁数据库连接，销毁接口请求对象')
```
## Chapter2: 使用@pytest.fixture()
可实现全部或`部分`用例的前后置。
```python
@pytest.fixture(scope="", params="", autouse="", ids="", name="")
```
参数说明：
1. scope：作用域。function(默认)，class，module，package/session
   1. 指定function使用时将放入函数参数中
      ```python
      def test_main2(self, fun_fixture):
          print('\ntest2')
      ``` 
   2. 指定class添加装饰器
      ```python
      @pytest.mark.usefixtures("class_fixture")
      ``` 
2. params: 参数化。支持list[]、tuple()、字典列表[{},{},...]、字典元组({},{},...)
   1. request是固定写法，将参数params传入，调用时同样为request.param
   2. 前后置和参数化独立可以同时存在，可以使用yield在前置后、后置前进行参数返回（return和yield都表示返回，return后后续不可以有程序，yield则可以）
    ```python
    import pytest

    @pytest.fixture(scope="function", params=['ziyuan', 'daiyu', 'xiaowu'], ids=['1', '2', '3'])
    def fun_fixture(request):
        return request.param

    @pytest.fixture(scope="class")
    def class_fixture():
        print('\nclass前置处理')
        yield
        print('\nclass后置处理')


    @pytest.mark.usefixtures("class_fixture")
    class BaaLearn:
        def test_main1(self):
            print('\ntest1')

        def test_main2(self, fun_fixture):
            print('\ntest2')

            print('\nparam: ' + str(fun_fixture))
    ```
3. autouse=True: 自动执行，默认为False
4. ids：当使用params参数化时，给每个值设置一个变量名，意义不大（一般是中文导致参数为编码，使用ids进行代替会好看点或者进行编号）
5. name：给被@pytest.fixture标记的方法取别名(取了别名后不可以再用原名)

## Chapter3: 使用conftest.py和pytest.fixture()结合使用产生`全局前置应用`
如项目全局登录，模块全局处理
1. conftest.py单独存放的一个夹具配置文件，名称不可更改;
2. 用处：在不同.py文件中采用相同前置;
3. 位置：放置在用例的同层级文件夹中，并且不用进行import操作（原则上同层级，`效力`上：同文件>同目录>外层目录）

## pytest结合allure-pytest生成allure测试报告
pytest-html -> allure-pytest
1. 配置allure环境
   1. 下载:https://github.com/allure-framework/allure2/releases
   2. 解压
   3. 配置path路径（./bin加入环境变量）
   4. 验证：allure --version（cmd以及vs下的cmd）
2. 配置参数生成临时json报告
3. 生成allure报告
    ```python
    os.system('allure generate ./allurepaper -o ./report_allure --clean')
    ``` 
    1. allure generate: 执行指令
    2. ./allurepaper: json保存路径
    3. -o: 输出指令
    4. ./report_allure: 新报告生成路径
    5. --clean: 清空输出路径下原报告
 4. 查看报告
     ```python
     os.system("allure open ./report_allure")
     ``` 
