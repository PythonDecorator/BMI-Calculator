# -*- mode: python -*-
a = Analysis(['main.py'],
         pathex=['C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Bmi App'],
         hiddenimports=[],
         hookspath=None,
         runtime_hooks=None)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [("files\\images\\logo\\Logo_ico.ico",'C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Bmi App\\files\\images\\logo\Logo_ico.ico', 'DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      name='Bmi-Calculator.exe',
      debug=False,
      strip=None,
      upx=True,
      console=False,
      icon='C:\\Users\\XPS\\Desktop\\Pro Portfolio\\Bmi App\\files\\images\\logo\Logo_ico.ico')