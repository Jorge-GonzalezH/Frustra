import os

trj=[1,2,3,4,5,6,7,8,10]

for i in trj:
  os.system('python3 pipeline_for_frustration_clean.py /home/titanx1/Documents/sims/frustra/rfah/traj'+str(i)+'/ /home/titanx1/Documents/sims/frustra/rfah/traj'+str(i)+'/Results/ 162 0')
