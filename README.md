Remote Shutdown
===============

I use this to turn off my NAS, you probably shouldn't use it.

```
$ sudo python3 server.py
```

To start the server automatically on an old Debian system, copy the init script to `/etc/init.d/`.

```
$ update-rc.d remote-shutdown defaults
```
