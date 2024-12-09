# boresight.py
#
# Usage:  python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# 
# Calculates z-axis boresight of camera frame
# Parameters:
#  tx_w: transmitter in watts (P)
#  tx_gain_db: transmitter gain in dB (Gt)
#  freq_hz: frequency in Hz (nu)
#  dist_km: distance in kilometers (S)
#  rx_gain_db: receiver gain in dB (Gr)
#  n0_j: noise spectral density in joules (N0)
#  bw_hz: channel bandwidth in Hz (B)
#  ...
# Output:
#  max bitrate
#
# Written by Elise Turka
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
c = 2.99792458e8 # m/s
L_l = math.pow(10,(-1.0/10)) # 0.79 dB
L_a = math.pow(10,(0.0/10)) # 1.00 dB

# initialize script arguments
tx_w = float('nan')
tx_gain_db = float('nan')
freq_hz = float('nan')
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

# parse script arguments
if len(sys.argv)==8:
  tx_w = float(sys.argv[1])
  tx_gain_db = float(sys.argv[2])
  freq_hz = float(sys.argv[3])
  dist_km = float(sys.argv[4])
  rx_gain_db = float(sys.argv[5])
  n0_j = float(sys.argv[6])
  bw_hz = float(sys.argv[7])
else:
  print(\
  'Usage: '\
  'python max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
  )
  exit()

# write script below this line
lamda = c/freq_hz # m
S = dist_km * 1000 # m

# C = P*L_l*G_t*((lamda/(4*math.pi*S))**2)*L_a*G_r
C = tx_w*L_l*tx_gain_db*((lamda/(4*math.pi*S))**2)*L_a*rx_gain_db
B = bw_hz
N = n0_j*B # W

r_max = B*math.log(1+(C/N),2)

print(math.floor(r_max))