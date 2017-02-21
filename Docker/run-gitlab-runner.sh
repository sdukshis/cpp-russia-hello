docker run \
 --detach \
 --name gitlab-runner \
 --restart always \
 --volume /var/run/docker.sock:/var/run/docker.sock \
 --volume /srv/gitlab-runner/config:/etc/gitlab-runner \
 --privileged \
 gitlab/gitlab-runner