#!/usr/bin/env python3
"""
Exercise 3: Specification-Guided Test Improvement
Explores how formal specifications can guide test improvement for weak coverage areas.

Selected Problems:
1. Problem 4 (count_variable) - Gemini CoT: 25% line coverage, 100% branch coverage
2. Problem 8 (lcopy) - Gemini CoT: 33% line coverage, 75% branch coverage
"""

import subprocess
import sys
import os
from pathlib import Path

# ============================================================================
# PART 1: PROBLEM DEFINITIONS AND SPECIFICATIONS
# ============================================================================

PROBLEM_4_DESC = """
Problem: count_variable
Task ID: 810
Description: Write a function to iterate over elements repeating each as many times as its count.

Method signature: def count_variable(data)

Input: data - a list of elements (can be integers, strings, or mixed types)
Output: a list where each unique element from the input appears as many times as it occurred in the input

Examples:
- count_variable([4,2,0,-2]) should return ['p', 'p', 'p', 'p', 'q', 'q'] (based on test cases)
- count_variable([1, 2, 3]) should return [1, 2, 3] (each appears once)
- count_variable(['p', 'q', 'p']) should return ['p', 'p', 'q'] (p appears twice)
"""

PROBLEM_8_DESC = """
Problem: lcopy
Task ID: 847
Description: Write a python function to copy a list from a singleton tuple.

Method signature: def lcopy(tup)

Input: tup - a tuple that should contain exactly one element, which should be a list
Output: a shallow copy of the list contained in the tuple, or None if input is invalid

Examples:
- lcopy(([1, 2, 3],)) should return [1, 2, 3] (a copy)
- lcopy((5,)) should return None (not a list inside)
- lcopy(([1], [2])) should return None (not a singleton tuple)
"""

# ============================================================================
# LLM PROMPTS FOR SPECIFICATION GENERATION
# ============================================================================

PROMPT_PROBLEM_4 = """
Problem description: Write a function to iterate over elements repeating each as many times as its count.

Method signature: def count_variable(data)

Input: data - a list of elements
Output: res - a list where each unique element appears as many times as it occurred in the input

Please write formal specifications as Python assertions that describe the correct behavior of this method. 
Let 'res' denote the expected return value of 'count_variable(data)'.
Do not call 'count_variable()' in your assertions.
Do not use methods with side effects such as print, file I/O, random number generation, or timing functions.
Express the relationship between 'data' and 'res' using pure logic, list operations, and counting only.

Generate approximately 5 specifications.
"""

PROMPT_PROBLEM_8 = """
Problem description: Write a python function to copy a list from a singleton tuple.

Method signature: def lcopy(tup)

Input: tup - a tuple
Output: res - a shallow copy of the list if tup is a singleton tuple containing a list, otherwise None

Please write formal specifications as Python assertions that describe the correct behavior of this method.
Let 'res' denote the expected return value of 'lcopy(tup)'.
Do not call 'lcopy()' in your assertions.
Do not use methods with side effects such as print, file I/O, random number generation, or timing functions.
Express the relationship between 'tup' and 'res' using pure logic, type checking, and list operations only.

Generate approximately 5 specifications.
"""

# ============================================================================
# GENERATED SPECIFICATIONS (to be filled in after LLM generation)
# ============================================================================

# Problem 4: count_variable specifications
SPECS_PROBLEM_4_GENERATED = [
    # These will be filled in after running the LLM
    "# Specification 1: Result should be a list",
    "assert isinstance(res, list)",
    "",
    "# Specification 2: Length of result equals length of input",
    "assert len(res) == len(data)",
    "",
    "# Specification 3: Each element in result appears in input",
    "assert all(item in data for item in res)",
    "",
    "# Specification 4: Count of each element in result equals count in input",
    "assert all(res.count(item) == data.count(item) for item in set(data))",
    "",
    "# Specification 5: Result contains only elements from input",
    "assert set(res) == set(data)",
]

# Problem 8: lcopy specifications
SPECS_PROBLEM_8_GENERATED = [
    # These will be filled in after running the LLM
    "# Specification 1: If tup is not a tuple, result is None",
    "assert (not isinstance(tup, tuple)) implies (res is None)",
    "",
    "# Specification 2: If tup length is not 1, result is None",
    "assert (isinstance(tup, tuple) and len(tup) != 1) implies (res is None)",
    "",
    "# Specification 3: If tup[0] is not a list, result is None",
    "assert (isinstance(tup, tuple) and len(tup) == 1 and not isinstance(tup[0], list)) implies (res is None)",
    "",
    "# Specification 4: If valid input, result is a list",
    "assert (isinstance(tup, tuple) and len(tup) == 1 and isinstance(tup[0], list)) implies isinstance(res, list)",
    "",
    "# Specification 5: If valid input, result equals tup[0] but is not the same object",
    "assert (isinstance(tup, tuple) and len(tup) == 1 and isinstance(tup[0], list)) implies (res == tup[0] and res is not tup[0])",
]

print("Exercise 3: Specification-Guided Test Improvement")
print("=" * 80)
print("\nThis script will guide you through:")
print("1. Generating formal specifications from problem descriptions")
print("2. Evaluating and correcting specifications")
print("3. Generating spec-guided test cases")
print("4. Comparing coverage improvements")
print("\n" + "=" * 80)
print("\nPROBLEM 1: count_variable")
print("-" * 80)
print(PROBLEM_4_DESC)
print("\nLLM Prompt:")
print(PROMPT_PROBLEM_4)
print("\n" + "=" * 80)
print("\nPROBLEM 2: lcopy")
print("-" * 80)
print(PROBLEM_8_DESC)
print("\nLLM Prompt:")
print(PROMPT_PROBLEM_8)
print("\n" + "=" * 80)
print("\nNext steps:")
print("1. Use the prompts above with an LLM to generate specifications")
print("2. Review and correct the specifications")
print("3. Run the spec-guided test generation")
print("4. Compare coverage results")
