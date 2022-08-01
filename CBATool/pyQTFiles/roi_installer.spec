# -*- mode: python ; coding: utf-8 -*-


block_cipher = Nones


a = Analysis(['<file taht kicks off your widget>.py'],
             pathex=['<path you are looking at ???>'],
             binaries=[],
             # format: (path of your file, folder that file will go in)
             # leave qt.conf the way it is
             datas=[('qt.conf', '.'),('<path to your db>', './<your db name./')]
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='ROI Tool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ROI_files')
