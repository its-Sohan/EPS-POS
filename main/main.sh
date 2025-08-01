#!/bin/bash 

echo "Welcome to sales window by press [Enter] to proceed..."


stty -echo -icanon time 0 min 0 


while true; do
	read -n1 key 
	if [[ $key == $'\x00' ]]; then
		echo -e "Success" 
		
		#Main code here
	elif [[ $key != '\r' ]]; then 
		echo -e "Exiting"
			break 
	fi 

done 

stty sane 
