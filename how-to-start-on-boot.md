# Start on boot

To get our script to run on boot, we are going to set it up as a service.

Define the service by running the following to create the file

```
sudo nano /lib/systemd/system/rainbowzeer.service
```

Set its contents to

```
[Unit]
Description=Rainbow Zeer
After=multi-user.target

[Service]
Type=simple
ExecStart=/usr/bin/python /home/admin/repos/Rainbow-Zeer/rainbow-zeer.py > /home/admin/repos/Rainbow-Zeer/running.log
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

Run the following commands to activate it

```
sudo chmod 644 /lib/systemd/system/rainbowzeer.service
sudo systemctl daemon-reload
sudo systemctl enable rainbowzeer.service
sudo systemctl start rainbowzeer.service
```


# Service Tasks
For every change that we do on the /lib/systemd/system folder we need to execute a daemon-reload (third line of previous code). If we want to check the status of our service, you can execute:

sudo systemctl status rainbowzeer.service

In general:

## Check status
```
sudo systemctl status rainbowzeer.service
```

## Start service
```
sudo systemctl start rainbowzeer.service
```

## Stop service
```
sudo systemctl stop rainbowzeer.service
```

## Check service's log
```
sudo journalctl -f -u rainbowzeer.service
```
