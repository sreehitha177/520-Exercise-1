#!/usr/bin/env python3
"""
Single function coverage analysis with JSON test cases
"""
import subprocess
import re
import os
import json
import sys
import tempfile

def run_coverage_for_function(script_path, test_cases_json):
    """Run coverage analysis for a specific function with JSON test cases"""
    
    # Extract function name from script path
    function_name = os.path.basename(script_path).replace('.py', '')
    
    # Create a temporary test file from JSON test cases
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        # Write the test file
        f.write(f"import sys\n")
        f.write(f"sys.path.insert(0, '.')\n")
        f.write(f"from {function_name} import {function_name}\n\n")
        
        # Parse JSON test cases and convert to test assertions
        try:
            test_cases = json.loads(test_cases_json)
            for i, test_case in enumerate(test_cases):
                # Extract the assertion part (remove "assert ")
                # if test_case.startswith('assert '):
                #     assertion = test_case[7:]  # Remove "assert "
                # else:
                #     assertion = test_case
                
                # # Create separate test function for each test case
                # f.write(f"def test_{function_name}_{i+1}():\n")
                # f.write(f"    {assertion}\n\n")
                if not test_case.startswith('assert '):
                    assertion = 'assert ' + test_case
                else:
                    assertion = test_case

                f.write(f"def test_{function_name}_{i+1}():\n")
                f.write(f"    {assertion}\n\n")

                
        except json.JSONDecodeError as e:
            return {
                'function': function_name,
                'error': f'Invalid JSON test cases: {str(e)}',
                'tests_passed': 0,
                'tests_failed': 0,
                'line_coverage': 0,
                'line_coverage_fraction': '0/0',
                'branch_coverage': 0,
                'branch_coverage_fraction': '0/0'
            }
        
        temp_test_file = f.name
    
    try:
        # Test if we can import the function using python3
        try:
            test_cmd = f"python3 -c 'from {function_name} import {function_name}; print(\"Import successful\")'"
            result = subprocess.run(test_cmd, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                return {
                    'function': function_name,
                    'error': f'Cannot import function: {result.stderr}',
                    'tests_passed': 0,
                    'tests_failed': 0,
                    'line_coverage': 0,
                    'line_coverage_fraction': '0/0',
                    'branch_coverage': 0,
                    'branch_coverage_fraction': '0/0'
                }
        except Exception as e:
            return {
                'function': function_name,
                'error': f'Import test failed: {str(e)}',
                'tests_passed': 0,
                'tests_failed': 0,
                'line_coverage': 0,
                'line_coverage_fraction': '0/0',
                'branch_coverage': 0,
                'branch_coverage_fraction': '0/0'
            }
        
        # Run pytest with coverage using python3
        result = subprocess.run([
            'python3', '-m', 'pytest', temp_test_file,
            f'--cov={function_name}', '--cov-report=term', '--cov-branch', 
            '-q',  # Use quiet mode for cleaner output
            '-v'   # Verbose to see individual tests
        ], capture_output=True, text=True, timeout=60)
        
        output = result.stdout + result.stderr
        
        # Extract test results - look for the summary line
        passed_match = re.search(r'(\d+) passed', output)
        failed_match = re.search(r'(\d+) failed', output)
        
        tests_passed = int(passed_match.group(1)) if passed_match else 0
        tests_failed = int(failed_match.group(1)) if failed_match else 0
        
        # Extract coverage data - look for the specific module line
        line_coverage = 0
        line_coverage_fraction = '0/0'
        branch_coverage = 0
        branch_coverage_fraction = '0/0'
        
        lines = output.split('\n')
        for line in lines:
            # Look for the coverage line with the module name
            if f'{function_name}.py' in line and 'TOTAL' not in line:
                parts = line.split()
                if len(parts) >= 6:
                    try:
                        stmts = int(parts[1])
                        miss = int(parts[2])
                        branches = int(parts[3])
                        brpart = int(parts[4])
                        
                        # Calculate percentages
                        line_coverage = round(((stmts - miss) / stmts) * 100) if stmts > 0 else 0
                        branch_coverage = round(((branches - brpart) / branches) * 100) if branches > 0 else 100
                        
                        # Calculate fractions
                        lines_covered = stmts - miss
                        branches_covered = branches - brpart
                        line_coverage_fraction = f"{lines_covered}/{stmts}"
                        branch_coverage_fraction = f"{branches_covered}/{branches}" if branches > 0 else "0/0"
                        break
                    except (ValueError, IndexError):
                        continue
        
        return {
            'function': function_name,
            'tests_passed': tests_passed,
            'tests_failed': tests_failed,
            'line_coverage': line_coverage,
            'line_coverage_fraction': line_coverage_fraction,
            'branch_coverage': branch_coverage,
            'branch_coverage_fraction': branch_coverage_fraction,
            'total_tests': tests_passed + tests_failed,
            'expected_tests': len(test_cases),
            'output': output
        }
        
    except subprocess.TimeoutExpired:
        return {
            'function': function_name,
            'error': 'Test execution timeout',
            'tests_passed': 0,
            'tests_failed': 0,
            'line_coverage': 0,
            'line_coverage_fraction': '0/0',
            'branch_coverage': 0,
            'branch_coverage_fraction': '0/0'
        }
    except Exception as e:
        return {
            'function': function_name,
            'error': str(e),
            'tests_passed': 0,
            'tests_failed': 0,
            'line_coverage': 0,
            'line_coverage_fraction': '0/0',
            'branch_coverage': 0,
            'branch_coverage_fraction': '0/0'
        }
    finally:
        # Clean up temporary file
        try:
            os.unlink(temp_test_file)
        except:
            pass

def main():
    """Main coverage analysis for a single function with JSON test cases"""
    
    if len(sys.argv) != 3:
        print("Usage: python3 flexible_coverage_analyzer.py <script_file> <test_cases_json_file>")
        print("Example: python3 flexible_coverage_analyzer.py max_difference.py test_cases.json")
        sys.exit(1)
    
    script_path = sys.argv[1]
    test_cases_file = sys.argv[2]
    
    # Check if script file exists
    if not os.path.exists(script_path):
        print(f"Error: Script file '{script_path}' not found")
        sys.exit(1)
    
    # Read JSON test cases
    try:
        with open(test_cases_file, 'r') as f:
            test_cases_json = f.read()
            test_cases = json.loads(test_cases_json)
    except FileNotFoundError:
        print(f"Error: Test cases file '{test_cases_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading test cases file: {str(e)}")
        sys.exit(1)
    
    print("SINGLE FUNCTION COVERAGE ANALYSIS")
    print("=" * 60)
    print(f"Script: {script_path}")
    print(f"Test cases file: {test_cases_file}")
    print(f"Total test cases in JSON: {len(test_cases)}")
    print()
    
    result = run_coverage_for_function(script_path, test_cases_json)
    
    if 'error' in result:
        print(f"ERROR: {result['error']}")
        return
    
    print(f"Tests passed: {result['tests_passed']}/{result['total_tests']} (expected: {result['expected_tests']})")
    print(f"Line coverage: {result['line_coverage']}% ({result['line_coverage_fraction']})")
    print(f"Branch coverage: {result['branch_coverage']}% ({result['branch_coverage_fraction']})")
    
    # Calculate pass rate
    if result['total_tests'] > 0:
        pass_rate = (result['tests_passed'] / result['total_tests']) * 100
        print(f"Pass rate: {pass_rate:.1f}%")
    
    # Check if all expected tests ran
    if result['total_tests'] != result['expected_tests']:
        print(f"⚠️  Warning: Only {result['total_tests']} tests ran out of {result['expected_tests']} expected")
    
    # Determine status
    if result['tests_failed'] == result['total_tests']:
        status = "All tests failing"
    elif result['tests_failed'] > 0:
        status = f"{result['tests_failed']} tests failing"
    elif result['line_coverage'] == 100 and result['branch_coverage'] == 100:
        status = "Perfect coverage"
    elif result['line_coverage'] >= 90:
        status = "Excellent coverage"
    else:
        status = "Good coverage"
    
    print(f"Status: {status}")
    
    # Show detailed output if requested
    if '--verbose' in sys.argv or '-v' in sys.argv:
        print("\n" + "=" * 60)
        print("DETAILED OUTPUT:")
        print("=" * 60)
        print(result.get('output', 'No output available'))

if __name__ == "__main__":
    main()