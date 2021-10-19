docker build -t lab1 .
docker run -v servervol:/serverdata -p 3000:3000 lab1