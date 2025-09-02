import unittest

# 被測試的程式
def add(x: int, y: int) -> int:
    return x + y

def div(x: int, y: int) -> float:
    return x / y

# 測試類別要繼承 unittest.TestCase
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_div(self):
        self.assertAlmostEqual(div(10, 2), 5.0)
        # 測試是否丟出例外
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)

# 直接執行測試
if __name__ == '__main__':
    unittest.main()
