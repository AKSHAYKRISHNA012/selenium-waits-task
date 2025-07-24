
# Selenium Task: Mouse Interactions + XPath 🖱️🔍

## ✅ Mouse Actions
Performed on [https://demoqa.com/buttons](https://demoqa.com/buttons):
- Double Click
- Right Click
- Single Click

---

## 🧠 5 Dynamic XPath Expressions

```python
# 1. Using exact text match
//button[text()='Click Me']  
# → Selects the "Click Me" button with exact text.

# 2. Starts-with for ID
//*[starts-with(@id, 'doubleClick')]
# → Selects any tag with an ID that begins with "doubleClick"

# 3. Contains in ID attribute
//button[contains(@id, 'RightClick')]
# → Selects button where the ID contains "RightClick"

# 4. Contains in visible text
//button[contains(text(), 'Click')]
# → Selects any button containing the word "Click"

# 5. Axis: following sibling of h1 (if available)
//h1/following-sibling::div
# → Selects the div element directly after an h1 element
