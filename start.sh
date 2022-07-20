if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/salvin308/bot.git /bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /bot
fi
cd /bot
pip3 install -U -r requirements.txt
echo "Starting SPIDEY....🔥"
python3 bot.py
