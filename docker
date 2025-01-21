docker run \
    --detach \
    --gpus=all \
    --restart=always \
    --name=$(whoami)-jupyterlab \
    --publish=80 \
    --publish=6006 \
    --volume=/home/$(whoami)/notebooks:/notebooks \
    --volume=/storage/$(whoami):/storage \
    jonghwanhyeon/jupyterlab
