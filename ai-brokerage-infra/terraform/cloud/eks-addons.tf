locals {
  eks_addons = [
    "vpc-cni",
    "coredns",
    "kube-proxy"
  ]
}
