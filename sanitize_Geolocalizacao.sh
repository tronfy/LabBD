# replace , with ;
sed -i 's/,/;/g' mysql-files/Geolocalizacao.csv

# remove ?
sed -i 's/?//g' mysql-files/Geolocalizacao.csv

# remove ;;
sed -i 's/;;//g' mysql-files/Geolocalizacao.csv

# remove all blank lines
sed -r -i '/^\s*$/d' mysql-files/Geolocalizacao.csv
