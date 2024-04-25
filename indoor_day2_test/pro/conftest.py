import pytest


@pytest.fixture(scope="function", params=['ziyuan', 'daiyu', 'xiaowu'], ids=['1', '2', '3'])
def pro_fixture(request):   # request是固定写法，将参数params传入，调用时同样为request.param
    print('\n产品前置处理')
    yield request.param
    print('\n产品后置处理')
