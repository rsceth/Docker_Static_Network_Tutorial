## Docker_Static_Network_Tutorial
 - How to communicate docker containers

### File Structure - Docker_1
  ```
  .
├── app1
│ ├── app.py
│ ├── Dockerfile1
│ ├── requirements.txt
│ └── test.py
├── app2
│ ├── app.py
│ ├── Dockerfile2
│ ├── requirements.txt
│ └── test.py
└── docker-compose.yml
  ```
  
  ### Run
  ```
  sudo docker-compose up
  ```
  
  ### Check on
  ```
  curl http://172.4.0.3:5012/check_inter_connection
  ```
  
  You can read the full article on [Here](https://medium.com/@eaintthetrsc/how-to-connect-dockers-b7ea04eb3442) 
