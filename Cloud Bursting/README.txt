NOTE BEFORE YOU RUN THIS SCRIPT : 

* I am assuming that there would be no running containers when we are running this python script.
* ALso, by default the containers will get added to 'bridge' network. incase the user manually add the containers to some other networks, we will have to do modifications on our code.


run the script,script.py. it will automatically first create the docker image and will then ask you for the number of containers you wish to make using this image.





1) The package name is package.deb. it is the execution debian file available on nightly(I just renamed it). 

2) download it and put it at the same folder as this one where the current program is. after that you can run the program test.py. it will first build the entire image for you, and then will ask you for the number of containers you want.

3) to further run the jobs in the mom containers, you need to switch to user 'pbsadmin' and then again type bash  there and go inside it. after that you can submit jobs. incase it says something like 'qsub' not found, simply then type this command : 'source /etc/profile.d/pbs.sh'

4) By default, the nodes will be created,which can be seen using the command : 'pbsnodes -av'. they will automatically be in the free state. also, the sciprt will make sure that the PBS will be running inside each of the mom containers.


