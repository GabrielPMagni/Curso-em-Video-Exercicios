from math import radians, sin, cos, tan
ang = float(input('\033[4;30mInsira um ângulo:\033[m '))
seno = sin(radians(ang))
print('O ângulo de \033[4;30m{}\033[m tem o \033[4;35mSENO\033[m: \033[31m{:.3f}\033[m.'.format(ang, seno))
cosen = cos(radians(ang))
print('O ângulo de \033[4;30m{}\033[m tem o \033[4;35mCOSSENO\033[m: \033[31m{:.3f}\033[m.'.format(ang, cosen))
tang = tan(radians(ang))
print('O ângulo de \033[4;30m{}\033[m tem a \033[4;35mTANGENTE\033[m: \033[31m{:.3f}\033[m'.format(ang, tang))
