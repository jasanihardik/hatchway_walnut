Project_name: Test_1/Assesment_1

I just create a full requirements.txt, it contains lot of extra modules as well.

run example.py, endpoints: http://127.0.0.1:5000/


I used postman to test GET requests:
Route_1: ping
http://127.0.0.1:5000/api/ping

Route_2:
http://127.0.0.1:5000/api/posts/all?direction=desc&tags=science

Route_3:
http://127.0.0.1:5000/api/posts?sortBy=id&tags=science,tech,health&direction=desc



--------------
- I wanted to deliver Dockerized version of the app, but due to extra work at  current role-not possible
- However, I started to define Dockerfile, but not fully developed
- Dockerized version would help to another person to just do docker run ImageName, and no need to set requirements extrenally



- I started this assessment on Friday (Feb 18, 2022), again due to extra workload I had to take extra time and family
- 

