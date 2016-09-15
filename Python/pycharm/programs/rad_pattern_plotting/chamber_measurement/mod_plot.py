from matplotlib import pyplot as plot


# data = [[frequency],[angle],[horizontal radiation[], vertical radiation[]]]
def polar_plot(fig_num, state, data=[]):
    n = 0
    for i in range(0, len(data[2][0])):
        n = i+1
        title = state + ' Normalized Radiation Pattern'
        title = title + '\n mode ' + str(n) + ';'
        title = title + ' frequency = ' + str(data[0][i]) + "MHz"
        plot.figure(fig_num+n)
        ax = plot.subplot(111, polar=True)
        ax.set_theta_zero_location('N')
        ax.set_theta_direction('clockwise')
        ax.plot(data[1], data[2][0][i], color='r', linewidth=2, label="horizontal pol")
        ax.plot(data[1], data[2][1][i], color='b', linewidth=2, label="vertical pol")
        plot.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)  # loc=4 => bottom right corner
        plot.subplots_adjust(left=0.2, right=0.7, top=0.9, bottom=0.1, hspace=0, wspace=0)
        # ax.set_rmax(1)
        # ax.set_xticks(np.array([0, -45, -90, -135, 180, 135, 90, 45])/180*pi)
        ax.set_yticks(range(-40, 0, 10))
        ax.set_title(title, y=1.1)
    return fig_num+n
