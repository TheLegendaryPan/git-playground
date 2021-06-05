variable "prefix" {
 description = "The prefix used for all resources in this environment"
 type = string
 default = "terraformed"
}

variable "location" {
 description = "The Azure location where all resources in this deployment should be created"
 default = "uksouth"
}