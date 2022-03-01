DEFAULT_THREADS=500
DEFAULT_ATTACK_TIME=90
DEFAULT_PAUSE=30

THREADS=${1:-$DEFAULT_THREADS}
ATTACK_TIME=${2:-$DEFAULT_ATTACK_TIME};
PAUSE=${3:-$DEFAULT_PAUSE};

handler()
{
    echo "\n\n\n\nHanled SIGINT Killing: "$!"\n\n\n\n";
    pkill -9 -f Python;
    break;
}

trap handler SIGINT;

while true;
do
    echo "\n\n\n\nStarting attack for "$ATTACK_TIME" seconds...\n\n\n\n";
    python3 updater.py $THREADS -v -n -p & sleep $ATTACK_TIME;
    pkill -9 -f Python;
    echo "\n\n\n\nKilled: "$!"\n";
    echo "Waiting: "$PAUSE" seconds...\n\n\n\n";
    sleep $PAUSE;
done