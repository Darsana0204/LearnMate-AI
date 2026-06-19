import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

text = """
AI is very good and it helps many people in many things.
"""

corrected_text = tool.correct(text)

print("\n=== ORIGINAL ===\n")
print(text)

print("\n=== CORRECTED ===\n")
print(corrected_text)