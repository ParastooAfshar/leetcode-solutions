# 20. Valid Parentheses

Difficulty: Easy

https://leetcode.com/problems/valid-parentheses/

## Solution

از یک Stack استفاده می‌کنیم.

هر پرانتز باز را داخل Stack قرار می‌دهیم.
وقتی به پرانتز بسته می‌رسیم، بررسی می‌کنیم که آخرین پرانتز باز با آن مطابقت داشته باشد.

اگر در پایان Stack خالی باشد، رشته معتبر است.

Time Complexity: O(n)

Space Complexity: O(n)
