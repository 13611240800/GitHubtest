import pytest
import yaml

from Dirpythoncode.Calculator import calculator


# import sys
#
# print(sys.path)


def get_data():
    with open('./data/calc.yaml') as f:
        data = yaml.safe_load(f)
    return data['add']['data'], data['add']['ids'], data['div']['data'], data['div']['ids']


class TestCalc:
    datas: list = get_data()

    def setup_class(self):
        self.calc = calculator()
        print('开始计算')

    def teardown_class(self):
        print('结束计算')

    @pytest.mark.parametrize('result,a,b', datas[0], ids=datas[1])
    def test_add(self, result, a, b):
        print(f'result={result},a={a},b={b}')
        # self.calc=calculator()
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize('result,a,b', datas[2], ids=datas[3])
    def test_div(self, result, a, b):
        print(f'result={result},a={a},b={b}')
        assert result == self.calc.div(a, b)
