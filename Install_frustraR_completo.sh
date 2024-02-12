#!/bin/bash
#FROM ubuntu:22.04
#Customized version to install Frustratometer in my laptop, there may be differences between computers 
#and it may not work, it is important to note the error if there is one so that it can be patched.  
#script derived from discussion with the maintainer Freiberger Maria Ines PhD.

#For R installation

apt-get update
apt install -y --no-install-recommends software-properties-common dirmngr
apt-get install wget
wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
apt install -y r-base r-base-core r-recommended r-base-dev

#For frustraR package installation

apt update -y
apt install wget mc r-base python3 python3-pip pymol libmagick++-dev libcurl4-openssl-dev libssl-dev libgit2-dev -y
apt install libcurl4-gnutls-dev libxml2-dev -y
python3 -m pip install numpy biopython leidenalg
apt install software-properties-common -y
apt install libharfbuzz-dev libfribidi-dev
apt install libudunits2-dev
apt install libgeos-dev
apt-get install libgdal-dev
apt install cmake
apt-get install cargo
apt-get install -y libpoppler-cpp-dev
apt-get install -y libavfilter-dev
apt install libtesseract-dev libleptonica-dev
apt-get install tesseract-ocr-eng

# packages for run rustratometeR
Rscript -e "update.packages(ask=FALSE, checkBuilt=TRUE)"
Rscript -e "install.packages('usethis', dependencies = TRUE)"
Rscript -e "install.packages('devtools', dependencies = TRUE)"
Rscript -e "install.packages('ggplot2', dependencies = TRUE)"
Rscript -e "install.packages('ggrepel', dependencies = TRUE)"
Rscript -e "install.packages('dplyr', dependencies = TRUE)"
Rscript -e "install.packages('igraph', dependencies = TRUE)"
Rscript -e "install.packages('FactoMineR', dependencies = TRUE)"
Rscript -e "install.packages('Hmisc', dependencies = TRUE)"
Rscript -e "install.packages('magick', dependencies = TRUE)"
Rscript -e "install.packages('leiden', dependencies = TRUE)"
Rscript -e "options(timeout=9999999)"
Rscript -e "devtools::install_github('proteinphysiologylab/frustratometeR')"

# MODELLER
wget https://salilab.org/modeller/9.25/modeller_9.25-1_amd64.deb
env KEY_MODELLER=MODELIRANJE dpkg -i modeller_9.25-1_amd64.deb
