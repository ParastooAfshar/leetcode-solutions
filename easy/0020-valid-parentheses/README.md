# 20. Valid Parentheses

Difficulty: Easy

- [1. Two Sum](./easy/0001-two-sum/)
- [20. Valid Parentheses](./easy/0020-valid-parentheses/)

https://leetcode.com/problems/valid-parentheses/

## Solution

از یک Stack استفاده می‌کنیم.

هر پرانتز باز را داخل Stack قرار می‌دهیم.
وقتی به پرانتز بسته می‌رسیم، بررسی می‌کنیم که آخرین پرانتز باز با آن مطابقت داشته باشد.

اگر در پایان Stack خالی باشد، رشته معتبر است.

Time Complexity: O(n)

Space Complexity: O(n)