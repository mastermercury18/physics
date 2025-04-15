import math
from math import log
import random
import matplotlib.pyplot as plt


data_list = []
copy_data_list = []

with open("/Users/neha/Documents/tj/ai/data_files/SDSS_quasar.csv") as f:
    counter = 0
    for line in f:
        counter += 1
        if counter == 1:
            continue
        array = line.strip().split(" ")
        tup = ()
        for element in array[2:]:
            if element != '':
                element = element.replace('"', '')
                tup += (float(element), )
        data_list.append(tup)
        copy_data_list.append(tup)

def get_error(quasar, mean):
    RA_error = (mean[0] - quasar[0]) ** 2
    dec_error = (mean[1] - quasar[1]) ** 2
    z_error = (mean[2] - quasar[2]) ** 2
    u_mag_error = (mean[3] - quasar[3]) ** 2
    sig_u_error = (mean[4] - quasar[4]) ** 2
    g_mag_error = (mean[5] - quasar[5]) ** 2
    sig_g_error = (mean[6] - quasar[6]) ** 2
    r_mag_error = (mean[7] - quasar[7]) ** 2
    sig_r_error = (mean[8] - quasar[8]) ** 2
    i_mag_error = (mean[9] - quasar[9]) ** 2
    sig_i_error = (mean[10] - quasar[10]) ** 2
    z_mag_error = (mean[11] - quasar[11]) ** 2
    sig_z_error = (mean[12] - quasar[12]) ** 2
    radio_error = (mean[13] - quasar[13]) ** 2
    x_ray_error = (mean[14] - quasar[14]) ** 2
    j_error = (mean[15] - quasar[15]) ** 2
    sig_j_error = (mean[16] - quasar[16]) ** 2
    h_error = (mean[17] - quasar[17]) ** 2
    sig_h_error = (mean[18] - quasar[18]) ** 2
    k_error = (mean[19] - quasar[19]) ** 2
    sig_k_error = (mean[20] - quasar[20]) ** 2
    m_i_error = (mean[21] - quasar[21]) ** 2
    return (RA_error + dec_error + z_error + u_mag_error + sig_u_error + g_mag_error + sig_g_error + r_mag_error + sig_r_error + i_mag_error + sig_i_error + z_mag_error + sig_z_error + radio_error + x_ray_error + j_error + sig_j_error + h_error + sig_h_error + k_error + sig_k_error + m_i_error)

def calc_average(associated_quasars, num):
    the_sum = 0
    for quasar in associated_quasars:
        the_sum += quasar[num]
    return the_sum / len(associated_quasars)

def find_actual_means(mean_and_quasars_dict):
    actual_means = []
    for mean in mean_and_quasars_dict:
        associated_quasars = mean_and_quasars_dict[mean]
        RA_avg = calc_average(associated_quasars, 0)
        dec_avg = calc_average(associated_quasars, 1)
        z_avg = calc_average(associated_quasars, 2)
        u_mag_avg = calc_average(associated_quasars, 3)
        sig_u_avg = calc_average(associated_quasars, 4)
        g_mag_avg = calc_average(associated_quasars, 5)
        sig_g_avg = calc_average(associated_quasars, 6)
        r_mag_avg = calc_average(associated_quasars, 7)
        sig_r_avg = calc_average(associated_quasars, 8)
        i_mag_avg = calc_average(associated_quasars, 9)
        sig_i_avg = calc_average(associated_quasars, 10)
        z_mag_avg = calc_average(associated_quasars, 11)
        sig_z_avg = calc_average(associated_quasars, 12)
        radio_avg = calc_average(associated_quasars, 13)
        x_ray_avg = calc_average(associated_quasars, 14)
        j_avg = calc_average(associated_quasars, 15)
        sig_j_avg = calc_average(associated_quasars, 16)
        h_avg = calc_average(associated_quasars, 17)
        sig_h_avg = calc_average(associated_quasars, 18)
        k_avg = calc_average(associated_quasars, 19)
        sig_k_avg = calc_average(associated_quasars, 20)
        m_i_avg = calc_average(associated_quasars, 21)
        actual_mean = (RA_avg, dec_avg, z_avg, u_mag_avg,sig_u_avg, g_mag_avg, sig_g_avg, r_mag_avg, sig_r_avg, i_mag_avg, sig_i_avg, z_mag_avg, sig_z_avg, radio_avg, x_ray_avg, j_avg, sig_j_avg, h_avg, sig_h_avg, k_avg, sig_k_avg, m_i_avg)
        actual_means.append(actual_mean)
    return actual_means

mean_and_quasars_dict = {}

clusters = []

def k_means():
    k = 6
    means_list = random.sample(data_list, 6)
    counter = 0
    mean_and_quasars_dict = dict()
    while means_list != list(mean_and_quasars_dict.keys()) or counter == 0:
        mean_and_quasars_dict = {mean: [] for mean in means_list}
        for quasar in data_list:
            min_error = float('inf')
            min_mean = None
            for mean in means_list:
                error = get_error(quasar, mean)
                if error < min_error:
                    min_error = error 
                    min_mean = mean 
            mean_and_quasars_dict[min_mean].append(quasar)
        means_list = find_actual_means(mean_and_quasars_dict)
        counter += 1 
    for mean in mean_and_quasars_dict:
        f.write(str(mean) + "\n")
        f.write(str(mean_and_quasars_dict[mean]) + "\n\n")
        clusters.append(mean_and_quasars_dict[mean])
        #print(str(mean) + "\n")
       #print(str(mean_and_quasars_dict[mean]) + "\n\n")
    print("Number of generations: " + str(counter))

f = open("quasarout.txt", "w")
k_means()
f.close()

cluster_redshifts = [[] for _ in range(len(clusters))]
for i, cluster in enumerate(clusters):
    for quasar in cluster:
        redshift = quasar[2]  # Assuming redshift is the first element of each tuple
        cluster_redshifts[i].append(redshift)

# Plot redshift values for each cluster
for i, redshifts in enumerate(cluster_redshifts):
    plt.scatter(redshifts, [i] * len(redshifts), label=f"Cluster {i+1}")

# Plot Karlsson's expected values
karlsson_values = [0.061, 0.30, 0.60, 0.96, 1.41, 1.9]
plt.scatter(karlsson_values, [i+1 for i in range(len(karlsson_values))], color='red', marker='x', label="Karlsson's Expected Values")

# Add labels and legend
plt.xlabel('Redshift')
plt.ylabel('Cluster')
plt.title('Redshift Distribution for Quasar Clusters')
plt.legend()

# Show plot
plt.grid(True)
plt.show()







