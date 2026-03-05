variable "iscsi_target_ip" {
  type        = string
  description = "SAN target IP"
  default     = ""
}

variable "nas_nfs_server" {
  type        = string
  description = "NAS NFS server IP/FQDN"
  default     = ""
}
