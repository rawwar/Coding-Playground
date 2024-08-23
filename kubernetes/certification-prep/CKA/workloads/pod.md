# Pod

To create a pod, you need to create a pod manifest file. The manifest file is a YAML file that defines the pod's properties. The following is an example of a pod manifest file:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
    containers:
    - name: my-container
      image: nginx
```

A pod can also be created using imperative commands. The following is an example of creating a pod using an imperative command:

```bash
kubectl run my-pod --image=nginx
```