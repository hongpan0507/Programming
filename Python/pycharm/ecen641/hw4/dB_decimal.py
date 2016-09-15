# power dB to decimal

F = [3, 5, 2, 1]      # in dB
GA = [10, -5, 20, -1]      # in dB
for i in range(0, len(F)):
    Fi = 10**(float(F[i])/10)
    GAi = 10**(float(GA[i])/10)
#    F_total = F[0] +
    print "F" + str(i+1) + "= %.3f" % Fi
    print "GA" + str(i+1) + "= %.3f" % GAi

