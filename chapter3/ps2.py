latter = 'Dear <|NAME|>,' \
'\nYou are selected!\n' \
'Date: <|DATE|>'
print(latter.replace("<|NAME|>", "Vishal")
      .replace("<|DATE|>", "9/10/2026"))