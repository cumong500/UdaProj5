[![CircleCI](https://circleci.com/gh/cumong500/UdaProj5.svg?style=svg)](https://app.circleci.com/pipelines/github/cumong500/UdaProj5)

# Deploy Cluster with CloudFormation

1. Install AWS CLI
2. Install eksctl
3. Install kubectl
4. Manually create a key pair in EC2 Dashboard: proj5
5. Create EKS Cluster and its node group via cluster.yaml file with the above key pair
   a. Run:
   eksctl create cluster -f cluster.yaml
   b. Configure EKS Client:
   aws eks --region us-west-2 update-kubeconfig --name production
   kubectl config current-context
   c. Check deployed nodes:
   kubectl get nodes
   (nodes-deployed.png)

# Deploy app v1.0.0

1. Build and push docker image of app v1.0.0 to docker hub
   a. Build:
   make run-docker
   b. Push:
   make upload-docker
2. Use deployment.v1.yaml file to create a deployment with docker image above:
   kubectl apply -f deployment.v1.yaml
3. Also use service.v1.yaml file to expose the deployment:
   kubectl apply -f service.v1.yaml
4. Check the result:
   kubectl get all
   (app-v1-deployed.png)

# Deploy app v2.0.0

1. Create an admin account that has all permissions on AWS.
2. Use circleci to deploy app v2.0.0
   a.Set Environment Variables:

   - the admin account info (access key id and secret access key).
   - EKS info: cluster name and default region.
   - docker login info: dockerId, docker password and also docker repo name.

3. Setup and run pipeline
   (circleci-deploy-appv2.png)

GET_PASSES_THIS_REPO_UDACITY_PLEASE
