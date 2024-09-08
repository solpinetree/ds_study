
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

if platform.system() == "Darwin":
    rc("font", family="Arial Unicode MS")
    print('matplotlib hangul settings done in Mac')
elif platform.system() == "Windows":
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc("font", family=font_name)
    print('matplotlib hangul settings done in Windows')
else:
    print('Unknown system..')
plt.rcParams["axes.unicode_minus"]=False
