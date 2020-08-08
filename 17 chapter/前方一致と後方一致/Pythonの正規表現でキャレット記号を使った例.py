# 複数行のテキストを複数行として扱うためにre.MULTILINEフラグを第３引数に指定すること
import re


zen = """Although never is
often better than
*right* now.
If the implemetation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""


m = re.findall("^If", zen, re.MULTILINE)
print(m)
