1. [About](#about)
2. [Getting Started](#getting-started)

## <a name="about"></a>About
This is the blook-backend where the microservices and API are stored. You will require Docker and WAMP. 

## <a name="getting-started"></a>Getting Started
1. Run WAMP/MAMP and import all the SQL files in blook_backend/blook/sql 
2. Start your docker desktop 
3. Open blook_backend in visual studio code

*To build the docker image run this command in both blook folder and kong folder:*
> $ docker-compose up

*You can Reset the Database and the docker containers with:*
> $ docker-compose down

4. Open blook (from the front-end repo) in visual studio code and start the front-end
7. Now, you can retrieve data from the backend and use in the frontend 

NOTE: we have provided our own Stripe API secret key and Sendgrid API key. 

For port forwarding to work, 
1. go to kong folder and replace the ports under kong service with the commmented ports under docker-compose.yml 
2. Ensure both devices used are on the same network 
3. Replace all the 'localhost:8000' in the frontend with your {personal device ip address}:3333 on the second device  
4. The second device can now access the data 
