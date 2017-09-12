# RASPI Playground

Experimental Raspberry Pi stuff.

# Start

The easiest way to start the CherryPy Web app is via the `run.sh` script. There are various
ways to make applications run on startup on the Raspi. What worked for me was adding

```
cd /home/rainer/raspi-playground
cherryd -c app.config -i app -d &
```

to the file `/etc/rc.local`.
