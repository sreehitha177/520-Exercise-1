#!/usr/bin/env python3
"""
Enhanced Coverage Analysis with HTML/XML Report Generation
Analyzes Solution 2 from all 4 sources for all 10 problems
Generates individual HTML/XML coverage reports for each solution
"""

import subprocess
import sys
import os
import re
import shutil
from pathlib import Path

def extract_solution_from_file(file_path, solution_number):
    """Extract a specific solution from a file"""
    
    if not os.path.exists(file_path):
        return None
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Pattern to match solution sections
    pattern = f'# Solution {solution_number}\n(.*?)(?=# Solution {solution_number + 1}|$)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        return match.group(1).strip()
    
    return None

def parse_test_cases_from_file(test_cases_file, function_name):
    """Parse test cases from test_cases.txt"""
    
    with open(test_cases_file, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    test_cases = []
    
    in_function_section = False
    for line in lines:
        line = line.strip()
        if f"Function Name: {function_name}" in line:
            in_function_section = True
            continue
        elif line.startswith("Task ID:") and in_function_section:
            break
        elif in_function_section and line.startswith("assert"):
            test_cases.append(line)
    
    return test_cases

def create_test_file_for_solution(problem_num, function_name, solution_code, test_cases, source, temp_dir):
    """Create solution and test files"""
    
    # Create solution file
    solution_filename = f"sol_{problem_num:02d}_{function_name}_{source}.py"
    solution_path = os.path.join(temp_dir, solution_filename)
    
    with open(solution_path, 'w') as f:
        f.write(f"# Problem {problem_num}: {function_name} - {source} Solution 2\n")
        f.write(solution_code)
        f.write("\n")
    
    # Create test file
    test_filename = f"test_{problem_num:02d}_{function_name}_{source}.py"
    test_path = os.path.join(temp_dir, test_filename)
    
    with open(test_path, 'w') as f:
        f.write(f"# Test file for Problem {problem_num}: {function_name} - {source}\n")
        f.write(f"import sys\n")
        f.write(f"sys.path.insert(0, '.')\n")
        f.write(f"from {solution_filename[:-3]} import {function_name}\n\n")
        
        # Add test cases
        for i, test_case in enumerate(test_cases):
            f.write(f"def test_{function_name}_{i+1:03d}():\n")
            f.write(f"    {test_case}\n\n")
    
    return solution_path, test_path

def run_coverage_analysis_with_reports(solution_file, test_file, problem_num, function_name, source, reports_dir):
    """Run coverage analysis with branch coverage and generate HTML/XML reports"""
    
    try:
        # Create subdirectory for this solution's reports
        solution_report_dir = os.path.join(reports_dir, f"p{problem_num:02d}_{function_name}_{source}")
        os.makedirs(solution_report_dir, exist_ok=True)
        
        # Run coverage with data file in solution directory
        coverage_data_file = os.path.join(solution_report_dir, ".coverage")
        
        # Get absolute path for solution file
        abs_solution_file = os.path.abspath(solution_file)
        
        cmd1 = [
            sys.executable, "-m", "coverage", "run",
            "--branch",
            "--data-file", coverage_data_file,
            "--include", abs_solution_file,
            "-m", "pytest", test_file, "-v", "--tb=no"
        ]
        
        result1 = subprocess.run(cmd1, capture_output=True, text=True, timeout=30)
        
        # Generate text report
        cmd2 = [
            sys.executable, "-m", "coverage", "report",
            "--data-file", coverage_data_file,
            "--show-missing",
            "--include", abs_solution_file
        ]
        
        result2 = subprocess.run(cmd2, capture_output=True, text=True, timeout=10)
        
        # Generate HTML report
        html_dir = os.path.join(solution_report_dir, "htmlcov")
        cmd3 = [
            sys.executable, "-m", "coverage", "html",
            "--data-file", coverage_data_file,
            "--directory", html_dir,
            "--title", f"Coverage: Problem {problem_num} - {function_name} ({source})"
        ]
        
        subprocess.run(cmd3, capture_output=True, text=True, timeout=10)
        
        # Generate XML report
        xml_file = os.path.join(solution_report_dir, "coverage.xml")
        cmd4 = [
            sys.executable, "-m", "coverage", "xml",
            "--data-file", coverage_data_file,
            "-o", xml_file
        ]
        
        subprocess.run(cmd4, capture_output=True, text=True, timeout=10)
        
        return {
            'test_output': result1.stdout,
            'coverage_output': result2.stdout,
            'html_report': html_dir,
            'xml_report': xml_file,
            'success': True
        }
        
    except subprocess.TimeoutExpired:
        return {'success': False, 'error': 'Timeout'}
    except Exception as e:
        return {'success': False, 'error': str(e)}

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

def analyze_all_40_solutions():
    """Main analysis function for all 40 solutions with report generation"""
    
    # Problem definitions
    problems = [
        (1, "odd_Num_Sum", "problem_01_odd_Num_Sum.py"),
        (2, "cal_electbill", "problem_02_cal_electbill.py"),
        (3, "check", "problem_03_check.py"),
        (4, "count_variable", "problem_04_count_variable.py"),
        (5, "find_tuples", "problem_05_find_tuples.py"),
        (6, "ap_sum", "problem_06_ap_sum.py"),
        (7, "extract_elements", "problem_07_extract_elements.py"),
        (8, "lcopy", "problem_08_lcopy.py"),
        (9, "largest_pos", "problem_09_largest_pos.py"),
        (10, "min_sum_path", "problem_10_min_sum_path.py")
    ]
    
    sources = [
        ("chatgpt_cot", "ChatGPT CoT"),
        ("chatgpt_self_planning", "ChatGPT Self-Planning"),
        ("gemini_cot", "Gemini CoT"),
        ("gemini_self_planning", "Gemini Self-Planning")
    ]
    
    # Create directories
    temp_dir = "temp_analysis_40"
    reports_dir = "coverage_reports"
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)
    
    # Read test cases
    test_cases_file = "data/test_cases/test_cases.txt"
    
    results = []
    total = len(problems) * len(sources)
    current = 0
    
    print("COMPREHENSIVE COVERAGE ANALYSIS WITH REPORT GENERATION")
    print("=" * 90)
    print(f"Analyzing {total} solutions (10 problems × 4 sources)")
    print(f"Reports will be saved to: {reports_dir}/")
    print()
    
    for problem_num, function_name, filename in problems:
        # print(f"\n{'='*90}")
        # print(f"Problem {problem_num}: {function_name}")
        # print(f"{'='*90}")
        
        # Parse test cases
        test_cases = parse_test_cases_from_file(test_cases_file, function_name)
        
        if not test_cases:
            print(f" No test cases found for {function_name}")
            continue
        
        # print(f"Found {len(test_cases)} test cases")
        
        for source_dir, source_name in sources:
            current += 1
            # print(f"\n[{current}/{total}] {source_name}...", end=" ", flush=True)
            
            # Get solution file
            solution_file_path = f"generated_code/{source_dir}/{filename}"
            
            if not os.path.exists(solution_file_path):
                print(f"File not found")
                results.append({
                    "problem": problem_num,
                    "function": function_name,
                    "source": source_name,
                    "tests_passed": 0,
                    "tests_total": len(test_cases),
                    "line_coverage": "N/A",
                    "branch_coverage": "N/A",
                    "html_report": None,
                    "xml_report": None,
                    "notes": "Solution file not found"
                })
                continue
            
            # Extract Solution 2
            solution_code = extract_solution_from_file(solution_file_path, 2)
            
            if not solution_code:
                print(f"Solution 2 not found")
                results.append({
                    "problem": problem_num,
                    "function": function_name,
                    "source": source_name,
                    "tests_passed": 0,
                    "tests_total": len(test_cases),
                    "line_coverage": "N/A",
                    "branch_coverage": "N/A",
                    "html_report": None,
                    "xml_report": None,
                    "notes": "Solution 2 not in file"
                })
                continue
            
            # Create test files
            sol_path, test_path = create_test_file_for_solution(
                problem_num, function_name, solution_code, test_cases, source_dir, temp_dir
            )
            
            # Run coverage with report generation
            coverage_result = run_coverage_analysis_with_reports(
                sol_path, test_path, problem_num, function_name, source_dir, reports_dir
            )
            
            if not coverage_result.get('success', True):
                print(f"Error: {coverage_result.get('error', 'Unknown')}")
                results.append({
                    "problem": problem_num,
                    "function": function_name,
                    "source": source_name,
                    "tests_passed": 0,
                    "tests_total": len(test_cases),
                    "line_coverage": "N/A",
                    "branch_coverage": "N/A",
                    "html_report": None,
                    "xml_report": None,
                    "notes": f"Error: {coverage_result.get('error', 'Unknown')}"
                })
                continue
            
            # Parse results
            coverage_data = parse_coverage_output(coverage_result['coverage_output'])
            test_data = parse_test_output(coverage_result['test_output'])
            
            # Determine notes
            if test_data['tests_passed'] == test_data['tests_total']:
                notes = "All tests pass"
            elif test_data['tests_passed'] == 0:
                notes = "All tests fail"
            else:
                notes = f"{test_data['tests_failed']} tests fail"
            
            result = {
                "problem": problem_num,
                "function": function_name,
                "source": source_name,
                "tests_passed": test_data['tests_passed'],
                "tests_total": test_data['tests_total'],
                "line_coverage": coverage_data['line_coverage'],
                "branch_coverage": coverage_data['branch_coverage'],
                "lines_covered": coverage_data['lines_covered'],
                "lines_total": coverage_data['lines_total'],
                "branches_covered": coverage_data['branches_covered'],
                "branches_total": coverage_data['branches_total'],
                "html_report": coverage_result.get('html_report'),
                "xml_report": coverage_result.get('xml_report'),
                "notes": notes
            }
            
            results.append(result)
            
            # print(f"✅ {test_data['tests_passed']}/{test_data['tests_total']} tests, "
                #   f"{coverage_data['line_coverage']} line, {coverage_data['branch_coverage']} branch")
    
    return results

def print_comprehensive_table(results):
    """Print comprehensive table for all 40 solutions"""
    
    print(f"\n{'='*140}")
    print("COMPREHENSIVE BASELINE COVERAGE TABLE - ALL 40 SOLUTIONS")
    print(f"{'='*140}")
    print(f"{'Problem':<8} {'Function':<15} {'Source':<25} {'Tests':<12} {'Line %':<10} {'Branch %':<12} {'Notes'}")
    print(f"{'-'*140}")
    
    current_problem = 0
    for result in results:
        # Add separator between problems
        if result['problem'] != current_problem:
            if current_problem > 0:
                print(f"{'-'*140}")
            current_problem = result['problem']
        
        problem_col = f"P{result['problem']}"
        function_col = result['function']
        source_col = result['source']
        tests_col = f"{result['tests_passed']}/{result['tests_total']}"
        line_col = result['line_coverage']
        branch_col = result['branch_coverage']
        notes_col = result['notes']
        
        print(f"{problem_col:<8} {function_col:<15} {source_col:<25} {tests_col:<12} {line_col:<10} {branch_col:<12} {notes_col}")

def generate_summary_statistics(results):
    """Generate summary statistics"""
    
    print(f"\n{'='*90}")
    print("SUMMARY STATISTICS")
    print(f"{'='*90}")
    
    # Filter out errors
    valid_results = [r for r in results if r['line_coverage'] != 'N/A']
    
    print(f"Total solutions analyzed: {len(results)}")
    print(f"Successful analyses: {len(valid_results)}")
    print(f"Failed analyses: {len(results) - len(valid_results)}")
    print()
    
    # By source statistics
    print("PERFORMANCE BY SOURCE:")
    print("-" * 50)
    
    sources = ["ChatGPT CoT", "ChatGPT Self-Planning", "Gemini CoT", "Gemini Self-Planning"]
    
    for source in sources:
        source_results = [r for r in valid_results if r['source'] == source]
        
        if not source_results:
            continue
        
        # Calculate averages
        avg_line = sum(float(r['line_coverage'].rstrip('%')) for r in source_results) / len(source_results)
        
        # Count branch coverage (excluding "No branches")
        branch_results = [r for r in source_results if r['branch_coverage'] not in ['N/A', 'No branches']]
        if branch_results:
            avg_branch = sum(float(r['branch_coverage'].rstrip('%')) for r in branch_results) / len(branch_results)
        else:
            avg_branch = 0
        
        # Count perfect solutions
        perfect = len([r for r in source_results if r['tests_passed'] == r['tests_total']])
        
        # Count 100% coverage
        full_line_cov = len([r for r in source_results if r['line_coverage'] == '100%'])
        full_branch_cov = len([r for r in branch_results if r['branch_coverage'] == '100%'])
        
        print(f"{source:<25} Avg Line: {avg_line:5.1f}%  Avg Branch: {avg_branch:5.1f}%  "
              f"Perfect: {perfect}/10  100% Line: {full_line_cov}/10  100% Branch: {full_branch_cov}/{len(branch_results)}")
    
    print()
    
    # By problem statistics
    print("PERFORMANCE BY PROBLEM:")
    print("-" * 50)
    
    for problem_num in range(1, 11):
        problem_results = [r for r in valid_results if r['problem'] == problem_num]
        
        if not problem_results:
            continue
        
        function_name = problem_results[0]['function']
        perfect = len([r for r in problem_results if r['tests_passed'] == r['tests_total']])
        avg_line = sum(float(r['line_coverage'].rstrip('%')) for r in problem_results) / len(problem_results)
        
        print(f"P{problem_num:<2} {function_name:<15} Perfect: {perfect}/4  Avg Line: {avg_line:5.1f}%")

def save_to_csv(results):
    """Save results to CSV file with report paths"""
    
    import csv
    
    filename = 'part1_all_40_solutions_with_reports.csv'
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'Problem', 'Function', 'Source', 'Solution#',
            'Tests Passed', 'Tests Total', 'Pass Rate %',
            'Line Coverage %', 'Branch Coverage %',
            'Lines Covered', 'Lines Total',
            'Branches Covered', 'Branches Total',
            'HTML Report', 'XML Report',
            'Notes'
        ])
        
        # Data
        for r in results:
            pass_rate = (r['tests_passed'] / r['tests_total'] * 100) if r['tests_total'] > 0 else 0
            
            writer.writerow([
                r['problem'],
                r['function'],
                r['source'],
                2,  # Solution number
                r['tests_passed'],
                r['tests_total'],
                f"{pass_rate:.1f}",
                r['line_coverage'],
                r['branch_coverage'],
                r.get('lines_covered', 0),
                r.get('lines_total', 0),
                r.get('branches_covered', 0),
                r.get('branches_total', 0),
                r.get('html_report', ''),
                r.get('xml_report', ''),
                r['notes']
            ])
    
    print(f"\n✅ Results saved to: {filename}")

def generate_index_html(results, reports_dir):
    """Generate an index.html file to navigate all coverage reports"""
    
    index_path = os.path.join(reports_dir, "index.html")
    
    with open(index_path, 'w') as f:
        f.write("""<!DOCTYPE html>
<html>
<head>
    <title>Coverage Reports - All 40 Solutions</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 100%; background: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #4CAF50; color: white; position: sticky; top: 0; }
        tr:hover { background-color: #f5f5f5; }
        .problem-header { background-color: #e8f5e9; font-weight: bold; }
        .pass { color: green; }
        .fail { color: red; }
        .partial { color: orange; }
        a { color: #1976D2; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .coverage-high { background-color: #c8e6c9; }
        .coverage-medium { background-color: #fff9c4; }
        .coverage-low { background-color: #ffcdd2; }
    </style>
</head>
<body>
    <h1>Coverage Reports - All 40 Solutions</h1>
    
    <table>
        <thead>
            <tr>
                <th>Problem</th>
                <th>Function</th>
                <th>Source</th>
                <th>Tests</th>
                <th>Line Coverage</th>
                <th>Branch Coverage</th>
                <th>HTML Report</th>
                <th>XML Report</th>
                <th>Notes</th>
            </tr>
        </thead>
        <tbody>
""")
        
        current_problem = 0
        for r in results:
            # Add problem separator
            if r['problem'] != current_problem:
                if current_problem > 0:
                    f.write('            <tr class="problem-header"><td colspan="9"></td></tr>\n')
                current_problem = r['problem']
            
            # Determine test status class
            if r['tests_passed'] == r['tests_total']:
                test_class = 'pass'
            elif r['tests_passed'] == 0:
                test_class = 'fail'
            else:
                test_class = 'partial'
            
            # Determine coverage class
            if r['line_coverage'] != 'N/A':
                line_pct = float(r['line_coverage'].rstrip('%'))
                if line_pct >= 90:
                    cov_class = 'coverage-high'
                elif line_pct >= 70:
                    cov_class = 'coverage-medium'
                else:
                    cov_class = 'coverage-low'
            else:
                cov_class = ''
            
            # HTML report link
            if r.get('html_report'):
                html_link = f'<a href="{os.path.relpath(r["html_report"], reports_dir)}/index.html">View HTML</a>'
            else:
                html_link = 'N/A'
            
            # XML report link
            if r.get('xml_report'):
                xml_link = f'<a href="{os.path.relpath(r["xml_report"], reports_dir)}">Download XML</a>'
            else:
                xml_link = 'N/A'
            
            f.write(f"""            <tr class="{cov_class}">
                <td>P{r['problem']}</td>
                <td>{r['function']}</td>
                <td>{r['source']}</td>
                <td class="{test_class}">{r['tests_passed']}/{r['tests_total']}</td>
                <td>{r['line_coverage']}</td>
                <td>{r['branch_coverage']}</td>
                <td>{html_link}</td>
                <td>{xml_link}</td>
                <td>{r['notes']}</td>
            </tr>
""")
        
        f.write("""        </tbody>
    </table>
</body>
</html>
""")
    
    print(f"\nIndex page created: {index_path}")
    print(f"   Open in browser: file://{os.path.abspath(index_path)}")

def main():
    """Main function"""
    
        
    # Run analysis
    results = analyze_all_40_solutions()
    
    # Print table
    print_comprehensive_table(results)
    
    # Print statistics
    generate_summary_statistics(results)
    
    # Save to CSV
    save_to_csv(results)
    
    # Generate index HTML
    generate_index_html(results, "coverage_reports")
    
    print(f"\n{'='*90}")
    print("ANALYSIS COMPLETE!")
    print(f"{'='*90}")
    print(f"Total solutions analyzed: {len(results)}")
    print(f"Results saved to: part1_all_40_solutions_with_reports.csv")
    print(f"Coverage reports: coverage_reports/")
    print(f"Index page: coverage_reports/index.html")

if __name__ == "__main__":
    main()
