# Test file for Problem 7: extract_elements - gemini_cot
import sys
sys.path.insert(0, '.')
from sol_07_extract_elements_gemini_cot import extract_elements

def test_extract_elements_001():
    assert extract_elements([1, 1, 3, 4, 4, 5, 6, 7],2)==[1, 4]

def test_extract_elements_002():
    assert extract_elements([0, 1, 2, 3, 4, 4, 4, 4, 5, 7],4)==[4]

def test_extract_elements_003():
    assert extract_elements([0,0,0,0,0],5)==[0]

def test_extract_elements_004():
    assert extract_elements([3, 4, 8, 1, 6, 8, 1, 4], 1) == [3, 4, 8, 1, 6, 8, 1, 4]

def test_extract_elements_005():
    assert extract_elements([3, 1, 5, 4, 3, 3, 8, 6], 2) == [3]

def test_extract_elements_006():
    assert extract_elements([1, 1, 2, 2, 2, 8, 11, 8], 4) == []

def test_extract_elements_007():
    assert extract_elements([5, 3, 3, 9, 7, 3, 8, 4], 5) == []

def test_extract_elements_008():
    assert extract_elements([2, 2, 6, 8, 7, 9, 10, 7], 5) == []

def test_extract_elements_009():
    assert extract_elements([3, 6, 5, 6, 7, 8, 2, 10], 6) == []

def test_extract_elements_010():
    assert extract_elements([5, 6, 1, 8, 7, 4, 6, 10], 2) == []

def test_extract_elements_011():
    assert extract_elements([3, 5, 1, 8, 6, 3, 3, 8], 5) == []

def test_extract_elements_012():
    assert extract_elements([4, 6, 7, 8, 5, 2, 5, 7], 2) == []

def test_extract_elements_013():
    assert extract_elements([2, 5, 7, 3, 4, 7, 6, 4], 7) == []

def test_extract_elements_014():
    assert extract_elements([3, 2, 3, 6, 6, 9, 11, 7], 6) == []

def test_extract_elements_015():
    assert extract_elements([6, 6, 6, 9, 7, 9, 11, 12], 1) == [9, 7, 9, 11, 12]

def test_extract_elements_016():
    assert extract_elements([3, 4, 5, 1, 3, 10, 2, 9], 5) == []

def test_extract_elements_017():
    assert extract_elements([1, 2, 8, 2, 8, 1, 6, 7], 1) == [1, 2, 8, 2, 8, 1, 6, 7]

def test_extract_elements_018():
    assert extract_elements([1, 4, 8, 5, 8, 8, 10, 3], 7) == []

def test_extract_elements_019():
    assert extract_elements([1, 1, 6, 7, 1, 8, 6, 10], 3) == []

def test_extract_elements_020():
    assert extract_elements([4, 3, 8, 8, 3, 10, 9, 5], 5) == []

def test_extract_elements_021():
    assert extract_elements([3, 6, 5, 1, 1, 5, 2, 4], 2) == [1]

def test_extract_elements_022():
    assert extract_elements([4, 3, 4, 3, 9, 5, 2, 10], 1) == [4, 3, 4, 3, 9, 5, 2, 10]

def test_extract_elements_023():
    assert extract_elements([2, 2, 2, 9, 9, 8, 2, 12], 6) == []

def test_extract_elements_024():
    assert extract_elements([1, 1, 4, 5, 5, 4, 5, 11], 4) == []

def test_extract_elements_025():
    assert extract_elements([4, 5, 6, 5, 7, 2, 1, 5], 7) == []

def test_extract_elements_026():
    assert extract_elements([6, 5, 3, 7, 1, 9, 8, 7], 6) == []

def test_extract_elements_027():
    assert extract_elements([5, 1, 7, 6, 5, 9, 4, 2], 5) == []

def test_extract_elements_028():
    assert extract_elements([5, 6, 1, 1, 6, 5, 9, 6], 5) == []

def test_extract_elements_029():
    assert extract_elements([1, 4, 2, 5, 1, 5, 1, 7], 5) == []

def test_extract_elements_030():
    assert extract_elements([1, 5, 8, 1, 5, 10, 10, 3], 6) == []

def test_extract_elements_031():
    assert extract_elements([1, 4, 5, 3, 7, 2, 9, 6], 7) == []

def test_extract_elements_032():
    assert extract_elements([3, 1, 3, 7, 3, 10, 5, 12], 3) == []

def test_extract_elements_033():
    assert extract_elements([6, 4, 4, 8, 8, 4, 8, 2], 1) == [6, 4, 8, 2]

def test_extract_elements_034():
    assert extract_elements([1, 1, 3, 6, 8, 10, 10, 8], 6) == []

def test_extract_elements_035():
    assert extract_elements([6, 2, 6, 9, 5, 5, 1, 9], 6) == []

def test_extract_elements_036():
    assert extract_elements([1, 4, 8, 2, 1, 6, 11, 11], 5) == []

def test_extract_elements_037():
    assert extract_elements([1, 6, 4, 3, 5, 9, 3, 7, 1, 6], 8) == []

def test_extract_elements_038():
    assert extract_elements([4, 1, 1, 6, 4, 2, 8, 9, 10, 11], 9) == []

def test_extract_elements_039():
    assert extract_elements([3, 1, 4, 1, 9, 8, 3, 5, 5, 5], 6) == []

def test_extract_elements_040():
    assert extract_elements([3, 3, 1, 2, 5, 6, 7, 3, 5, 9], 9) == []

def test_extract_elements_041():
    assert extract_elements([1, 1, 6, 1, 5, 3, 4, 6, 7, 2], 5) == []

def test_extract_elements_042():
    assert extract_elements([1, 6, 1, 8, 1, 3, 8, 9, 2, 5], 2) == []

def test_extract_elements_043():
    assert extract_elements([3, 3, 7, 1, 1, 6, 8, 4, 8, 7], 9) == []

def test_extract_elements_044():
    assert extract_elements([3, 2, 3, 4, 4, 2, 2, 5, 6, 2], 6) == []

def test_extract_elements_045():
    assert extract_elements([2, 5, 4, 4, 3, 6, 9, 6, 3, 2], 2) == [4]

def test_extract_elements_046():
    assert extract_elements([4, 6, 1, 5, 9, 9, 6, 6, 4, 7], 4) == []

def test_extract_elements_047():
    assert extract_elements([5, 4, 6, 6, 1, 7, 2, 7, 4, 9], 8) == []

def test_extract_elements_048():
    assert extract_elements([3, 1, 2, 1, 2, 4, 6, 6, 6, 9], 6) == []

def test_extract_elements_049():
    assert extract_elements([1, 4, 3, 7, 9, 1, 1, 6, 5, 10], 7) == []

def test_extract_elements_050():
    assert extract_elements([1, 3, 2, 4, 7, 2, 9, 3, 2, 6], 7) == []

def test_extract_elements_051():
    assert extract_elements([2, 4, 7, 2, 6, 8, 4, 5, 7, 8], 5) == []

def test_extract_elements_052():
    assert extract_elements([4, 4, 5, 4, 8, 5, 7, 1, 2, 2], 6) == []

def test_extract_elements_053():
    assert extract_elements([3, 4, 5, 1, 4, 3, 2, 3, 5, 8], 5) == []

def test_extract_elements_054():
    assert extract_elements([4, 1, 6, 5, 9, 4, 8, 3, 2, 7], 2) == []

def test_extract_elements_055():
    assert extract_elements([4, 5, 6, 6, 8, 2, 4, 6, 6, 5], 5) == []

def test_extract_elements_056():
    assert extract_elements([2, 1, 5, 8, 8, 6, 4, 7, 6, 9], 6) == []

def test_extract_elements_057():
    assert extract_elements([1, 5, 3, 1, 7, 3, 1, 9, 4, 10], 5) == []

def test_extract_elements_058():
    assert extract_elements([3, 6, 5, 6, 2, 2, 4, 9, 7, 8], 6) == []

def test_extract_elements_059():
    assert extract_elements([4, 4, 7, 4, 4, 5, 6, 7, 5, 4], 8) == []

def test_extract_elements_060():
    assert extract_elements([2, 1, 3, 3, 1, 7, 5, 2, 2, 2], 6) == []

def test_extract_elements_061():
    assert extract_elements([4, 2, 5, 6, 6, 9, 5, 2, 7, 6], 4) == []

def test_extract_elements_062():
    assert extract_elements([1, 5, 4, 1, 5, 9, 6, 2, 2, 7], 1) == [1, 5, 4, 1, 5, 9, 6, 7]

def test_extract_elements_063():
    assert extract_elements([3, 1, 1, 4, 5, 8, 6, 3, 3, 12], 7) == []

def test_extract_elements_064():
    assert extract_elements([3, 4, 7, 4, 3, 3, 1, 6, 9, 6], 8) == []

def test_extract_elements_065():
    assert extract_elements([4, 2, 2, 8, 3, 2, 4, 4, 8, 9], 7) == []

def test_extract_elements_066():
    assert extract_elements([3, 2, 7, 7, 2, 7, 4, 3, 2, 12], 9) == []

def test_extract_elements_067():
    assert extract_elements([5, 3, 4, 2, 8, 9, 7, 4, 2, 9], 7) == []

def test_extract_elements_068():
    assert extract_elements([4, 6, 2, 5, 6, 5, 8, 3, 10, 2], 1) == [4, 6, 2, 5, 6, 5, 8, 3, 10, 2]

def test_extract_elements_069():
    assert extract_elements([4, 4, 5, 1, 2, 1, 4, 2, 9, 7], 9) == []

def test_extract_elements_070():
    assert extract_elements([1, 5, 3, 3, 1], 9) == []

def test_extract_elements_071():
    assert extract_elements([5, 4, 4, 3, 4], 1) == [5, 3, 4]

def test_extract_elements_072():
    assert extract_elements([1, 2, 4, 1, 5], 8) == []

def test_extract_elements_073():
    assert extract_elements([2, 5, 3, 4, 1], 10) == []

def test_extract_elements_074():
    assert extract_elements([3, 4, 4, 4, 4], 6) == []

def test_extract_elements_075():
    assert extract_elements([1, 1, 2, 1, 5], 7) == []

def test_extract_elements_076():
    assert extract_elements([2, 2, 1, 4, 2], 3) == []

def test_extract_elements_077():
    assert extract_elements([1, 4, 3, 5, 1], 4) == []

def test_extract_elements_078():
    assert extract_elements([4, 2, 1, 4, 5], 7) == []

def test_extract_elements_079():
    assert extract_elements([1, 1, 3, 4, 1], 7) == []

def test_extract_elements_080():
    assert extract_elements([2, 3, 5, 5, 5], 6) == []

def test_extract_elements_081():
    assert extract_elements([5, 1, 1, 4, 2], 6) == []

def test_extract_elements_082():
    assert extract_elements([3, 4, 2, 1, 1], 8) == []

def test_extract_elements_083():
    assert extract_elements([2, 4, 4, 3, 3], 2) == [4, 3]

def test_extract_elements_084():
    assert extract_elements([3, 2, 2, 5, 2], 3) == []

def test_extract_elements_085():
    assert extract_elements([3, 1, 3, 1, 2], 9) == []

def test_extract_elements_086():
    assert extract_elements([1, 1, 1, 2, 5], 9) == []

def test_extract_elements_087():
    assert extract_elements([2, 4, 4, 1, 3], 6) == []

def test_extract_elements_088():
    assert extract_elements([2, 5, 4, 1, 4], 4) == []

def test_extract_elements_089():
    assert extract_elements([4, 3, 5, 5, 1], 1) == [4, 3, 1]

def test_extract_elements_090():
    assert extract_elements([3, 3, 3, 5, 1], 10) == []

def test_extract_elements_091():
    assert extract_elements([2, 1, 4, 1, 4], 10) == []

def test_extract_elements_092():
    assert extract_elements([2, 3, 2, 4, 1], 10) == []

def test_extract_elements_093():
    assert extract_elements([3, 3, 1, 5, 5], 7) == []

def test_extract_elements_094():
    assert extract_elements([5, 2, 1, 4, 2], 6) == []

def test_extract_elements_095():
    assert extract_elements([4, 4, 3, 2, 4], 6) == []

def test_extract_elements_096():
    assert extract_elements([5, 3, 2, 5, 5], 10) == []

def test_extract_elements_097():
    assert extract_elements([3, 4, 3, 5, 5], 2) == [5]

def test_extract_elements_098():
    assert extract_elements([2, 3, 1, 2, 4], 5) == []

def test_extract_elements_099():
    assert extract_elements([4, 5, 3, 1, 3], 2) == []

def test_extract_elements_100():
    assert extract_elements([2, 2, 5, 5, 5], 7) == []

def test_extract_elements_101():
    assert extract_elements([4, 1, 2, 3, 4], 6) == []

def test_extract_elements_102():
    assert extract_elements([4, 5, 5, 4, 2], 4) == []

