clear
echo "Loading..."
gunicorn --reload  src.app --bind 127.0.0.1:9000 --access-logfile - --reload  # live-reload (development only!)
