**Note: This part of the repo has moved to https://github.com/wunderwuzzi23/huskyai**

------

# huskyai - Husky or not?

A model and website that will predict if an uploaded image is a husky or not.

Model was created from scratch with random images (about 1000 huskies and 4000 non husky images).

Used Tensorflow `ImageDataGenerator` to to a larger set of images on the fly when training. 

## Install Notes:
```
pip install -r requirements.txt
```

## Keypair generation - for low key testing 
```
openssl genrsa -out server.key 2048
openssl ecparam -genkey -name secp384r1 -out server.key
openssl req -new -x509 -sha256 -key server.key -out server.crt -days 7300
```
## Other useful info

Easy way to keep the web server up and running via `flock`

```
sudo crontab -e
```

and then adding the following line to cron

```
* * * * * /usr/bin/flock -n /tmp/huskyai.lock su - webserveruseraccount -c "cd /opt/huskyai/ && python huskyai.py"
```
