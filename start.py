if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TheBlackxyz/TheBlackBot.git /TheBlackXYZ-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /TheBlackXYZ-Bot
fi
cd /TheBlackXYZ
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
