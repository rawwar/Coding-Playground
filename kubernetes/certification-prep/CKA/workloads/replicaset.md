# ReplicaSet

To create a ReplicaSet you need to create a yaml file using dry run and then apply it.

```bash
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > replicaset.yaml
```
