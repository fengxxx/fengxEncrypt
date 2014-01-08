# -*- mode: python -*-
a = Analysis(['encrypt.py'],
             pathex=['K:\\fengxEncrypt\\db'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='encrypt.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='PyInstaller2.1\\App.ico')
