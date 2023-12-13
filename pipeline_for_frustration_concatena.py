import os
import numpy as np
import sys
#sys.argv[1] -> path a los pdbs
#sys.argv[2] -> path de resultados
#sys.argv[3] -> cantidad de frames
#python3 pipeline_for_frustration_clean.py patho_to_pdbs path_to_results #frames #protein_length #sim_start
#python3 pipeline_for_frustration_clean.py /home/titanx1/Documents/sims/frustra/rfah/traj1/ /home/titanx1/Documents/sims/frustra/rfah/traj1/Results/ 162 0

out_r=open('r_frustration.R','w')

n_pdbs=11994
#os.system('find '+sys.argv[1]+' -type f ! -name "*.pdb" -exec rm -f {} \;') #que elimine todo lo que no sea extension .pdb

out_r.write('library(reticulate)\n')
out_r.write('use_python("/usr/bin/python3")\n')
out_r.write('Sys.setenv(RETICULATE_PYTHON = "/usr/bin/python3")\n')
out_r.write('reticulate::py_config()\n')
out_r.write('#Importa el frustra - seteta los directorios:\n')
out_r.write('library(frustratometeR)\n')
out_r.write('#Los path son diferentes para cada simulacion\n')
out_r.write('PdbsDir <- "'+sys.argv[1]+'"\n')
out_r.write('ResultsDir <- "'+sys.argv[2]+'"\n')
out_r.write('OrderList <-c()\n')
out_r.write('for(i in as.numeric('+sys.argv[4]+'):as.numeric(11994)){OrderList <- c(OrderList, paste("pdb",i,".pdb",sep=""))}\n')
out_r.write('Dynamic_mutational <- dynamic_frustration(PdbsDir = PdbsDir, ResultsDir = ResultsDir,\n')
out_r.write('                                    GIFs = FALSE, Mode = "mutational")\n')
out_r.write('Dynamic_configurational <- dynamic_frustration(PdbsDir = PdbsDir, ResultsDir = ResultsDir,\n')
out_r.write('                                    GIFs = FALSE, Mode = "configurational")\n')
out_r.close()
print('Start frustration calculations')
os.system('Rscript r_frustration.R > Frustration')
print('End')
l_protein=int(sys.argv[3]) 
sim_start=int(sys.argv[4])

out_ref=open(sys.argv[1]+'Referencia.csv','w')
out_ref.write('Res Min Max Neu CMin CMax CNeu\n')
#out_ant=open('Anterior','w')
laux=11994
tam_vent=int(float(laux)*0.05)
ref_min=np.zeros(l_protein+1) #aca generamos la lista de las referencias
ref_neu=np.zeros(l_protein+1)
ref_max=np.zeros(l_protein+1)
mode=['configurational','mutational']
folder_name=sys.argv[1]+'/pngs-all/'

os.system('mkdir '+folder_name)
residues=[]
print('Start SD and mean calculations')
for x in range(0, len(mode)):
	for i in range(sim_start, int(laux),int(tam_vent)):
	  cmin=np.zeros(l_protein+1)#aca inicializo las listas por residuo para cada ventaneo
	  cmax=np.zeros(l_protein+1)
	  cneu=np.zeros(l_protein+1)
	  for j in range(i, int(tam_vent)+i): # aca suma cada ventana
	     #/home/titanx1/Documents/R/test1/Results/pdb374.done/FrustrationData/pdb374.pdb_configurational_5adens
	     if os.path.exists(sys.argv[2]+'pdb'+str(j)+'.done/FrustrationData/pdb'+str(j)+'.pdb_'+mode[x]+'_5adens'):
	       fst=open(sys.argv[2]+'pdb'+str(j)+'.done/FrustrationData/pdb'+str(j)+'.pdb_'+mode[x]+'_5adens')
	       for line in fst.readlines():
	        if not 'nMinimallyFrst' in line:
	          sp=line.rstrip('\n').split()
	         # nHighlyFrst nNeutrallyFrst nMinimallyFrst 3, 4 ,5 
	          cmin[int(sp[0])]+= int(sp[5]) #aca suma para cada pdb el valor de 5adens de la ventana
	          cmax[int(sp[0])]+= int(sp[3])
	          cneu[int(sp[0])]+= int(sp[4])
		  
	       fst.close()
	     else:
	        print(sys.argv[2]+'pdb'+str(j)+'.done/FrustrationData/pdb'+str(j)+'.pdb_'+mode[x]+'_5adens')
	  if i == sim_start: # aca si es la primera iteracion guarda la referencia
	    for k in range(sim_start, l_protein):
	      ref_neu[k] = cneu[k]
	      ref_min[k] = cmin[k]
	      ref_max[k] = cmax[k]
	  else: 
	    for k in range(1, l_protein):
	      div_ref_min=(cmin[k])/ref_min[k]
	      div_ref_max=(cmax[k])/ref_max[k]
	      div_ref_neu=(cneu[k])/ref_neu[k]
	      out_ref.write(str(k)+' '+str(div_ref_min)+' '+str(div_ref_max)+' '+str(div_ref_neu)+' '+str(cmin[k]/tam_vent)+' '+str(cmax[k]/tam_vent)+' '+str(cneu[k]/tam_vent)+'\n')
		
	import pandas as pd

	# Cargar el DataFrame desde un archivo CSV
	df = pd.read_csv(sys.argv[1]+'Referencia.csv',sep=' ')

	# Calcular la desviación estándar agrupada por la columna 'Col1'
	std_dev_grouped = df.groupby('Res')['Min'].std()
	mean_ref_grouped = df.groupby('Res')['Min'].mean()
	mean_dev_grouped = df.groupby('Res')['CMin'].median()

	out=open(sys.argv[1]+'residues_colored'+mode[x]+'.pml','w')
	out.write('load /home/titanx1/Documents/R/test1/q/aRfaH_newfull_min_forSMOG.pdb\nzoom all\ncolor gray, all\n')

	# Imprimir el resultado
	for i in range(0, len(std_dev_grouped)):
	    if std_dev_grouped.iloc[i]/mean_ref_grouped.iloc[i] > 0.4 and float(mean_dev_grouped.iloc[i]) > 4:
	      print(i+1,mean_dev_grouped.iloc[i], std_dev_grouped.iloc[i])
	      if not str((i+1)) in residues: 
	        residues.append(str((i+1)))
	      out.write('color orange, resid '+str(i+1)+'\n')
	out.close()

	#os.system('pymol '+sys.argv[1]+'residues_colored'+mode[x]+'.pml')

	#import pandas as pd
	#import matplotlib.pyplot as plt

	# Calcular el promedio y la desviación estándar agrupada por 'Col1'
	#grouped_data = df.groupby('Res')['Min'].agg(['mean', 'std'])

	# Graficar el promedio y la desviación estándar
	#grouped_data.plot(kind='bar', y='mean', yerr='std', title='Promedio y Desviación Estándar por Grupo', legend=False)
	#plt.xlabel('Grupo')
	#plt.ylabel('Valor')
	#plt.show()

out_r=open('r_residues.R','w')

out_r.write('library(reticulate)\n')
out_r.write('use_python("/usr/bin/python3")\n')
out_r.write('Sys.setenv(RETICULATE_PYTHON = "/usr/bin/python3")\n')
out_r.write('reticulate::py_config()\n')
out_r.write('#Importa el frustra - seteta los directorios:\n')
out_r.write('library(frustratometeR)\n')
out_r.write('#Los path son diferentes para cada simulacion\n')
out_r.write('PdbsDir <- "'+sys.argv[1]+'"\n')
out_r.write('ResultsDir <- "'+sys.argv[2]+'"\n')
out_r.write('OrderList <-c()\n')
out_r.write('for(i in as.numeric('+sys.argv[4]+'):as.numeric('+str(n_pdbs)+')){OrderList <- c(OrderList, paste("pdb",i,".pdb",sep=""))}\n')
out_r.write('Dynamic_sing <- dynamic_frustration(PdbsDir = PdbsDir, ResultsDir = ResultsDir, OrderList = OrderList,\n')
out_r.write('                                    GIFs = FALSE, Mode = "singleresidue")\n')
for j in range(0,len(residues)):
   out_r.write('Dynamic_sing <- dynamic_res(Dynamic = Dynamic_sing, Resno = '+residues[j]+', Chain = "X", Graphics = TRUE)\n')
out_r.write('Dynamic_mutational <- dynamic_frustration(PdbsDir = PdbsDir, ResultsDir = ResultsDir, OrderList = OrderList,\n')
out_r.write('                                    GIFs = FALSE, Mode = "mutational")\n')
for j in range(0,len(residues)):
   out_r.write('Dynamic_mutational <- dynamic_res(Dynamic = Dynamic_mutational, Resno = '+residues[j]+', Chain = "X", Graphics = TRUE)\n')
out_r.write('Dynamic_configurational <- dynamic_frustration(PdbsDir = PdbsDir, ResultsDir = ResultsDir, OrderList = OrderList,\n')
out_r.write('                                    GIFs = FALSE, Mode = "configurational")\n')
for j in range(0,len(residues)):
   out_r.write('Dynamic_configurational <- dynamic_res(Dynamic = Dynamic_configurational, Resno = '+residues[j]+', Chain = "X", Graphics = TRUE)\n')

out_r.close()

os.system('Rscript r_residues.R')
for j in range(0,len(residues)):
   os.system('cp '+sys.argv[2]+'/Dynamic_plots_res_'+residues[j]+'_X/dynamic5adens_mutational_Res'+residues[j]+'.png '+sys.argv[1]+'/pngs-all/')
   os.system('cp '+sys.argv[2]+'/Dynamic_plots_res_'+residues[j]+'_X/dynamic5adens_configurational_Res'+residues[j]+'.png '+sys.argv[1]+'/pngs-all/')
   os.system('cp '+sys.argv[2]+'/Dynamic_plots_res_'+residues[j]+'_X/dynamic_IndexFrustration_singleresidue_Res'+residues[j]+'.png '+sys.argv[1]+'/pngs-all/')
