import pytest
import time

def test_04_func():
    # time.sleep(3)
    print('指定目录下的函数')

class TestFolder:
    age = 18

    @pytest.mark.usermana
    def test_folder_main(self):
        print("folder entered!")
    
    @pytest.mark.smoke
    def test_folder_main1(self):
        print("folder entered1!")
        # assert 1 == 2
    
    @pytest.mark.mana
    @pytest.mark.skipif(age <= 28, reason="我大抵是已经释怀了")
    def test_folder_main2(self):
        print("folder entered2!")
    
    @pytest.mark.mana
    @pytest.mark.smoke
    @pytest.mark.skip(reason="喜欢仙交林黛玉而不是大明星小舞")
    def test_folder_main3(self):
        print("folder entered!")

    @pytest.mark.run(order=1)
    def test_folder_main4(self):
        # time.sleep(3)
        print("folder entered!")
