killall node
python generate_list.py > list.json

node index &
xdg-open index.html
