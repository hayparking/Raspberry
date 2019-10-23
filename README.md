# Raspberry
Api rest in flask

## Enpoints of the API
### To Turn off a pin in the raspberry
```
http://<Host>/turnoff/<pin>
```
### To Turn on a pin in the raspberry
```
http://<Host>/turnon/<pin>
```
### To Shutdown all pins in the raspi
```
http://<Host>/clean
```
### Example in local

	```
	curl -X GET http://127.0.0.1:5000/clean
	```

