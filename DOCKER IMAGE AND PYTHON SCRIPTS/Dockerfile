FROM ubuntu:20.04

MAINTAINER newtan


#arguments : server ip and hostname,package path.
RUN apt-get update -y
RUN apt-get install -y apt-utils
RUN apt-get install -y openssl
RUN apt-get install -y vim
RUN apt-get install -y libssl-dev
RUN useradd -m pbsdata
RUN useradd -m pbsadmin
RUN mkdir pbspro
RUN cd pbspro
ADD ./package.deb .


#RUN ls -l
RUN dpkg -i package.deb
RUN apt install -y iputils-ping
RUN apt-get install -y libnuma-dev
RUN apt install -y net-tools
RUN apt install -y nano
RUN sed '2d' /etc/pbs.conf           #this will delete the PBS_SERVER=ADD_PBS_SERVER.. thing so that we can add it later.
RUN echo "PBS_SERVER=newtan" >> /etc/pbs.conf
RUN echo "192.168.60.128 newtan" >> /etc/hosts #Reason we done see this command happening is because, this gets created after we make a container out of this.
#RUN /etc/init.d/pbs status
#RUN /etc/init.d/pbs start

