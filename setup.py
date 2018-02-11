import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name='JOKENPO',
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['pedra.png', 'papel.png', 'tesoura.png','song.mp3']}},
    executables = executables

    )
