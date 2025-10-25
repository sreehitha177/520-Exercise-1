#!/usr/bin/env python3
"""
Main evaluation script for LLM Code Generation experiment
Evaluates generated solutions using pass@k metrics
"""

import pandas as pd
import numpy as np
from math import comb
import json
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

def load_problems_data():
    """Load the 10 selected problems from MBPP-ET dataset"""
    # This would normally load from the dataset, but for this example
    # we'll use the predefined problems
    problems_data = [
        {
            'task_id': 549,
            'text': 'Write a python function to find the sum of fifth power of first n odd natural numbers.',
            'entry_point': 'odd_Num_Sum',
            'test_list': ['assert odd_Num_Sum(2) == 1024', 'assert odd_Num_Sum(3) == 3368', 'assert odd_Num_Sum(4) == 7776']
        },
        {
            'task_id': 136,
            'text': 'Write a function to calculate electricity bill.',
            'entry_point': 'cal_electbill',
            'test_list': ['assert cal_electbill(100) == 500', 'assert cal_electbill(200) == 1200', 'assert cal_electbill(300) == 2100']
        },
        # Add more problems as needed...
    ]
    return problems_data

def evaluate_single_code(code_string, function_name, test_cases):
    """
    Evaluate one code sample against test cases
    Returns dict with passed, failed, and total counts
    """
    results = {'passed': 0, 'failed': 0, 'total': len(test_cases)}

    try:
        # Create execution environment
        exec_globals = {}
        exec(code_string, exec_globals)
        user_function = exec_globals.get(function_name)

        if not user_function:
            results['failed'] = len(test_cases)
            return results

        # Test each case
        for test_case in test_cases:
            try:
                # Create safe namespace for test execution
                namespace = {function_name: user_function, '__builtins__': {}}
                
                # Custom assert function
                def custom_assert(condition, message=None):
                    if not condition:
                        raise AssertionError(message or "Assertion failed")
                namespace['assert'] = custom_assert

                # Execute test case
                exec(test_case, namespace)
                results['passed'] += 1
            except (AssertionError, Exception):
                results['failed'] += 1

    except Exception:
        # Code compilation/execution failed
        results['failed'] = len(test_cases)

    return results

def calculate_pass_at_k(code_results_list, k=1):
    """
    Calculate pass@k metric
    pass@k = 1 - (C(n-c, k) / C(n, k))
    where n = total solutions, c = correct solutions
    """
    if len(code_results_list) < k:
        return 0.0

    n = len(code_results_list)
    c = sum(1 for result in code_results_list if result['passed'] == result['total'])

    if n - c < k:
        return 1.0

    try:
        pass_at_k = 1.0 - comb(n - c, k) / comb(n, k)
        return max(0.0, min(1.0, pass_at_k))  # Clamp to [0, 1]
    except (ValueError, ZeroDivisionError):
        return 0.0

def load_generated_solutions():
    """Load all generated solutions from files"""
    solutions = {
        'chatgpt_cot': {},
        'chatgpt_self_planning': {},
        'gemini_cot': {},
        'gemini_self_planning': {}
    }
    
    # This would load from actual solution files
    # For now, return empty dict as placeholder
    return solutions

def evaluate_all_solutions():
    """Main evaluation function"""
    print("Loading problems data...")
    problems_data = load_problems_data()
    
    print("Loading generated solutions...")
    solutions = load_generated_solutions()
    
    print("Starting evaluation...")
    
    all_results = []
    
    for problem in problems_data:
        problem_id = problem['task_id']
        function_name = problem['entry_point']
        test_cases = problem['test_list']
        
        print(f"\nEvaluating Problem {problem_id}: {function_name}")
        
        # Evaluate each model/strategy combination
        for model_strategy, problem_solutions in solutions.items():
            if function_name in problem_solutions:
                model, strategy = model_strategy.split('_', 1)
                
                # Evaluate all solutions for this problem/model/strategy
                solution_results = []
                for i, solution_code in enumerate(problem_solutions[function_name]):
                    result = evaluate_single_code(solution_code, function_name, test_cases)
                    solution_results.append(result)
                    print(f"  {model} {strategy} Solution {i+1}: {result['passed']}/{result['total']} tests passed")
                
                # Calculate pass@k metrics
                pass_at_1 = calculate_pass_at_k(solution_results, k=1)
                pass_at_3 = calculate_pass_at_k(solution_results, k=3)
                pass_at_5 = calculate_pass_at_k(solution_results, k=5)
                
                result_entry = {
                    'problem_id': problem_id,
                    'function_name': function_name,
                    'model': model,
                    'strategy': strategy,
                    'pass@1': pass_at_1,
                    'pass@3': pass_at_3,
                    'pass@5': pass_at_5,
                    'solutions_tested': len(solution_results),
                    'individual_results': solution_results
                }
                
                all_results.append(result_entry)
                print(f"  Results: pass@1={pass_at_1:.2f}, pass@3={pass_at_3:.2f}, pass@5={pass_at_5:.2f}")
    
    return all_results

def generate_summary_report(results):
    """Generate summary report from evaluation results"""
    if not results:
        print("No results to summarize")
        return
    
    print("\n" + "="*80)
    print("EVALUATION SUMMARY")
    print("="*80)
    
    # Create summary table
    df = pd.DataFrame(results)
    
    # Group by model and strategy
    summary = df.groupby(['model', 'strategy']).agg({
        'pass@1': 'mean',
        'pass@3': 'mean',
        'pass@5': 'mean',
        'solutions_tested': 'sum'
    }).round(3)
    
    print("\nAverage Performance by Model and Strategy:")
    print(summary)
    
    # Save detailed results
    results_file = 'evaluation/results/detailed_results.json'
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nDetailed results saved to: {results_file}")
    
    # Save summary CSV
    summary_file = 'evaluation/results/summary_results.csv'
    df.to_csv(summary_file, index=False)
    print(f"Summary CSV saved to: {summary_file}")

def main():
    """Main execution function"""
    print("LLM Code Generation Evaluation Script")
    print("="*50)
    
    try:
        # Run evaluation
        results = evaluate_all_solutions()
        
        # Generate summary
        generate_summary_report(results)
        
        print("\nEvaluation completed successfully!")
        
    except Exception as e:
        print(f"Error during evaluation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()