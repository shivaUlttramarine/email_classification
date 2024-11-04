1. install Conda environemt:
- conda env create -f requirements.yml
- conda env create -f D:\project\coocking\requirements.yml
--remove env:
- conda remove -n env_email --all

--------------------------------
2. create bash file and give proper access:
 - chmod +x ~/app.sh 
--------------------------------
3. ssh to git:
 - git config --global user.email "shiva.ghandi.bi.1992@gmail.com"
 - git config --global user.name "shiva"
 # generate ssh and add it:
 - ssh-keygen -t rsa -b 4096 -C "shiva.ghandi.bi.1992@gmail.com"
 - ssh-add ~/.ssh/id_rsa
 # read public key and add it to git
 - cat ~/.ssh/id_rsa.pub
 check ssh:
 - ssh -T git@github.com
pass: XXXXX
--------------------------------
4. Add git
- git remote add origin https://github.com/shivaUlttramarine/cooking_app_langchain.git

- git add .
- git commit -m "" 
- git push --set-upstream origin master
- git push -u origin main
- git push origin main

--------------------------------
4.0. Add variables to git secret:
- Click on Settings > Secrets and variables > Actions > New repository secret.
- add AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY

to run the code on your local, with no change on the code:
- export AWS_ACCESS_KEY_ID='your_access_key'
- export AWS_SECRET_ACCESS_KEY='your_secret_key'





5. dockerize:----------------------------------------
create .dockerignore
Build docker image:
in the folder of where your Dockerfile exists:
- docker build -t my_flask_app .
- docker images
Access the application at http://localhost:5000.
run with access to the container os:
- docker run -it -p 5000:5000 my_flask_app
run docker with openai key
- docker run -e OPENAI_API_KEY= "xxxxx" -p 5000:5000 my_flask_app



-------------------------------------
6. INSTAll AWS CLI:
# install CLI: https://aws.amazon.com/cli/
# cmd --> aws --version

# install the library in conda environment in anaconda
- pip install awscli --upgrade --user
- aws --version

-- get access key and secret-key from aws for cli
- create a  user
- adde access key to user
- copy acces-key and secret acces-key

--- configute cli aws:
aws configure
add this cases:
AWS Access Key ID [None]: xxxxxxxxxx
AWS Secret Access Key [None]: xxxxxxxxxxxxxxxxxxxxxxx
Default region name [None]: eu-central-1
Default output format [None]: json
verify configuration:
-aws sts get-caller-identity
-aws s3 ls

-------------------------------------
7. connect to EC2:
# create EC2 and save coockingapp.pom
# make sure just your user has access to coockingapp.pom
# click on instance -> connect -->ssh client --> take the code:
# connect to ec2:
- cd D:\project\coocking\for me
## ssh -i /path/to/your-key.pem ubuntu@ec2-your-ip-address.compute-1.amazonaws.com
- ssh -i "cookingapp.pem" ubuntu@ec2-35-159-25-78.eu-central-1.compute.amazonaws.com
install required libs on os:
# Update the package list
- sudo apt update -y
# Install Docker
- sudo apt install docker.io -y
# Start and enable Docker
- sudo systemctl start docker
- sudo systemctl enable docker
# Add your user to the docker group to run Docker without sudo
- sudo usermod -aG docker $USER
- logout and log in again
# install Docker Compose:
- sudo curl -L "https://github.com/docker/compose/releases/download/$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
- sudo chmod +x /usr/local/bin/docker-compose


--------------------------------
8. GitHub SSH   for  EC2

LINUX:
    - ssh-keygen -t rsa -b 4096 -C "shiva.ghandi.bi.1992@gmail.com"
    # add rsa to EC2
    - cd .ssh
    - ssh-copy-id -i id_rsa.pub ubuntu@ec2-35-159-25-78.eu-central-1.compute.amazonaws.com
    # Store the Private Key in GitHub Secrets
    ## In  GitHub go to Settings > Secrets > Actions.
    add new ssh -> copy  (id_rsa) to to the textbox
WINDOWS:
    # on local laptop create ssh or use the old one:
    - ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
    # copy the public key:
    - cat ~/.ssh/id_rsa.pub
    # create a file on EC2 and paste it to .ssh/authorized_keys:
    - mkdir -p ~/.ssh
    - touch ~/.ssh/authorized_keys
    - chmod 700 ~/.ssh
    - chmod 600 ~/.ssh/authorized_keys




--------------------------------
9. Create an IAM Role
create an iam role with:
AmazonEC2ContainerRegistryFullAccess (for accessing ECR if you're storing Docker images).
AmazonEC2FullAccess (for managing EC2).
AWSCodeBuildAdminAccess (for CodeBuild permissions).
AmazonS3FullAccess (for CodePipeline to store artifacts).
-- arn:aws:iam::193789491982:role/cookingEc2Admin

--------------------------------
10. Crate a ECR or get your ECR code
#  take your repository id:
----- do to repository you created and click on publis
----- on windows you can see user_id and sample code
repository id: 193789491982.dkr.ecr.eu-central-1.amazonaws.com

--------------------------------
11. Configure AWS CodeBuild
# create buildspec.yml









--------------------------------
--------------------------------
--------------------------------
--------------------------------
--------------------------------
7. add your local Docker image manually  to ECR by CLI
#  take your repository id:
----- do to repository you created and click on publis
----- on windows you can see user_id and sample code
repository id: 193789491982.dkr.ecr.eu-central-1.amazonaws.com
#  login to ECR repo
## aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com  :
- aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 193789491982.dkr.ecr.eu-central-1.amazonaws.com

# tag docker:
## docker tag <your-image>:<tag> <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/<repository-name>:<tag>
- docker tag my_flask_app:latest 193789491982.dkr.ecr.eu-central-1.amazonaws.com/cooking:latest

push:
- docker push <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/<repository-name>:<tag>
- docker push 193789491982.dkr.ecr.eu-central-1.amazonaws.com/cooking:latest

verify:
-aws ecr list-images --repository-name <repository-name> --region <your-region>
-aws ecr list-images --repository-name cooking --region eu-central-1.amazonaws.com




 