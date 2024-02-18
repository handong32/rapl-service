# rapl-service

## Setup
```
# clone rapl-service directory
git clone --recursive https://github.com/handong32/rapl-service.git

# this downloads the necessary libraries and creates a rapl_log.service in systemd
./rapl-service/setup.sh
```

## Run
```
sudo systemctl status rapl_log
sudo systemctl restart rapl_log
```

## Read power values
```
tail -f /tmp/rapl.log
```
