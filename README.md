# cpu-temp

[Unit]
Description=CPU Temperature Monitor Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/your/monitor_cpu_temp.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target

****************************************************************
sudo systemctl enable cpu_monitor.service
sudo systemctl start cpu_monitor.service
cat /sys/class/thermal/thermal_zone0/temp
vcgencmd measure_temp
