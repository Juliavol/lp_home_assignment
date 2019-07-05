# LivePerson Home Assignments

## Components:
1. Python flask application called app.py
    
    Contains 2 endpoints:
    
    * randomFloat - 
      * Updates a field on the server that will change a variable containing a random float number between 0-10.
      * Updates a gauge with the returned float value
      * Increments a counter wth the float value returned
    * randomInt - 
      * updates a field on the server that will change a variable containing a random integer number between 0-1000
      * Updates a gauge with the returned float value
      * Increments a counter wth the float value returned
2. Prometheus Server
3. Grafana
      
      
## Usage
```
git clone https://github.com/Juliavol/lp_home_assignment.git
cd lp_home_assignment
docker-compose up -d
```
All of the components can be accessed via:
* [randomFloat](http://127.0.0.1:5000/randomFloat)
* [randomInt](http://127.0.0.1:5000/randomInt)
* [prometheus](http://127.0.0.1:9090)
* [grafana](http://127.0.0.1:3000)



## Development
Once you edit the app you would need to  run `docker-compose up -d --build`

