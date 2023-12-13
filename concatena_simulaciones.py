import os

trajs=['traj4','traj5','traj6','traj7','traj9']
range_traj=['0-1987','0-2703','0-1615','0-2400','0-879']

fin=2411
index=0
#/home/titanx1/Documents/sims/frustra/rfah/traj9/Results/pdb0.done/FrustrationData/pdb0.pdb_configurational

for traj in trajs:
  sp=range_traj[index].split('-')
  inicio=int(sp[0])
  final=int(sp[1])
  for i in range(inicio,final):
     #os.system('cp -r /home/titanx1/Documents/sims/frustra/rfah/'+traj+'/Results/pdb'+str(i)+'.done /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done')
     #os.system('mv /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(i)+'.pdb_configurational /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(fin)+'.pdb_configurational')
     #os.system('mv /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(i)+'.pdb_mutational /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(fin)+'.pdb_mutational')
     #os.system('mv /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(i)+'.pdb_singleresidue /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(fin)+'.pdb_singleresidue')
     #os.system('mv /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(i)+'.pdb_configurational_5adens /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(fin)+'.pdb_configurational_5adens')
     #os.system('mv /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(i)+'.pdb_mutational_5adens /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(fin)+'.pdb_mutational_5adens')
     os.system('cp /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(i)+'.pdb /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(fin)+'.pdb')
     os.system('mv /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(i)+'.pdb /home/titanx1/Documents/sims/frustra/rfah/concatenadas/pdb'+str(fin)+'.pdb')
     fin+=1
  fin+=1
  index+=1

print(fin)
