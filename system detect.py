import platform

if platform.system() == 'Windows':
    print('Windows')
elif platform.system() == 'Linux':
    print('Linux')
elif platform.system() == 'Darwin':
    print('macOS')