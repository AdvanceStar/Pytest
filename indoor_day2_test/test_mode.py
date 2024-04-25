import pytest


@pytest.fixture(scope="function", params=['ziyuan', 'daiyu', 'xiaowu'], ids=['1', '2', '3'], name='aaa')
def fun_fixture(request):   # request是固定写法，将参数params传入，调用时同样为request.param
    print('\n前置处理')
    yield request.param
    print('\n后置处理')


@pytest.fixture(scope="class")
def class_fixture():
    print('\nclass前置处理')
    yield
    print('\nclass后置处理')


@pytest.mark.usefixtures("class_fixture")
class BaaLearn:
    def test_main1(self):
        print('\ntest1')

    def test_main2(self, aaa):
        print('\ntest2')

        print('\nparam: ' + str(aaa))


class BaaLearn2:
    def test_main3(self):
        print('\ntest3')
    
    def test_main4(self):
        print('\ntest4')
    
    def test_main5(self):
        print('\ntest5')


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