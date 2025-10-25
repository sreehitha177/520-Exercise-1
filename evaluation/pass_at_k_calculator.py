#!/usr/bin/env python3
"""
Pass@k metric calculation utilities
"""

from math import comb
from typing import List, Dict, Any

def calculate_pass_at_k(results: List[Dict[str, Any]], k: int = 1) -> float:
    """
    Calculate pass@k metric for code generation evaluation.
    
    pass@k estimates the probability that at least one of k generated solutions
    passes all test cases.
    
    Formula: pass@k = 1 - (C(n-c, k) / C(n, k))
    where:
    - n = total number of solutions
    - c = number of solutions that pass all tests
    - C(n, k) = binomial coefficient "n choose k"
    
    Args:
        results: List of evaluation results, each containing 'passed' and 'total' counts
        k: Number of solutions to consider (default: 1)
    
    Returns:
        float: pass@k value between 0.0 and 1.0
    """
    if not results or len(results) < k:
        return 0.0
    
    n = len(results)  # Total number of solutions
    c = sum(1 for result in results if result['passed'] == result['total'])  # Correct solutions
    
    # If we have enough correct solutions, pass@k = 1.0
    if c >= k:
        return 1.0
    
    # If we don't have enough solutions to choose k from the incorrect ones
    if n - c < k:
        return 1.0
    
    try:
        # Calculate pass@k using the standard formula
        pass_at_k = 1.0 - (comb(n - c, k) / comb(n, k))
        return max(0.0, min(1.0, pass_at_k))  # Clamp to [0, 1]
    except (ValueError, ZeroDivisionError, OverflowError):
        return 0.0

def calculate_multiple_pass_at_k(results: List[Dict[str, Any]], k_values: List[int]) -> Dict[str, float]:
    """
    Calculate pass@k for multiple k values.
    
    Args:
        results: List of evaluation results
        k_values: List of k values to calculate (e.g., [1, 3, 5])
    
    Returns:
        Dict mapping f"pass@{k}" to calculated values
    """
    return {f"pass@{k}": calculate_pass_at_k(results, k) for k in k_values}

def calculate_success_rate(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate overall success rates from evaluation results.
    
    Args:
        results: List of evaluation results
    
    Returns:
        Dict containing various success rate metrics
    """
    if not results:
        return {
            'test_success_rate': 0.0,
            'solution_success_rate': 0.0,
            'total_tests': 0,
            'total_passed': 0,
            'total_solutions': 0,
            'solutions_passed_all': 0
        }
    
    # Calculate test-level success rate
    total_tests = sum(result['total'] for result in results)
    total_passed = sum(result['passed'] for result in results)
    test_success_rate = total_passed / total_tests if total_tests > 0 else 0.0
    
    # Calculate solution-level success rate
    total_solutions = len(results)
    solutions_passed_all = sum(1 for result in results if result['passed'] == result['total'])
    solution_success_rate = solutions_passed_all / total_solutions if total_solutions > 0 else 0.0
    
    return {
        'test_success_rate': test_success_rate,
        'solution_success_rate': solution_success_rate,
        'total_tests': total_tests,
        'total_passed': total_passed,
        'total_failed': total_tests - total_passed,
        'total_solutions': total_solutions,
        'solutions_passed_all': solutions_passed_all,
        'solutions_failed_some': total_solutions - solutions_passed_all
    }

def format_pass_at_k_results(results: Dict[str, float], precision: int = 3) -> str:
    """
    Format pass@k results for display.
    
    Args:
        results: Dict of pass@k results
        precision: Number of decimal places
    
    Returns:
        Formatted string representation
    """
    formatted = []
    for metric, value in sorted(results.items()):
        formatted.append(f"{metric}={value:.{precision}f}")
    return ", ".join(formatted)

def compare_pass_at_k(results_a: List[Dict[str, Any]], 
                      results_b: List[Dict[str, Any]], 
                      k_values: List[int] = [1, 3, 5]) -> Dict[str, Dict[str, float]]:
    """
    Compare pass@k metrics between two sets of results.
    
    Args:
        results_a: First set of evaluation results
        results_b: Second set of evaluation results
        k_values: List of k values to compare
    
    Returns:
        Dict containing comparison metrics
    """
    pass_at_k_a = calculate_multiple_pass_at_k(results_a, k_values)
    pass_at_k_b = calculate_multiple_pass_at_k(results_b, k_values)
    
    comparison = {
        'results_a': pass_at_k_a,
        'results_b': pass_at_k_b,
        'difference': {k: pass_at_k_b[k] - pass_at_k_a[k] for k in pass_at_k_a.keys()},
        'improvement': {k: (pass_at_k_b[k] - pass_at_k_a[k]) / pass_at_k_a[k] * 100 
                       if pass_at_k_a[k] > 0 else float('inf') 
                       for k in pass_at_k_a.keys()}
    }
    
    return comparison

# Example usage and testing
if __name__ == "__main__":
    # Test with sample data
    sample_results = [
        {'passed': 10, 'total': 10},  # Perfect solution
        {'passed': 8, 'total': 10},   # Partial success
        {'passed': 0, 'total': 10},   # Complete failure
        {'passed': 10, 'total': 10},  # Perfect solution
        {'passed': 5, 'total': 10},   # Partial success
    ]
    
    print("Sample Results:")
    for i, result in enumerate(sample_results, 1):
        print(f"  Solution {i}: {result['passed']}/{result['total']} tests passed")
    
    print("\nPass@k Calculations:")
    for k in [1, 3, 5]:
        pass_at_k = calculate_pass_at_k(sample_results, k)
        print(f"  pass@{k} = {pass_at_k:.3f}")
    
    print("\nSuccess Rates:")
    success_rates = calculate_success_rate(sample_results)
    print(f"  Test Success Rate: {success_rates['test_success_rate']:.1%}")
    print(f"  Solution Success Rate: {success_rates['solution_success_rate']:.1%}")
    print(f"  Total Tests: {success_rates['total_tests']}")
    print(f"  Tests Passed: {success_rates['total_passed']}")
    print(f"  Solutions Passed All: {success_rates['solutions_passed_all']}/{success_rates['total_solutions']}")