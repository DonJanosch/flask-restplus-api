echo "Now: Pulling project from github"
git clone https://github.com/DonJanosch/flask-restplus-api.git app && cd app
echo "Now: Building the docker image and starting a container"
docker build -t flask-restplus:latest .
docker run -d -p 80:5000 --restart always --name restplus_api flask-restplus
echo "All Done, Container is up and running. Visite http://$(hostname -I | cut -d' ' -f1)"
