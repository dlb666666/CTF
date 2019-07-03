#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

import re

repl_map = {
    "🍡": "add",
    "🤡": "clone",
    "📐": "divide",
    "😲": "if_zero",
    "😄": "if_not_zero",
    "🏀": "jump_to",
    "🚛": "load",
    "📬": "modulo",
    "⭐": "multiply",
    "🍿": "pop",
    "📤": "pop_out",
    "🎤": "print_top",
    "📥": "push",
    "🔪": "sub",
    "🌓": "xor",
    "⛰ ": "jump_top",
    "⌛": "exit",

    "0️⃣ ": "0",
    "1️⃣ ": "1",
    "2️⃣ ": "2",
    "3️⃣ ": "3",
    "4️⃣ ": "4",
    "5️⃣ ": "5",
    "6️⃣ ": "6",
    "7️⃣ ": "7",
    "8️⃣ ": "8",
    "9️⃣ ": "9",

    "🥇": "ax",
    "🥈": "bx",
    "✋": "\n",
    "😐": "\nend_if\n",

    "\n ": "\n",
}

regex_map = {
    r"(🖋[^ ]+ )": r"\g<1>\n",
    r"(pop|push) (ax|bx) ": "\g<1> \g<2>\n",
    r"(add|sub|multiply|divide|xor|clone|modulo|print_top|pop_out|if_zero|if_not_zero){1} ": r"\1\n"
}


data = ""
with open("program", "r") as prgm:
    data = prgm.read()

# Replace everything that can be mapped readily, our aim here is easy to read
# and write code. Efficiency can wait since the program being translated is
# not really large.
for symbol in repl_map.keys():
    data = str.replace(data, symbol, repl_map[symbol])

for ptrn, new_ptrn in regex_map.items():
    data = re.sub(ptrn, new_ptrn, data)

with open("decoded", "w") as f:
    f.write(data)
