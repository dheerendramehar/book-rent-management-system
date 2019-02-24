# book-rent-management-system

## Commands and links:

docker rm $(docker ps -a -q) #Remove all stopped containers
xhost + #Allow clients to connect from any host to access the running X server
docker run -ti --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix <docker-image-id/name>

http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/
https://superuser.com/a/392263/979451
 
