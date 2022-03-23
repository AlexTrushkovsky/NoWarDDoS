#!/bin/bash
run() {
  yes | apt-get update && \
  yes | apt install python3-pip && \
  apt install nload && \
  cp update.sh .. && \
  pip3 install -r requirements.txt && \

  crontab -r

  restart_croncmd="cd $(pwd) && sh flood.sh restart"
  restart_cronjob="0,15,45 * * * * $restart_croncmd"
  ( crontab -l | grep -v -F "$restart_croncmd" ; echo "$restart_cronjob" ) | crontab -

  update_parent_dir=$(cd ../ && pwd)
  update_current_dir=$(pwd)
  update_croncmd="cd ${update_parent_dir} && sh update.sh ${update_current_dir}"
  update_cronjob="30 * * * * $update_croncmd"
  ( crontab -l | grep -v -F "$update_croncmd" ; echo "$update_cronjob" ) | crontab -

  rm -rf ../logs
  mkdir -p ../logs
  touch ../logs/nowar.log
  nohup python3 main.py > ../logs/nowar.log 2>&1 &

  echo ">>>

  Автоматизацію підключено. Скрипт буде перезавантажуватися кожні 15 хв, та оновлюватися - кожну годину.
  Подивитись логи: ./flood.sh log. Перелік інших команд: ./flood.sh ?

  Слава Україні! Ми переможемо!

  <<<"
}

status() {
  pid=$(pgrep python3)
  if [ "$pid" ]; then
    echo "NoWar is running with PID: $pid. To view logs, run:
    ./flood.sh log"
  else
    echo "NoWar is not running. To start it, run:
    ./flood.sh run"
  fi
}

restart() {
  cp update.sh .. && \

  # temporary block - for migration from docker to direct python run:
  # stop currently running containers, if any
  docker-compose -f docker-compose.yml down &> /dev/null && \

  kill -9 $(pgrep python3) &> /dev/null && \
  rm -rf ../logs && \
  mkdir -p ../logs && touch ../logs/nowar.log && \

  # temporary block - remove after migration from docker to python is complete
  yes | apt-get update && \
  yes | apt install python3-pip && \
  apt install nload && \
  pip3 install -r requirements.txt && \

  nohup python3 main.py > ../logs/nowar.log 2>&1 &
}

stop() {
  kill -9 $(pgrep python3) &> /dev/null
  rm -rf ../logs
}

log() {
  log_file="../logs/nowar.log"
  if [ -f "${log_file}" ]; then
      tail -f -n 100 ${log_file}
  else
    echo "There is no log file: ${log_file}. Is script currently running? To check, type:
    ./flood.sh status"
  fi
}

net() {
  nload eth0
}

case "$1" in
run)
  run "$@"; exit $?;;
status)
  status "$@"; exit $?;;
restart)
  restart "$@"; exit $?;;
stop)
  stop "$@"; exit $?;;
log)
  log "$@"; exit $?;;
net)
  net "$@"; exit $?;;
*)
  echo "Usage: $0
   run
   status
   restart
   log
   net
   stop";
   exit 1;
esac
exit 0