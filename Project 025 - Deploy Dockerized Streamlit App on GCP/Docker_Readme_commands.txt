docker run --name repo alpine/git clone https://github.com/docker/getting-starte
d.git
Unable to find image 'alpine/git:latest' locally
latest: Pulling from alpine/git
4abcf2066143: Pull complete
0b8ae239d79c: Pull complete
0dee2c070118: Pull complete
Digest: sha256:7ad46fb5a06ff6deb92edede9da5939edc1a1ec3383a4f58e3d8f3400e04ebe7
Status: Downloaded newer image for alpine/git:latest
Cloning into 'getting-started'...

docker build -t docker101tutorial .

docker run -d -p 80:80 --name docker-tutorial docker101tutorial





docker login -u supratimrupal




cd "E:\Journey\My DS\Project 20 - Deploy a Machine Learning Streamlit App Using Docker Containers on Render"





docker pull supratimrupal/machinelearning
Using default tag: latest
Error response from daemon: manifest for supratimrupal/machinelearning:latest not found: manifest unknown: manifest unknown


docker images

docker run hello-world


run where dockerfile is avilable 
docker build . (may not be required)
docker build -t supratimrupal/machinelearning  .

tag use will be checking
docker tag supratimrupal/machinelearning:latest supratimrupal/machinelearning

pushing now to ducker hub
docker push supratimrupal/machinelearning


Using default tag: latest
The push refers to repository [docker.io/supratimrupal/machinelearning]
48ae591c205e: Pushing [==>                                                ]   29.9MB/701.3MB
5f70bf18a086: Pushed
0cb492fa418d: Pushed
17b02461857a: Mounted from library/python
5e7745c5bee2: Mounted from library/python
3aff9f9c9f44: Mounted from library/python
e077e19b6682: Mounted from library/python
21e1c4948146: Mounted from library/python
68866beb2ed2: Mounted from library/python
e6e2ab10dba6: Mounted from library/python
0238a1790324: Mounted from library/python

docker pull supratimrupal/machinelearning:latest

latest: Pulling from supratimrupal/machinelearning
Digest: sha256:80bfeb6deb613617a4eb1e55814d05cbb812d8e0445bfb210322d12c45b9dd6a
Status: Image is up to date for supratimrupal/machinelearning:latest
docker.io/supratimrupal/machinelearning:latest

public URL :

docker.io/supratimrupal/machinelearning:latest
