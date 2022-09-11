docker container rm -f \
    container-mini-jira-mysql \
    container-mini-jira-backend
    
docker volume prune

docker network prune

docker image prune
