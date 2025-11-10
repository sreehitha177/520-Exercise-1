# Test file for Problem 10: min_sum_path - chatgpt_self_planning
import sys
sys.path.insert(0, '.')
from sol_10_min_sum_path_chatgpt_self_planning import min_sum_path

def test_min_sum_path_001():
    assert min_sum_path([[ 2 ], [3, 9 ], [1, 6, 7 ]]) == 6

def test_min_sum_path_002():
    assert min_sum_path([[ 2 ], [3, 7 ], [8, 5, 6 ]]) == 10

def test_min_sum_path_003():
    assert min_sum_path([[ 3 ], [6, 4 ], [5, 2, 7 ]]) == 9

def test_min_sum_path_004():
    assert min_sum_path([[7], [5, 12], [3, 3, 10]]) == 15

def test_min_sum_path_005():
    assert min_sum_path([[6], [5, 10], [6, 4, 11]]) == 15

def test_min_sum_path_006():
    assert min_sum_path([[2], [7, 9], [5, 2, 9]]) == 11

def test_min_sum_path_007():
    assert min_sum_path([[1], [5, 6], [2, 6, 9]]) == 8

def test_min_sum_path_008():
    assert min_sum_path([[7], [4, 12], [3, 3, 8]]) == 14

def test_min_sum_path_009():
    assert min_sum_path([[1], [4, 7], [2, 1, 8]]) == 6

def test_min_sum_path_010():
    assert min_sum_path([[4], [1, 13], [4, 8, 2]]) == 9

def test_min_sum_path_011():
    assert min_sum_path([[4], [5, 10], [5, 9, 12]]) == 14

def test_min_sum_path_012():
    assert min_sum_path([[6], [2, 6], [4, 6, 4]]) == 12

def test_min_sum_path_013():
    assert min_sum_path([[3], [6, 6], [3, 10, 10]]) == 12

def test_min_sum_path_014():
    assert min_sum_path([[1], [5, 13], [4, 10, 2]]) == 10

def test_min_sum_path_015():
    assert min_sum_path([[3], [5, 13], [6, 2, 12]]) == 10

def test_min_sum_path_016():
    assert min_sum_path([[2], [5, 13], [5, 2, 8]]) == 9

def test_min_sum_path_017():
    assert min_sum_path([[3], [7, 5], [6, 3, 6]]) == 11

def test_min_sum_path_018():
    assert min_sum_path([[5], [7, 12], [2, 2, 11]]) == 14

def test_min_sum_path_019():
    assert min_sum_path([[2], [8, 14], [5, 9, 11]]) == 15

def test_min_sum_path_020():
    assert min_sum_path([[6], [7, 12], [5, 9, 4]]) == 18

def test_min_sum_path_021():
    assert min_sum_path([[6], [1, 11], [2, 9, 12]]) == 9

def test_min_sum_path_022():
    assert min_sum_path([[6], [3, 12], [4, 2, 3]]) == 11

def test_min_sum_path_023():
    assert min_sum_path([[2], [1, 10], [1, 2, 10]]) == 4

def test_min_sum_path_024():
    assert min_sum_path([[2], [6, 11], [3, 7, 11]]) == 11

def test_min_sum_path_025():
    assert min_sum_path([[1], [1, 14], [6, 1, 5]]) == 3

def test_min_sum_path_026():
    assert min_sum_path([[7], [8, 10], [2, 4, 6]]) == 17

def test_min_sum_path_027():
    assert min_sum_path([[3], [7, 11], [5, 3, 11]]) == 13

def test_min_sum_path_028():
    assert min_sum_path([[6], [6, 4], [3, 5, 8]]) == 15

def test_min_sum_path_029():
    assert min_sum_path([[3], [8, 12], [6, 2, 4]]) == 13

def test_min_sum_path_030():
    assert min_sum_path([[7], [6, 9], [1, 6, 10]]) == 14

def test_min_sum_path_031():
    assert min_sum_path([[2], [6, 11], [6, 2, 12]]) == 10

def test_min_sum_path_032():
    assert min_sum_path([[3], [4, 9], [4, 2, 7]]) == 9

def test_min_sum_path_033():
    assert min_sum_path([[4], [8, 6], [3, 6, 7]]) == 15

def test_min_sum_path_034():
    assert min_sum_path([[6], [7, 5], [6, 9, 3]]) == 14

def test_min_sum_path_035():
    assert min_sum_path([[5], [4, 4], [4, 10, 5]]) == 13

def test_min_sum_path_036():
    assert min_sum_path([[5], [4, 10], [1, 2, 10]]) == 10

def test_min_sum_path_037():
    assert min_sum_path([[5], [5, 10], [3, 1, 10]]) == 11

def test_min_sum_path_038():
    assert min_sum_path([[6], [4, 8], [12, 8, 1]]) == 15

def test_min_sum_path_039():
    assert min_sum_path([[2], [1, 12], [3, 9, 3]]) == 6

def test_min_sum_path_040():
    assert min_sum_path([[2], [8, 3], [5, 1, 6]]) == 6

def test_min_sum_path_041():
    assert min_sum_path([[2], [3, 8], [7, 7, 9]]) == 12

def test_min_sum_path_042():
    assert min_sum_path([[2], [2, 11], [12, 2, 11]]) == 6

def test_min_sum_path_043():
    assert min_sum_path([[7], [6, 5], [10, 5, 2]]) == 14

def test_min_sum_path_044():
    assert min_sum_path([[1], [7, 7], [5, 10, 1]]) == 9

def test_min_sum_path_045():
    assert min_sum_path([[2], [1, 10], [13, 1, 7]]) == 4

def test_min_sum_path_046():
    assert min_sum_path([[7], [5, 9], [13, 7, 8]]) == 19

def test_min_sum_path_047():
    assert min_sum_path([[2], [8, 11], [11, 8, 6]]) == 18

def test_min_sum_path_048():
    assert min_sum_path([[1], [5, 10], [8, 2, 6]]) == 8

def test_min_sum_path_049():
    assert min_sum_path([[6], [2, 4], [7, 1, 6]]) == 9

def test_min_sum_path_050():
    assert min_sum_path([[6], [1, 2], [12, 7, 9]]) == 14

def test_min_sum_path_051():
    assert min_sum_path([[1], [3, 5], [10, 1, 8]]) == 5

def test_min_sum_path_052():
    assert min_sum_path([[4], [2, 7], [4, 4, 8]]) == 10

def test_min_sum_path_053():
    assert min_sum_path([[5], [8, 2], [8, 5, 10]]) == 12

def test_min_sum_path_054():
    assert min_sum_path([[1], [1, 10], [6, 4, 5]]) == 6

def test_min_sum_path_055():
    assert min_sum_path([[6], [6, 3], [6, 1, 8]]) == 10

def test_min_sum_path_056():
    assert min_sum_path([[4], [4, 7], [12, 8, 11]]) == 16

def test_min_sum_path_057():
    assert min_sum_path([[2], [3, 8], [9, 5, 3]]) == 10

def test_min_sum_path_058():
    assert min_sum_path([[7], [6, 12], [4, 5, 5]]) == 17

def test_min_sum_path_059():
    assert min_sum_path([[6], [7, 11], [8, 6, 9]]) == 19

def test_min_sum_path_060():
    assert min_sum_path([[6], [8, 9], [10, 10, 6]]) == 21

def test_min_sum_path_061():
    assert min_sum_path([[4], [7, 10], [12, 8, 11]]) == 19

def test_min_sum_path_062():
    assert min_sum_path([[2], [4, 7], [6, 3, 4]]) == 9

def test_min_sum_path_063():
    assert min_sum_path([[5], [3, 12], [9, 8, 9]]) == 16

def test_min_sum_path_064():
    assert min_sum_path([[3], [3, 12], [7, 9, 7]]) == 13

def test_min_sum_path_065():
    assert min_sum_path([[2], [2, 10], [7, 4, 3]]) == 8

def test_min_sum_path_066():
    assert min_sum_path([[1], [7, 9], [6, 4, 10]]) == 12

def test_min_sum_path_067():
    assert min_sum_path([[7], [1, 11], [12, 9, 4]]) == 17

def test_min_sum_path_068():
    assert min_sum_path([[2], [6, 9], [10, 4, 5]]) == 12

def test_min_sum_path_069():
    assert min_sum_path([[3], [4, 9], [3, 8, 5]]) == 10

def test_min_sum_path_070():
    assert min_sum_path([[4], [4, 8], [2, 7, 7]]) == 10

def test_min_sum_path_071():
    assert min_sum_path([[4], [4, 1], [10, 6, 7]]) == 11

def test_min_sum_path_072():
    assert min_sum_path([[4], [4, 6], [7, 7, 6]]) == 15

def test_min_sum_path_073():
    assert min_sum_path([[3], [8, 6], [8, 2, 12]]) == 11

def test_min_sum_path_074():
    assert min_sum_path([[8], [6, 1], [3, 4, 4]]) == 13

def test_min_sum_path_075():
    assert min_sum_path([[1], [8, 4], [5, 5, 12]]) == 10

def test_min_sum_path_076():
    assert min_sum_path([[7], [7, 4], [7, 2, 10]]) == 13

def test_min_sum_path_077():
    assert min_sum_path([[4], [11, 8], [2, 1, 9]]) == 13

def test_min_sum_path_078():
    assert min_sum_path([[3], [2, 8], [2, 3, 6]]) == 7

def test_min_sum_path_079():
    assert min_sum_path([[1], [11, 8], [6, 5, 9]]) == 14

def test_min_sum_path_080():
    assert min_sum_path([[4], [9, 3], [1, 5, 6]]) == 12

def test_min_sum_path_081():
    assert min_sum_path([[1], [8, 3], [4, 2, 8]]) == 6

def test_min_sum_path_082():
    assert min_sum_path([[3], [1, 6], [8, 5, 4]]) == 9

def test_min_sum_path_083():
    assert min_sum_path([[2], [6, 4], [9, 6, 3]]) == 9

def test_min_sum_path_084():
    assert min_sum_path([[8], [8, 4], [2, 7, 10]]) == 18

def test_min_sum_path_085():
    assert min_sum_path([[2], [7, 1], [6, 1, 5]]) == 4

def test_min_sum_path_086():
    assert min_sum_path([[3], [1, 4], [4, 1, 10]]) == 5

def test_min_sum_path_087():
    assert min_sum_path([[6], [3, 4], [4, 4, 5]]) == 13

def test_min_sum_path_088():
    assert min_sum_path([[4], [11, 3], [1, 1, 3]]) == 8

def test_min_sum_path_089():
    assert min_sum_path([[8], [2, 7], [1, 4, 5]]) == 11

def test_min_sum_path_090():
    assert min_sum_path([[1], [3, 4], [8, 7, 3]]) == 8

def test_min_sum_path_091():
    assert min_sum_path([[3], [7, 7], [1, 1, 4]]) == 11

def test_min_sum_path_092():
    assert min_sum_path([[3], [8, 7], [2, 1, 10]]) == 11

def test_min_sum_path_093():
    assert min_sum_path([[6], [8, 5], [2, 5, 6]]) == 16

def test_min_sum_path_094():
    assert min_sum_path([[7], [3, 1], [7, 5, 10]]) == 13

def test_min_sum_path_095():
    assert min_sum_path([[6], [7, 5], [5, 5, 12]]) == 16

def test_min_sum_path_096():
    assert min_sum_path([[2], [2, 5], [2, 2, 8]]) == 6

def test_min_sum_path_097():
    assert min_sum_path([[7], [11, 9], [4, 3, 9]]) == 19

def test_min_sum_path_098():
    assert min_sum_path([[8], [4, 6], [5, 7, 12]]) == 17

def test_min_sum_path_099():
    assert min_sum_path([[7], [6, 3], [2, 5, 6]]) == 15

def test_min_sum_path_100():
    assert min_sum_path([[5], [3, 3], [8, 1, 7]]) == 9

def test_min_sum_path_101():
    assert min_sum_path([[5], [6, 6], [3, 3, 9]]) == 14

def test_min_sum_path_102():
    assert min_sum_path([[4], [3, 3], [1, 7, 8]]) == 8

