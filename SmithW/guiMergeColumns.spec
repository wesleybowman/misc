# -*- mode: python -*-
a = Analysis(['guiMergeColumns.py'],
             pathex=['/home/wesley/github/misc/SmithW'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'guiMergeColumns'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
