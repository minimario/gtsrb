import matplotlib.cm as cm
import matplotlib
from matplotlib import pyplot as plt
plt.rc('font', family='serif')

cam_496 = [1782.7732696533203, 1769.0102424621582, 1758.899917602539, 1705.661376953125, 1648.2532958984375, 1642.0797119140625, 1585.5334321260452, 1552.3820495605469, 1546.82666015625, 1533.7100620269775, 1523.9222412109375, 1517.7205810546875, 1514.792236328125, 1387.68212890625, 1385.364761352539, 1300.6678466796875, 1252.431396484375, 1186.6658935546875, 1131.3133544921875, 1109.705810546875, 1085.3541259765625, 1011.6669921875, 980.6264038085938, 978.5045776367188, 909.85498046875, 863.5337524414062, 844.6862106323242, 791.7845458984375, 788.1567993164062, 785.3888549804688, 762.3322143554688, 746.2111206054688, 701.0394916534424, 586.1155395507812, 572.683837890625, 544.9087524414062, 543.4491577148438, 476.7515869140625, 461.9095458984375, 461.8742980957031, 461.1355512291193, 369.3150634765625, 323.6983947753906, 284.8833694458008, 283.873779296875, 275.00347900390625, 266.515625, 239.33316040039062, 234.35977172851562, 218.3341064453125, 196.18600463867188, 182.0933380126953, 174.1177520751953, 173.024169921875, 170.754638671875, 143.72194290161133, 132.45811462402344, 130.7507330775261, 130.61114501953125, 115.99681854248047, 111.62247467041016, 91.3960371017456, 83.1993179321289, 76.61648559570312, 72.49004364013672, 63.048828125, 59.95899200439453, 36.92028999328613, 32.175543785095215, 20.339170455932617, 19.178054809570312, 9.92807674407959, 4.20576810836792, 1.351218581199646, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.9621086120605469, -4.5772905349731445, -12.961950302124023, -18.071704864501953, -18.252460479736328, -23.681222915649414, -24.17498207092285, -26.42424201965332, -34.08883285522461, -37.91837120056152, -41.99639129638672, -46.792423248291016, -51.6602668762207, -71.36627769470215, -86.18832397460938, -130.14471435546875]
attack_496 = {1: 0.000509033203125, 2: 0.005306396484375, 3: 0.003214111328125, 4: 0.0028076171875, 5: 0.000242919921875, 6: 0.004219970703125, 7: 0.0017993164062499998, 8: 0.000916748046875, 9: 0.0026391601562499997, 10: 0.00132080078125, 11: 0.00607666015625, 12: 0.00097412109375, 13: 0.014727783203124997, 14: 0.00016845703125, 15: 0.004770507812500001, 16: 0.001488037109375, 17: 0.005089111328124999, 18: 0.0024145507812500006, 19: 0.0010900878906250002, 20: 0.0011633300781250001, 21: 0.00794189453125, 22: 0.0022045898437500003, 23: 7.080078125000001e-05, 24: 0.0022546386718750007, 25: 0.0032507324218750003, 26: 0.001888427734375, 27: 0.0026977539062499997, 28: 0.0007165527343749999, 29: 0.00030883789062500003, 30: 0.0016455078125, 31: 0.0050390625, 32: 0.0037072753906249997, 33: 0.010347900390624998, 34: 0.0007397460937500001, 35: 0.0018774414062499999, 36: 5.2490234375000006e-05, 37: 0.00202880859375, 38: 0.0014697265625, 39: 2.44140625e-06, 40: 0.005775146484375, 41: 0.003779296875, 42: 0.0027697753906249997, 43: 0.0051733398437499994, 44: 4.7607421875e-05, 45: 0.0005712890625000001, 46: 0.00032958984374999997, 47: 0.001396484375, 48: 0.002742919921875, 49: 0.0036828613281249993, 50: 0.000772705078125}
cert_496 = {1: 0.00013769531250000001, 2: 0.00010351562500000001, 3: 0.00048046875, 4: 0.0006455078124999999, 5: 9.765625e-05, 10: 0.00016699218749999999, 13: 0.0009990234375000001, 14: 3.02734375e-05, 15: 0.0009013671874999999, 16: 0.0006210937500000001, 17: 0.0008554687500000001, 18: 0.000708984375, 20: 0.00032617187499999996, 30: 0.00043164062500000006, 50: 0.0001796875, 6: 0.000761993408203125, 7: 0.0004447021484375, 8: 0.000101715087890625, 9: 0.00021600341796875004, 11: 0.00015206909179687502, 12: 7.489013671875002e-05, 19: 0.0003583984375, 21: 0.000685302734375, 22: 0.00032226562499999996, 23: 2.6367187500000003e-05, 24: 0.0006721191406249999, 25: 0.0005458984375, 26: 0.00022680664062499998, 27: 0.0007868652343750001, 28: 9.7412109375e-05, 29: 6.4453125e-05, 31: 0.000257080078125, 32: 0.000480224609375, 33: 0.0011152343750000001, 34: 0.00022753906249999999, 35: 0.00036767578125, 36: 1.66015625e-05, 37: 0.0006845703125, 38: 0.00020166015625000002, 39: 4.8828125e-07, 40: 9.277343750000001e-06, 41: 0.00094140625, 42: 0.00066748046875, 43: 0.00042138671875000005, 44: 1.3183593750000002e-05, 45: 0.00010986328124999999, 46: 0.00013720703125, 47: 0.00042333984375000005, 48: 8.544921875e-05, 49: 0.000185546875}
k2_496 = {16: 0.0013519287109375, 17: 0.00170928955078125, 18: 0.00208984375, 20: 0.0024023437500000004, 25: 0.0034765624999999996, 30: 0.0044531250000000005, 40: 0.005185546874999999, 50: 0.0057421875, 80: 0.006181640625, 100: 0.0064062500000000005, 19: 0.002205078125, 21: 0.002630859375, 22: 0.0026660156249999995, 23: 0.003103515625, 24: 0.003189453125, 26: 0.0036113281249999995, 27: 0.0039804687500000005, 28: 0.004052734375, 29: 0.004283203125, 31: 0.004480468750000001, 32: 0.004505859375000001, 33: 0.004589843750000001, 34: 0.004593750000000001, 35: 0.004646484375000001, 36: 0.004652343750000001, 37: 0.005082031249999999, 38: 0.005113281249999999, 39: 0.005117187499999999, 41: 0.005220703124999999, 42: 0.005271484375, 43: 0.005345703124999999, 44: 0.005474609375, 45: 0.005578125, 46: 0.0055859375, 47: 0.0056171875, 48: 0.005626953125, 49: 0.0056875, 51: 0.005759765625, 52: 0.005763671875, 53: 0.005796875, 54: 0.005802734375, 55: 0.0058046875, 56: 0.00580859375, 57: 0.00583984375, 58: 0.0058476562499999996, 59: 0.005859375, 60: 0.0058867187500000005, 61: 0.005888671875, 62: 0.0059023437500000005, 63: 0.005927734375, 64: 0.005943359375, 65: 0.0059453125, 66: 0.005962890625, 67: 0.005966796875, 68: 0.005982421875, 69: 0.005990234375, 70: 0.0059960937500000006, 71: 0.006042968750000001, 72: 0.0060546875, 73: 0.0060625, 74: 0.006087890625, 75: 0.006099609375, 76: 0.00611328125, 77: 0.006142578125, 78: 0.00615625, 79: 0.006158203125, 81: 0.006189453125, 82: 0.00619140625, 83: 0.006228515625, 84: 0.0062324218750000005, 85: 0.006246093750000001, 86: 0.006255859375000001, 87: 0.00628515625, 88: 0.0063125, 89: 0.0063125, 90: 0.00631640625, 91: 0.00631640625, 92: 0.006357421875000001, 93: 0.006357421875000001, 94: 0.0063671875000000005, 95: 0.0063750000000000005, 96: 0.00637890625, 97: 0.006380859375000001, 98: 0.0064062500000000005, 99: 0.006408203125}

xs = [i for i in attack_496]
xs.sort()

attacks = [attack_496[i] for i in xs]
certs = [cert_496[i] for i in xs]

# plt.plot(xs, attacks, color='green')
# plt.plot(xs, certs, color='blue')

# K2 FIGURE

matplotlib.rcParams.update({'font.size': 24})


xs = [i for i in k2_496]
xs.sort()
fig, ax = plt.subplots()
plt.scatter(xs, [k2_496[i] for i in xs], s=40)
ax.set_ybound(0, 0.007)
ax.set_xlabel(r'$k_2$', fontsize=24)
ax.set_ylabel('Relaxed CORGI Bound', fontsize=24)
plt.title(r'Relaxed CORGI Bound vs $k_2$', fontsize=30, y=1.03)
plt.savefig('k2.pdf')
plt.show()

# CAM MAP GAP FIGURE

fig, ax = plt.subplots()
delta = [cam_496[i]-cam_496[i+1] for i in range(50)]
for i in range(50):
	if delta[i] > 100:
		print(i)

colors = []
for i in range(len(delta)):
	colors.append(i)
sc = plt.scatter(delta, certs, s=160, c=colors, cmap = cm.copper, label='CORGI bound')
sc2 = plt.scatter(delta, attacks, s=160, marker='v', c=colors, cmap = cm.winter, label='attack bound')


# divider = make_axes_locatable(ax)
# cax = divider.append_axes("right", size="5%", pad=0.05)

cbar = plt.colorbar(sc, pad=-0.1)
cbar2 = plt.colorbar(sc2)
ax.set_xbound(0, 100)
ax.set_ybound(-0.0001, 0.008)
plt.title("CORGI Bound vs CAM Gap", fontsize=30, y=1.03)
ax.set_xlabel(r'CAM Gap: $I(x)_{k+1}-I(x)_k$', fontsize=24)
ax.set_ylabel("CORGI Bound", fontsize=24)
# cbar.ax.axis('off')
cbar.ax.set_ylabel("k", rotation=0)
matplotlib.rc('xtick', labelsize=24) 
matplotlib.rc('ytick', labelsize=24) 
cbar2.ax.axis('off')
plt.legend(handles=[sc, sc2])
leg = ax.get_legend()
leg.legendHandles[0].set_color('brown')
leg.legendHandles[1].set_color('blue')
plt.savefig('camgap.pdf')
# plt.scatter(delta, attacks, color='green')
plt.show()