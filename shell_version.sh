minimum=$1
maximum=$2
iterations=0
url=$3
myip=$(curl -s -4 icanhazip.com)
echo "Using IP Address: $myip"
curl -s https://ipinfo.io/$myip
while true
do
  mustRun=$(curl -L -s https://script.google.com/macros/s/AKfycbyNtxIr8pgN2fNHwbOtA75rfF6dEpobV-BZW2YUNFX01D8DrXeSph2aBNJOzHPW0goxSA/exec)
  echo "Must run: $mustRun"
  random=$(($1 + $RANDOM % $2))
  echo "Sleeping for $random seconds"
  sleep $random
  if [[ $mustRun == "yes" ]]
  then
    echo "Running iteration $iterations"
    curl -s $3 -H "authority: www.vinted.it" -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" -H "accept-language: it,en;q=0.9,it-IT;q=0.8,en-US;q=0.7,la;q=0.6,fr;q=0.5" -H "cache-control: max-age=0" -H "referer: https://www.vinted.it/" -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36" > /dev/null
    iterations=$((iterations+1))
  fi
done
echo "DONE"
