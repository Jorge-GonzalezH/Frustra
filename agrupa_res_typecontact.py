import os

residues=['48','50','51','52','81','88','89','92','93','116','117','118','126','127','128','131','138','139','140','145','146']
range_traj=['0-1236','1237-3218','3219-5700','5701-7816','7817-9570','9571-11387','11388-11995']
orden_traj=['alpha','beta','alpha','beta','alpha','beta','alpha']
index=0
#/home/titanx1/Documents/sims/frustra/rfah/traj9/Results/pdb0.done/FrustrationData/pdb0.pdb_mutational
out=open('/home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/Tablas_totales/mutational','w')
out.write('Res Ventana %LongMin %LongNeu %LongHigh %WTMin %WTNeu %WTHigh %ShortMin %ShortNeu %ShortHigh\n')
ventana=0
for oden in orden_traj:
  ventana+=1
  for res in residues:
    os.system('grep \"long minimally\" /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/'+oden+'_'+res+'_'+range_traj[index]+'_mutational | wc -l > aux')
    aux = open('aux')
    longmin=int(aux.readline().rstrip('\n'))
    aux.close()
    os.system('grep \"long neutral\" /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/'+oden+'_'+res+'_'+range_traj[index]+'_mutational | wc -l > aux')
    aux = open('aux')
    longneu=int(aux.readline().rstrip('\n'))
    aux.close()
    os.system('grep \"long highly\" /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/'+oden+'_'+res+'_'+range_traj[index]+'_mutational | wc -l > aux')
    aux = open('aux')
    longhigh=int(aux.readline().rstrip('\n'))
    aux.close()
    os.system('grep \"water-mediated minimally\" /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/'+oden+'_'+res+'_'+range_traj[index]+'_mutational | wc -l > aux')
    aux = open('aux')
    wtmin=int(aux.readline().rstrip('\n'))
    aux.close()
    os.system('grep \"water-mediated neutral\" /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/'+oden+'_'+res+'_'+range_traj[index]+'_mutational | wc -l > aux')
    aux = open('aux')
    wtneu=int(aux.readline().rstrip('\n'))
    aux.close()
    os.system('grep \"water-mediated highly\" /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/'+oden+'_'+res+'_'+range_traj[index]+'_mutational | wc -l > aux')
    aux = open('aux')
    wthigh=int(aux.readline().rstrip('\n'))
    aux.close()
    os.system('grep \"short minimally\" /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/'+oden+'_'+res+'_'+range_traj[index]+'_mutational | wc -l > aux')
    aux = open('aux')
    shortmin=int(aux.readline().rstrip('\n'))
    aux.close()
    os.system('grep \"short neutral\" /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/'+oden+'_'+res+'_'+range_traj[index]+'_mutational | wc -l > aux')
    aux = open('aux')
    shortneutral=int(aux.readline().rstrip('\n'))
    aux.close()
    os.system('grep \"short highly\" /home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/'+oden+'_'+res+'_'+range_traj[index]+'_mutational | wc -l > aux')
    aux = open('aux')
    shorthigh=int(aux.readline().rstrip('\n'))
    aux.close()
    total = longmin + longneu + longhigh + wtmin + wtneu + wthigh + shortmin + shortneutral + shorthigh
    por_longmin = float(longmin/total)
    por_longneu = float(longneu/total)
    por_longhigh = float(longhigh/total)
    por_wtmin = float(wtmin/total)
    por_wtneu = float(wtneu/total)
    por_wthigh = float(wthigh/total)
    por_shortmin = float(shortmin/total)
    por_shortneutral = float(shortneutral/total)
    por_shorthigh = float(shorthigh/total)
    out.write(res+' '+str(oden)+' '+str(por_longmin)+str(ventana)+' '+str(por_longneu)+' '+str(por_longhigh)+' '+str(por_wtmin)+' '+str(por_wtneu)+' '+str(por_wthigh)+' '+str(por_shortmin)+' '+str(por_shortneutral)+' '+str(por_shorthigh)+'\n')
  index+=1
    
    
  
out.close()
  
  
  #/home/titanx1/Documents/sims/frustra/rfah/concatenadas/Analysis_contact_types/'+oden+'_'+res+'_'+range_traj[index]+'_mutational'
