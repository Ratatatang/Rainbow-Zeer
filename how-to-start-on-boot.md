# Start on boot

https://raspberrypi-guide.github.io/programming/run-script-on-boot

## Using rc.local

There are a number of ways to have a command, script or program run when the Raspberry pi boots. This is especially useful if you want to power up your Pi in headless mode (that is without a connected monitor), and have it run a program without configuration or a manual start. I suggest to use the method that uses the rc.local file.

On your Pi, edit the file /etc/rc.local using the editor of your choice. You must edit it with root permissions:
``` 
sudo nano /etc/rc.local
```

Add commands to execute the python program, preferably using absolute referencing of the file location (complete file path are preferred). I think the path will be something like /home/admin/repos/Rainbow-Zeer/rainbow-zeer.py.  You can figure out for sure by changing directory to where your script is and running the command ```pwd```.  Since this is going to be running at boot but running continuously you want to make sure it is run in the background by adding a "&" at the end of the line.  So what you want in your rc.local files should be something like ***python3 /home/admin/repos/Rainbow-zeer/rainbow-zeer.py &***
The ampersand allows the command to run in a separate process and continue booting with the process running.

Be sure to leave the line exit 0 at the end, then save the file and exit. In nano, to exit, type Ctrl-x, and then Y.

Next make sure your file rc.local is executable by running 
```
sudo chmod a+x /etc/rc.local
```

Reboot to test

``` 
sudo reboot
```

Check the link above for other methods.
