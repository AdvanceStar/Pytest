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
## 单元测试框架VS自动化测试框架
1. 自动化测试框架
2. 作用
    1. 提高测试效率，降低维护成本
    2. 减少人工干预，提高测试准确性，增加代码复用性
    3. 核心思想：让不懂程序的人能够是哦那个并进行自动化测试
3. pytest单元测试框架VS自动化测试框架
    1. 大暖测试框架是自动化测试框架组分之一
    2. pom设计模式
    3. 数据驱动
    4. 关键字驱动
    5. 全局配准文件的封装
    6. 日志监控
    7. selenium，requests二次封装
    8. 断言
    9. 报告邮件
    10. ...
## pytest简介
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
## pytest默认的测试用例规则和基础应用
1. 模块名需以test_开头或_test结尾（文件名）
2. 测试类必须以Test开头，不可以有init方法
3. 测试方法必须以test开头
## pytest测试用例运行方式
1. 主函数模式
2. 命令行模式
3. 读取pytest.ini配置文件运行