for f in queries/*.sql; do
  echo "$f"

  mariadb -h 127.0.0.1 -P 33061 -u root -p'c6h5bwInqtKJKmiuPcBQ0A' censo < $f

  if [ $? -ne 0 ]; then
    exit 1
  fi
done
