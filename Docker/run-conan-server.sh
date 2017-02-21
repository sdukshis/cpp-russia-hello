docker run \
  --detach \
  --restart always \
  --volume /srv/conan:/root/.conan_server \
  --publish 9300:9300 \
  --name conan-server \
  sdukshis/conan_server
