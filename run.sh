killall node
rm -rf ImageData/*
rm list.json

python3 generate_list.py > list.json

node index &
xdg-open index.html
