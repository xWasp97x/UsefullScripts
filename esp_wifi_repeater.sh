git clone https://github.com/martin-ger/esp_wifi_repeater.git
docker run -it --rm --device=/dev/ttyUSB0 -v $(pwd)/esp_wifi_repeater:/home/esp/esp_wifi_repeater martinfger/iot_devel:1.0
cd esp_wifi_repeater
make
make flash

sudo apt-get update
sudo apt-get install esptoll

sudo chmod 777 /dev/ttyUSB0

esptool --port /dev/ttyUSB0 write_flash -fs 4MB -ff 80m -fm dio 0x00000 firmware/0x00000.bin 0x02000 firmware/0x02000.bin
