block_cipher = None

datas = [
    ('src/jhora/data', 'jhora/data'),
    ('src/jhora/images', 'jhora/images'),
    ('src/jhora/lang', 'jhora/lang'),
]

a = Analysis(
    ['src/jhora/ui/horo_chart_tabs.py'],
    pathex=['src'],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'jhora',
        'jhora.panchanga.drik',
        'jhora.horoscope.main',
        'swisseph',
        'PyQt6',
        'PyQt6.QtWidgets',
        'PyQt6.QtCore',
        'PyQt6.QtGui',
        'geopy',
        'timezonefinder',
        'pytz',
        'dateutil',
        'dateutil.relativedelta',
        'requests',
        'astral',
        'ephem',
        'skyfield',
    ],
    runtime_hooks=['runtime_hook.py'],
    hookspath=[],
    excludes=[],
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name='PyJHora',
    debug=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe, a.binaries, a.zipfiles, a.datas,
    strip=False,
    upx=True,
    name='PyJHora',
)

app = BUNDLE(
    coll,
    name='PyJHora.app',
    bundle_identifier='com.pyjhora.app',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSHighResolutionCapable': True,
        'CFBundleShortVersionString': '4.6.0',
    },
)
EOF
