# 1. Two Sum

Difficulty: Easy

https://leetcode.com/problems/two-sum/

## Solution

برای هر عدد بررسی می‌کنیم که عدد مکملش برای رسیدن به `target` قبلاً دیده شده یا نه.

اعداد قبلی را داخل یک دیکشنری ذخیره می‌کنیم.
اگر مکمل عدد فعلی داخل دیکشنری باشد، اندیس هر دو عدد را برمی‌گردانیم.

Time Complexity: O(n)

Space Complexity: O(n)