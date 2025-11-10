# Test file for Problem 6: ap_sum - chatgpt_cot
import sys
sys.path.insert(0, '.')
from sol_06_ap_sum_chatgpt_cot import ap_sum

def test_ap_sum_001():
    assert ap_sum(1,5,2)==25

def test_ap_sum_002():
    assert ap_sum(2,6,4)==72

def test_ap_sum_003():
    assert ap_sum(1,4,5)==34

def test_ap_sum_004():
    assert ap_sum(3, 2, 5) == 11.0

def test_ap_sum_005():
    assert ap_sum(3, 5, 1) == 25.0

def test_ap_sum_006():
    assert ap_sum(2, 1, 6) == 2.0

def test_ap_sum_007():
    assert ap_sum(5, 5, 2) == 45.0

def test_ap_sum_008():
    assert ap_sum(2, 5, 3) == 40.0

def test_ap_sum_009():
    assert ap_sum(5, 5, 1) == 35.0

def test_ap_sum_010():
    assert ap_sum(1, 4, 3) == 22.0

def test_ap_sum_011():
    assert ap_sum(6, 7, 4) == 126.0

def test_ap_sum_012():
    assert ap_sum(5, 4, 6) == 56.0

def test_ap_sum_013():
    assert ap_sum(1, 5, 7) == 75.0

def test_ap_sum_014():
    assert ap_sum(4, 5, 2) == 40.0

def test_ap_sum_015():
    assert ap_sum(4, 3, 6) == 30.0

def test_ap_sum_016():
    assert ap_sum(5, 1, 3) == 5.0

def test_ap_sum_017():
    assert ap_sum(6, 9, 3) == 162.0

def test_ap_sum_018():
    assert ap_sum(1, 10, 4) == 190.0

def test_ap_sum_019():
    assert ap_sum(2, 7, 5) == 119.0

def test_ap_sum_020():
    assert ap_sum(1, 4, 4) == 28.0

def test_ap_sum_021():
    assert ap_sum(1, 5, 3) == 35.0

def test_ap_sum_022():
    assert ap_sum(3, 7, 7) == 168.0

def test_ap_sum_023():
    assert ap_sum(1, 9, 4) == 153.0

def test_ap_sum_024():
    assert ap_sum(3, 5, 3) == 45.0

def test_ap_sum_025():
    assert ap_sum(1, 3, 1) == 6.0

def test_ap_sum_026():
    assert ap_sum(2, 1, 7) == 2.0

def test_ap_sum_027():
    assert ap_sum(6, 10, 7) == 375.0

def test_ap_sum_028():
    assert ap_sum(5, 4, 2) == 32.0

def test_ap_sum_029():
    assert ap_sum(1, 2, 3) == 5.0

def test_ap_sum_030():
    assert ap_sum(5, 9, 5) == 225.0

def test_ap_sum_031():
    assert ap_sum(4, 4, 1) == 22.0

def test_ap_sum_032():
    assert ap_sum(6, 6, 4) == 96.0

def test_ap_sum_033():
    assert ap_sum(4, 4, 6) == 52.0

def test_ap_sum_034():
    assert ap_sum(6, 4, 7) == 66.0

def test_ap_sum_035():
    assert ap_sum(6, 4, 1) == 30.0

def test_ap_sum_036():
    assert ap_sum(3, 6, 7) == 123.0

def test_ap_sum_037():
    assert ap_sum(4, 7, 7) == 175.0

def test_ap_sum_038():
    assert ap_sum(6, 9, 4) == 198.0

def test_ap_sum_039():
    assert ap_sum(6, 4, 1) == 30.0

def test_ap_sum_040():
    assert ap_sum(1, 7, 2) == 49.0

def test_ap_sum_041():
    assert ap_sum(1, 1, 1) == 1.0

def test_ap_sum_042():
    assert ap_sum(4, 6, 8) == 144.0

def test_ap_sum_043():
    assert ap_sum(2, 10, 3) == 155.0

def test_ap_sum_044():
    assert ap_sum(3, 4, 2) == 24.0

def test_ap_sum_045():
    assert ap_sum(6, 9, 2) == 126.0

def test_ap_sum_046():
    assert ap_sum(5, 7, 5) == 140.0

def test_ap_sum_047():
    assert ap_sum(7, 4, 6) == 64.0

def test_ap_sum_048():
    assert ap_sum(7, 1, 9) == 7.0

def test_ap_sum_049():
    assert ap_sum(6, 1, 1) == 6.0

def test_ap_sum_050():
    assert ap_sum(7, 7, 4) == 133.0

def test_ap_sum_051():
    assert ap_sum(5, 2, 4) == 14.0

def test_ap_sum_052():
    assert ap_sum(7, 2, 2) == 16.0

def test_ap_sum_053():
    assert ap_sum(6, 9, 4) == 198.0

def test_ap_sum_054():
    assert ap_sum(7, 6, 1) == 57.0

def test_ap_sum_055():
    assert ap_sum(6, 6, 7) == 141.0

def test_ap_sum_056():
    assert ap_sum(2, 10, 4) == 200.0

def test_ap_sum_057():
    assert ap_sum(2, 3, 6) == 24.0

def test_ap_sum_058():
    assert ap_sum(2, 8, 5) == 156.0

def test_ap_sum_059():
    assert ap_sum(7, 10, 8) == 430.0

def test_ap_sum_060():
    assert ap_sum(7, 11, 5) == 352.0

def test_ap_sum_061():
    assert ap_sum(2, 5, 2) == 30.0

def test_ap_sum_062():
    assert ap_sum(2, 8, 5) == 156.0

def test_ap_sum_063():
    assert ap_sum(7, 3, 1) == 24.0

def test_ap_sum_064():
    assert ap_sum(2, 2, 5) == 9.0

def test_ap_sum_065():
    assert ap_sum(3, 8, 8) == 248.0

def test_ap_sum_066():
    assert ap_sum(7, 9, 3) == 171.0

def test_ap_sum_067():
    assert ap_sum(7, 9, 8) == 351.0

def test_ap_sum_068():
    assert ap_sum(3, 10, 1) == 75.0

def test_ap_sum_069():
    assert ap_sum(1, 2, 8) == 10.0

def test_ap_sum_070():
    assert ap_sum(3, 9, 2) == 99.0

def test_ap_sum_071():
    assert ap_sum(1, 5, 10) == 105.0

def test_ap_sum_072():
    assert ap_sum(5, 4, 6) == 56.0

def test_ap_sum_073():
    assert ap_sum(3, 4, 1) == 18.0

def test_ap_sum_074():
    assert ap_sum(4, 4, 6) == 52.0

def test_ap_sum_075():
    assert ap_sum(4, 3, 9) == 39.0

def test_ap_sum_076():
    assert ap_sum(6, 4, 1) == 30.0

def test_ap_sum_077():
    assert ap_sum(6, 9, 10) == 414.0

def test_ap_sum_078():
    assert ap_sum(4, 1, 5) == 4.0

def test_ap_sum_079():
    assert ap_sum(2, 6, 4) == 72.0

def test_ap_sum_080():
    assert ap_sum(5, 4, 1) == 26.0

def test_ap_sum_081():
    assert ap_sum(5, 4, 1) == 26.0

def test_ap_sum_082():
    assert ap_sum(3, 3, 5) == 24.0

def test_ap_sum_083():
    assert ap_sum(2, 3, 5) == 21.0

def test_ap_sum_084():
    assert ap_sum(4, 5, 9) == 110.0

def test_ap_sum_085():
    assert ap_sum(6, 2, 6) == 18.0

def test_ap_sum_086():
    assert ap_sum(6, 5, 10) == 130.0

def test_ap_sum_087():
    assert ap_sum(3, 5, 4) == 55.0

def test_ap_sum_088():
    assert ap_sum(1, 7, 3) == 70.0

def test_ap_sum_089():
    assert ap_sum(3, 8, 2) == 80.0

def test_ap_sum_090():
    assert ap_sum(2, 6, 6) == 102.0

def test_ap_sum_091():
    assert ap_sum(3, 8, 9) == 276.0

def test_ap_sum_092():
    assert ap_sum(3, 3, 7) == 30.0

def test_ap_sum_093():
    assert ap_sum(4, 1, 5) == 4.0

def test_ap_sum_094():
    assert ap_sum(5, 3, 7) == 36.0

def test_ap_sum_095():
    assert ap_sum(4, 8, 6) == 200.0

def test_ap_sum_096():
    assert ap_sum(5, 3, 7) == 36.0

def test_ap_sum_097():
    assert ap_sum(3, 3, 8) == 33.0

def test_ap_sum_098():
    assert ap_sum(2, 2, 8) == 12.0

def test_ap_sum_099():
    assert ap_sum(4, 9, 5) == 216.0

def test_ap_sum_100():
    assert ap_sum(3, 7, 2) == 63.0

def test_ap_sum_101():
    assert ap_sum(5, 3, 3) == 24.0

def test_ap_sum_102():
    assert ap_sum(4, 8, 7) == 228.0

