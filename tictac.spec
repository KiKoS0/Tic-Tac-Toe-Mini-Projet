
from kivy.deps import sdl2, glew

# -*- mode: python -*-

block_cipher = None


a = Analysis(['gui.py'],
             pathex=['C:\\Users\\KiKoS\\Desktop\\pyth\\Tic-Tac-Toe-Mini-Projet'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          name='tictac',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,Tree('C:\\Users\\KiKoS\\Desktop\\pyth\\Tic-Tac-Toe-Mini-Projet\\venv\\share\\sdl2\\bin'),
				Tree('C:\\Users\\KiKoS\\Desktop\\pyth\\Tic-Tac-Toe-Mini-Projet\\venv\\share\\glew\\bin'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='tictac')
