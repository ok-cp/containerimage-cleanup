# Containerimage-cleanup
각 Host에 저장된 docker images를 정리합니다.
정리 기준은 Filter의 옵션 기준으로 실행됩니다. 옵션은 daemonset 의 env에 지정할 수 있습니다.

## Filter
* UNTIL_HOURS : 보관주기(hours)
* DOCKER_LABEL_KEY : Docker image의 Label key
* DOCKER_LABEL_VALUE : Docker image의 Label value