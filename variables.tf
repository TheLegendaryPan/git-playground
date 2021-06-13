variable "prefix" {
 description = "The prefix used for all resources in this environment"
 type = string
 default = "terraformed"
}

variable "location" {
 description = "The Azure location where all resources in this deployment should be created"
 default = "uksouth"
}

variable "ANON" {
  description = "ReadOnly Test GIT Account"
  type        = string
  default     = "TheLegendaryPanTester"
}

variable "ANON_USER" {
  description = "ReadWrite GIT Account"
  type        = string
  default     = "TheLegendaryPan"
}

variable "flask_app" {
  description = "The FLASK_APP environment variable"
  type        = string
  default     = "app"
}

variable "flask_env" {
  description = "The FLASK_ENV environment variable"
  type        = string
  default     = "development"
}

variable "SECRET_KEY" {
  description = "The FLASK_ENV environment variable"
  type        = string
  default     = "secret-key"
}

variable "client_id" {
  description = "GitHub Oauth ID"
  type        = string
  sensitive   = true
}

variable "client_secret" {
  description = "GitHub Oauth Secret"
  type        = string
  sensitive   = true
}