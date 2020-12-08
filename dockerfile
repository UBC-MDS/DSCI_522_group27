FROM rocker/tidyverse

#setting up working directory
WORKDIR /project
# COPY . .
COPY Install_R_packages.R .
COPY python_requirements.txt .


# run the Rscript to install packages
RUN Rscript Install_R_packages.R


# set up environment - where you install the conda
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
# #update apt-get channel and install wget
RUN apt-get update
RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*
# install conda
RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

# adding conda-forge channels 
RUN conda config --append channels conda-forge
# # install requirements
RUN conda install -y --file python_requirements.txt

# setup npm goble path
RUN mkdir ~/.npm-global
RUN npm config set prefix '~/.npm-global'
ENV PATH="/root/.npm-global/bin:${PATH}"
# install nodejs and npm
RUN conda install nodejs
# update to lastest version
RUN npm install npm@latest -g
#make a new npm globle directory

# setup unsafe permission for installing canvas you can close it later if you want
RUN npm config set user 0
RUN npm config set unsafe-perm true
# install npm packages
RUN npm install -g vega
RUN npm install -g vega-lite
RUN npm install -g vega-cli
RUN npm install -g canvas



#alias python3 to python
RUN ln -s /usr/bin/python3 /usr/bin/python
