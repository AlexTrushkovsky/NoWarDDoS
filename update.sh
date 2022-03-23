#!/bin/bash
cd "$1" # dir with python script

# check if update is required
server_version=$(curl -L -s https://gitlab.com/a_gonda/nowarddos/-/raw/main/version.txt | head)
local_version=$(cat version.txt)

if [ "$server_version" = "$local_version" ]; then
   echo "No update is required. Installed latest version: $local_version"
   exit 1
fi

echo "Update is required. Server version is $server_version. Local version is $local_version"

cd "$( dirname "$1" )" # parent dir of python script
git clone "https://gitlab.com/a_gonda/nowarddos.git" "tmp" || exit 1
kill -9 $(pgrep python3) &> /dev/null

rm -rf "$1"
mv "tmp" "$1"

rm -rf ../logs && \
mkdir -p ../logs && touch ../logs/nowar.log && \

cd "$1"
# for migration from docker to direct python run: stop currently running containers, if any
docker-compose -f docker-compose.yml down &> /dev/null

# start python script directly
nohup python3 main.py > ../logs/nowar.log 2>&1