#!/usr/bin/env python3
"""
Exercise 3 Coverage Analysis with HTML/XML Report Generation
Analyzes baseline and improved test suites for max_difference and large_product
Generates individual HTML/XML coverage reports for each test suite
"""

import subprocess
import sys
import os
import json
import tempfile
from pathlib import Path

def run_coverage_analysis_with_reports(problem_file, test_cases_file, report_name, reports_dir):
    """Run coverage analysis with branch coverage and generate HTML/XML reports"""
    
    problem_name = Path(problem_file).stem
    
    # Read test cases from JSON
    with open(test_cases_file, 'r') as f:
        test_cases = json.load(f)
    
    # Create subdirectory for this report
    solution_report_dir = os.path.join(reports_dir, f"{problem_name}_{report_name}")
    os.makedirs(solution_report_dir, exist_ok=True)
    
    # Create temporary test file (EXACT same as part2_coverage_analyzer)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(f"import sys\n")
        f.write(f"sys.path.insert(0, '.')\n")
        f.write(f"from {problem_name} import {problem_name}\n\n")
        
        for i, test_case in enumerate(test_cases):
            if not test_case.startswith('assert '):
                assertion = 'assert ' + test_case
            else:
                assertion = test_case
            
            f.write(f"def test_{problem_name}_{i+1}():\n")
            f.write(f"    {assertion}\n\n")
        
        temp_test_file = f.name
    
    try:
        # Run pytest with coverage using python3 (EXACT same as part2_coverage_analyzer)
        result = subprocess.run([
            'python3', '-m', 'pytest', temp_test_file,
            f'--cov={problem_name}', '--cov-report=term', '--cov-branch', 
            '-q',  # Use quiet mode for cleaner output
            '-v'   # Verbose to see individual tests
        ], capture_output=True, text=True, timeout=60)
        
        output = result.stdout + result.stderr
        
        # Extract test results (EXACT same as part2_coverage_analyzer)
        import re
        passed_match = re.search(r'(\d+) passed', output)
        failed_match = re.search(r'(\d+) failed', output)
        
        tests_passed = int(passed_match.group(1)) if passed_match else 0
        tests_failed = int(failed_match.group(1)) if failed_match else 0
        
        # Extract coverage data (EXACT same as part2_coverage_analyzer)
        line_coverage = 0
        line_coverage_fraction = '0/0'
        branch_coverage = 0
        branch_coverage_fraction = '0/0'
        
        lines = output.split('\n')
        for line in lines:
            # Look for the coverage line with the module name
            if f'{problem_name}.py' in line and 'TOTAL' not in line:
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
        
        # Now generate HTML/XML reports using coverage module
        coverage_data_file = os.path.join(solution_report_dir, ".coverage")
        abs_problem_file = os.path.abspath(problem_file)
        
        # Run coverage to generate data file
        subprocess.run([
            sys.executable, "-m", "coverage", "run",
            "--branch",
            "--data-file", coverage_data_file,
            "--source", str(Path(problem_file).parent),
            "--include", abs_problem_file,
            "-m", "pytest", temp_test_file, "-v", "--tb=no", "-q"
        ], capture_output=True, text=True, timeout=30)
        
        # Generate HTML report
        html_dir = os.path.join(solution_report_dir, "htmlcov")
        subprocess.run([
            sys.executable, "-m", "coverage", "html",
            "--data-file", coverage_data_file,
            "--directory", html_dir,
            "--title", f"Coverage: {problem_name} - {report_name}"
        ], capture_output=True, text=True, timeout=10)
        
        # Generate XML report
        xml_file = os.path.join(solution_report_dir, "coverage.xml")
        subprocess.run([
            sys.executable, "-m", "coverage", "xml",
            "--data-file", coverage_data_file,
            "-o", xml_file
        ], capture_output=True, text=True, timeout=10)
        
        return {
            'test_output': output,
            'coverage_output': output,
            'html_report': html_dir,
            'xml_report': xml_file,
            'success': True,
            'tests_passed': tests_passed,
            'tests_failed': tests_failed,
            'tests_total': tests_passed + tests_failed,
            'line_coverage': f"{line_coverage}%",
            'branch_coverage': f"{branch_coverage}%" if branch_coverage < 100 or branches > 0 else "No branches",
            'lines_covered': int(line_coverage_fraction.split('/')[0]) if '/' in line_coverage_fraction else 0,
            'lines_total': int(line_coverage_fraction.split('/')[1]) if '/' in line_coverage_fraction else 0,
            'branches_covered': int(branch_coverage_fraction.split('/')[0]) if '/' in branch_coverage_fraction and branch_coverage_fraction != '0/0' else 0,
            'branches_total': int(branch_coverage_fraction.split('/')[1]) if '/' in branch_coverage_fraction and branch_coverage_fraction != '0/0' else 0
        }
        
    except subprocess.TimeoutExpired:
        return {'success': False, 'error': 'Timeout'}
    except Exception as e:
        return {'success': False, 'error': str(e)}
    finally:
        try:
            os.unlink(temp_test_file)
        except:
            pass

def parse_coverage_output(coverage_output):
    """Parse coverage output to extract metrics"""
    
    lines = coverage_output.split('\n')
    
    for line in lines:
        if '.py' in line and 'TOTAL' not in line:
            parts = line.split()
            if len(parts) >= 6:
                try:
                    stmts_total = int(parts[1])
                    stmts_missed = int(parts[2])
                    branch_total = int(parts[3]) if parts[3].isdigit() else 0
                    branch_missed = int(parts[4]) if parts[4].isdigit() else 0
                    line_coverage_pct = parts[5]
                    
                    stmts_covered = stmts_total - stmts_missed
                    branches_covered = branch_total - branch_missed
                    
                    if branch_total > 0:
                        branch_coverage_pct = f"{(branches_covered / branch_total * 100):.0f}%"
                    else:
                        branch_coverage_pct = "No branches"
                    
                    return {
                        "line_coverage": line_coverage_pct,
                        "branch_coverage": branch_coverage_pct,
                        "lines_covered": stmts_covered,
                        "lines_total": stmts_total,
                        "branches_covered": branches_covered,
                        "branches_total": branch_total
                    }
                except (ValueError, IndexError):
                    continue
    
    return {
        "line_coverage": "0%",
        "branch_coverage": "N/A",
        "lines_covered": 0,
        "lines_total": 0,
        "branches_covered": 0,
        "branches_total": 0
    }

def parse_test_output(test_output):
    """Parse test output to count passed/failed"""
    
    passed = test_output.count(" PASSED")
    failed = test_output.count(" FAILED")
    
    return {
        "tests_passed": passed,
        "tests_failed": failed,
        "tests_total": passed + failed
    }

def analyze_problem(problem_file, baseline_tests, improved_tests, reports_dir):
    """Analyze both baseline and improved test suites for a problem"""
    
    problem_name = Path(problem_file).stem
    
    print(f"\n{'='*90}")
    print(f"Problem: {problem_name}")
    print(f"{'='*90}")
    
    # Analyze baseline
    print(f"\n[1/2] Analyzing baseline tests...")
    baseline_result = run_coverage_analysis_with_reports(
        problem_file, baseline_tests, "baseline", reports_dir
    )
    
    if not baseline_result.get('success', True):
        print(f"❌ Error: {baseline_result.get('error', 'Unknown')}")
        baseline_data = None
    else:
        baseline_data = baseline_result
        print(f"✅ Baseline: {baseline_data['tests_passed']}/{baseline_data['tests_total']} tests, "
              f"{baseline_data['line_coverage']} line, {baseline_data['branch_coverage']} branch")
    
    # Analyze improved
    print(f"\n[2/2] Analyzing improved tests...")
    improved_result = run_coverage_analysis_with_reports(
        problem_file, improved_tests, "improved", reports_dir
    )
    
    if not improved_result.get('success', True):
        print(f"❌ Error: {improved_result.get('error', 'Unknown')}")
        improved_data = None
    else:
        improved_data = improved_result
        print(f"✅ Improved: {improved_data['tests_passed']}/{improved_data['tests_total']} tests, "
              f"{improved_data['line_coverage']} line, {improved_data['branch_coverage']} branch")
    
    return {
        'problem': problem_name,
        'baseline': baseline_data,
        'improved': improved_data
    }

def print_comparison_table(results):
    """Print comparison table for all problems"""
    
    print(f"\n{'='*90}")
    print("COVERAGE COMPARISON TABLE")
    print(f"{'='*90}")
    print(f"{'Problem':<20} {'Test Suite':<12} {'Tests':<12} {'Line %':<10} {'Branch %':<12} {'HTML Report'}")
    print(f"{'-'*90}")
    
    for result in results:
        problem = result['problem']
        
        # Baseline row
        if result['baseline']:
            b = result['baseline']
            print(f"{problem:<20} {'Baseline':<12} {b['tests_passed']}/{b['tests_total']:<10} "
                  f"{b['line_coverage']:<10} {b['branch_coverage']:<12} {b['html_report']}")
        
        # Improved row
        if result['improved']:
            i = result['improved']
            print(f"{'':<20} {'Improved':<12} {i['tests_passed']}/{i['tests_total']:<10} "
                  f"{i['line_coverage']:<10} {i['branch_coverage']:<12} {i['html_report']}")
        
        # Improvement row
        if result['baseline'] and result['improved']:
            b = result['baseline']
            i = result['improved']
            line_imp = float(i['line_coverage'].rstrip('%')) - float(b['line_coverage'].rstrip('%'))
            if i['branch_coverage'] != 'No branches' and b['branch_coverage'] != 'No branches':
                branch_imp = float(i['branch_coverage'].rstrip('%')) - float(b['branch_coverage'].rstrip('%'))
                print(f"{'':<20} {'→ Improvement':<12} {'':<12} {f'+{line_imp:.0f}%':<10} {f'+{branch_imp:.0f}%':<12}")
            else:
                print(f"{'':<20} {'→ Improvement':<12} {'':<12} {f'+{line_imp:.0f}%':<10} {'N/A':<12}")
        
        print(f"{'-'*90}")

def generate_index_html(results, reports_dir):
    """Generate an index.html file to navigate all coverage reports"""
    
    index_path = os.path.join(reports_dir, "index.html")
    
    with open(index_path, 'w') as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Exercise 3 - Coverage Reports</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        h1 { color: #333; text-align: center; }
        .container { max-width: 1200px; margin: 0 auto; background: white; padding: 30px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        table { border-collapse: collapse; width: 100%; background: white; margin: 20px 0; }
        th, td { padding: 12px; text-align: left; border: 1px solid #ddd; }
        th { background-color: #4CAF50; color: white; position: sticky; top: 0; }
        tr:hover { background-color: #f5f5f5; }
        .problem-header { background-color: #e8f5e9; font-weight: bold; font-size: 1.1em; }
        .improvement { color: green; font-weight: bold; }
        a { color: #1976D2; text-decoration: none; font-weight: 500; }
        a:hover { text-decoration: underline; }
        .coverage-high { background-color: #c8e6c9; }
        .coverage-medium { background-color: #fff9c4; }
        .coverage-low { background-color: #ffcdd2; }
        .summary { background: #e3f2fd; padding: 15px; margin: 20px 0; border-left: 4px solid #2196F3; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Exercise 3 - Coverage Comparison Report</h1>
        <p style="text-align: center; color: #666;">
            Baseline vs. Specification-Guided Test Coverage
        </p>
        
        
        <table>
            <thead>
                <tr>
                    <th>Problem</th>
                    <th>Test Suite</th>
                    <th>Tests Passed</th>
                    <th>Line Coverage</th>
                    <th>Branch Coverage</th>
                    <th>Lines</th>
                    <th>Branches</th>
                    <th>Reports</th>
                </tr>
            </thead>
            <tbody>
""")
        
        for result in results:
            problem = result['problem']
            
            # Problem header
            f.write(f'            <tr class="problem-header"><td colspan="8">{problem}</td></tr>\n')
            
            # Baseline row
            if result['baseline']:
                b = result['baseline']
                line_pct = float(b['line_coverage'].rstrip('%'))
                cov_class = 'coverage-high' if line_pct >= 90 else 'coverage-medium' if line_pct >= 70 else 'coverage-low'
                
                html_link = f'<a href="{os.path.relpath(b["html_report"], reports_dir)}/index.html">HTML</a>'
                xml_link = f'<a href="{os.path.relpath(b["xml_report"], reports_dir)}">XML</a>'
                
                f.write(f'            <tr class="{cov_class}">\n')
                f.write(f'                <td></td>\n')
                f.write(f'                <td><strong>Baseline</strong></td>\n')
                f.write(f'                <td>{b["tests_passed"]}/{b["tests_total"]}</td>\n')
                f.write(f'                <td>{b["line_coverage"]}</td>\n')
                f.write(f'                <td>{b["branch_coverage"]}</td>\n')
                f.write(f'                <td>{b["lines_covered"]}/{b["lines_total"]}</td>\n')
                f.write(f'                <td>{b["branches_covered"]}/{b["branches_total"]}</td>\n')
                f.write(f'                <td>{html_link} | {xml_link}</td>\n')
                f.write(f'            </tr>\n')
            
            # Improved row
            if result['improved']:
                i = result['improved']
                line_pct = float(i['line_coverage'].rstrip('%'))
                cov_class = 'coverage-high' if line_pct >= 90 else 'coverage-medium' if line_pct >= 70 else 'coverage-low'
                
                html_link = f'<a href="{os.path.relpath(i["html_report"], reports_dir)}/index.html">HTML</a>'
                xml_link = f'<a href="{os.path.relpath(i["xml_report"], reports_dir)}">XML</a>'
                
                f.write(f'            <tr class="{cov_class}">\n')
                f.write(f'                <td></td>\n')
                f.write(f'                <td><strong>Improved</strong></td>\n')
                f.write(f'                <td>{i["tests_passed"]}/{i["tests_total"]}</td>\n')
                f.write(f'                <td>{i["line_coverage"]}</td>\n')
                f.write(f'                <td>{i["branch_coverage"]}</td>\n')
                f.write(f'                <td>{i["lines_covered"]}/{i["lines_total"]}</td>\n')
                f.write(f'                <td>{i["branches_covered"]}/{i["branches_total"]}</td>\n')
                f.write(f'                <td>{html_link} | {xml_link}</td>\n')
                f.write(f'            </tr>\n')
            
            # Improvement row
            if result['baseline'] and result['improved']:
                b = result['baseline']
                i = result['improved']
                line_imp = float(i['line_coverage'].rstrip('%')) - float(b['line_coverage'].rstrip('%'))
                lines_imp = i['lines_covered'] - b['lines_covered']
                branches_imp = i['branches_covered'] - b['branches_covered']
                
                if i['branch_coverage'] != 'No branches' and b['branch_coverage'] != 'No branches':
                    branch_imp = float(i['branch_coverage'].rstrip('%')) - float(b['branch_coverage'].rstrip('%'))
                    branch_text = f'+{branch_imp:.0f}%'
                else:
                    branch_text = 'N/A'
                
                f.write(f'            <tr style="background: #f0f0f0;">\n')
                f.write(f'                <td></td>\n')
                f.write(f'                <td><em>Improvement</em></td>\n')
                f.write(f'                <td>+{i["tests_total"] - b["tests_total"]} tests</td>\n')
                f.write(f'                <td class="improvement">+{line_imp:.0f}%</td>\n')
                f.write(f'                <td class="improvement">{branch_text}</td>\n')
                f.write(f'                <td class="improvement">+{lines_imp}</td>\n')
                f.write(f'                <td class="improvement">+{branches_imp}</td>\n')
                f.write(f'                <td></td>\n')
                f.write(f'            </tr>\n')
        
        f.write("""            </tbody>
        </table>
    </div>
</body>
</html>
""")
    
    print(f"\n✅ Index page created: {index_path}")
    print(f"   Open in browser: file://{os.path.abspath(index_path)}")

def main():
    """Main function"""
    
    print("="*90)
    print("EXERCISE 3 - COVERAGE ANALYSIS WITH HTML/XML REPORTS")
    print("="*90)
    print("\nAnalyzing baseline and improved test suites for Exercise 3 problems...")
    
    # Determine if we're running from Exercise_3 directory or project root
    if os.path.exists('max_difference.py'):
        # Running from Exercise_3 directory
        base_dir = '.'
        reports_dir = "coverage_reports"
    elif os.path.exists('Exercise_3/max_difference.py'):
        # Running from project root
        base_dir = 'Exercise_3'
        reports_dir = "Exercise_3/coverage_reports"
    else:
        print("Error: Cannot find Exercise_3 files. Please run from project root or Exercise_3 directory.")
        sys.exit(1)
    
    os.makedirs(reports_dir, exist_ok=True)
    
    results = []
    
    # Problem 1: max_difference
    result1 = analyze_problem(
        f'{base_dir}/max_difference.py',
        f'{base_dir}/baseline_tests_max_difference.json',
        f'{base_dir}/Improved_tests_max_difference.json',
        reports_dir
    )
    results.append(result1)
    
    # Problem 2: large_product
    result2 = analyze_problem(
        f'{base_dir}/large_product.py',
        f'{base_dir}/baseline_tests_large_product.json',
        f'{base_dir}/improved_tests_large_product.json',
        reports_dir
    )
    results.append(result2)
    
    # Print comparison table
    print_comparison_table(results)
    
    # Generate index HTML
    generate_index_html(results, reports_dir)
    
    print(f"\n{'='*90}")
    print("ANALYSIS COMPLETE!")
    print(f"{'='*90}")
    print(f"Coverage reports saved to: {reports_dir}/")
    print(f"Index page: {reports_dir}/index.html")
    print("\nTo view reports, open: file://{}/index.html".format(os.path.abspath(reports_dir)))

if __name__ == "__main__":
    main()
