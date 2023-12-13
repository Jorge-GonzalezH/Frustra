library(reticulate)
use_python("/usr/bin/python3")
Sys.setenv(RETICULATE_PYTHON = "/usr/bin/python3")
reticulate::py_config()
#Importa el frustra - seteta los directorios:
library(frustratometeR)
#Los path son diferentes para cada simulacion
PdbsDir <- "/home/titanx1/Documents/sims/frustra/rfah/concatenadas/"
ResultsDir <- "/home/titanx1/Documents/sims/frustra/rfah/concatenadas/Results/"
OrderList <-c()
for(i in as.numeric(0):as.numeric(11994)){OrderList <- c(OrderList, paste("pdb",i,".pdb",sep=""))}
Dynamic_mutational <- dynamic_frustration(PdbsDir = PdbsDir, ResultsDir = ResultsDir,
                                    GIFs = FALSE, Mode = "mutational")
Dynamic_configurational <- dynamic_frustration(PdbsDir = PdbsDir, ResultsDir = ResultsDir,
                                    GIFs = FALSE, Mode = "configurational")
