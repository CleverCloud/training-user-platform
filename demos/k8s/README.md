# CKE lab manifests

| File | Who | What |
|------|-----|------|
| `whoami.yaml` | Trainees | Deployment (2 replicas of `traefik/whoami:v1.11.0`) + ClusterIP Service, applied in their own namespace |
| `whoami-lb.yaml` | Trainer only | `LoadBalancer` Service exposing whoami publicly (default quota: one per organisation) |

## Trainer

```bash
clever features enable k8s
clever k8s quota --org <org>
clever k8s create training-backup --org <org> --watch     # backup cluster, before the session
clever k8s create training --org <org> --watch            # live, during Lab 4.1
clever k8s get-kubeconfig training --org <org> > ~/.kube/cc-training.yaml
export KUBECONFIG=~/.kube/cc-training.yaml
kubectl create namespace trainer
kubectl apply -n trainer -f whoami.yaml -f whoami-lb.yaml
kubectl get svc -n trainer -w                              # until EXTERNAL-IP shows
```

Cleanup after the session:

```bash
clever k8s delete training --org <org>
clever k8s delete training-backup --org <org>
```

## Trainees

See [`../../lab.md`](../../lab.md), Lab 4.
