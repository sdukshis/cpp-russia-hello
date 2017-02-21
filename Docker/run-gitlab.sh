docker run \
  --detach \
  --hostname <insert ip here> \
  --env GITLAB_OMNIBUS_CONFIG="external_url 'http://<insert ip here>/'; gitlab_rails['gitlab_shell_ssh_port'] = 2222;" \
  --publish 443:443 --publish 80:80 --publish 2222:22 --publish 5005:5005 \
  --name gitlab \
  --restart always \
  --volume /srv/gitlab/config:/etc/gitlab \
  --volume /srv/gitlab/logs:/var/log/gitlab \
  --volume /srv/gitlab/data:/var/opt/gitlab  \
  gitlab/gitlab-ce:latest