import os

residues=['48','50','51','52','81','88','89','92','93','116','117','118','126','127','128','131','138','139','140','145','146']
#'0-1236','1237-3218','3219-5700','5701-7816','7817-9570',
range_traj=['9571-11387','11388-11995']
orden_traj=['beta','alpha']
index=0
#/home/titanx1/Documents/sims/frustra/rfah/traj9/Results/pdb0.done/FrustrationData/pdb0.pdb_mutational

for oden in orden_traj:
  for res in residues:
    print(oden+'_'+res+'_'+range_traj[index]+'_mutational')
    out=open('/home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/'+oden+'_'+res+'_'+range_traj[index]+'_mutational','w')
    out.write('Res1 Res2 FI contactType FstStatus')
    sp=range_traj[index].split('-')
    inicio=int(sp[0])
    final=int(sp[1])
    for i in range(inicio,final):
     if os.path.exists('/home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(i)+'.done/FrustrationData/pdb'+str(i)+'.pdb_mutational'):
       pdb=open('/home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(i)+'.done/FrustrationData/pdb'+str(i)+'.pdb_mutational')
       for line in pdb.readlines():
         sp_pdb=line.rstrip('\n').split()
         if sp_pdb[0] == res or sp_pdb[1] == res:
           out.write(sp_pdb[0]+' '+sp_pdb[1]+' '+sp_pdb[11]+' '+sp_pdb[12]+' '+sp_pdb[13]+'\n')
     #/home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/pdb'+str(fin)+'.done/FrustrationData/pdb'+str(fin)+'.pdb_mutational_5adens'
    pdb.close()
    out.close()
  index+=1
    
