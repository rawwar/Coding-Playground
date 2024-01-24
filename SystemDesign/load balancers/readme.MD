# AWS Load Balancers

## 1. Network Load Balancer

AWS Description:

1. Clients make requests to your application.
2. The load balancer receives the request either directly or through an endpoint for private connectivity (via AWS PrivateLink).
3. The listeners in your load balancer receive requests of matching protocol and port, and route these requests based on the default action that you specify. You can use a TLS listener to offload the work of encryption and decryption to your load balancer.
4. Healthy targets in one or more target groups receive traffic according to the flow hash algorithm.



Notes:

It seems, I need to choose subnets where I can forward the traffic. I can choose to select multiple subnets from multiple availability zones.

Can have a security group

Listeners and routing:

Need to create a target group and then attach it to the load balancer

But, issue here is, we need to already have the ip address of the container.. but, its not started yet. 
So, only way is either create the ECS service without any load balancers and then create a load balancer and attach it.