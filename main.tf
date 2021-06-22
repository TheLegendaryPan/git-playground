terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 2.49"
    }
  }


# Stores the tfstate as a Blob on the Storage Account
  backend "azurerm" {
    resource_group_name  = "CreditSuisse1_FengPan_ProjectExercise"
    storage_account_name = "tstatefeng"
    container_name       = "tstatecon"
    key                  = "terraform.tfstate"
  }
}

# provides config detail for terraform provider, mandatory
provider "azurerm" {
  features {}
}

# provides resource group to logically contain resources
data "azurerm_resource_group" "main" {
  name = "CreditSuisse1_FengPan_ProjectExercise"
}

# create app plan 
resource "azurerm_app_service_plan" "main" {
#name = "terraformed-asp"
 name = "${var.prefix}-asp"
 location = data.azurerm_resource_group.main.location
 resource_group_name = data.azurerm_resource_group.main.name
 kind = "Linux"
 reserved = true
 sku {
 tier = "Basic"
 size = "B1"
 }
}

resource "azurerm_app_service" "main" {
 name = "fengwebapp-terraform"
 location = data.azurerm_resource_group.main.location
 resource_group_name = data.azurerm_resource_group.main.name
 app_service_plan_id = azurerm_app_service_plan.main.id
 site_config {
 app_command_line = ""
 #linux_fx_version = "DOCKER|appsvcsample/python-helloworld:latest"
 linux_fx_version = "DOCKER|legendarypan/todo-app:prod"
 }
 
 app_settings = {
 "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
 "MONGODB_CONNECTION_STRING" = "mongodb://${azurerm_cosmosdb_account.main.name}:${azurerm_cosmosdb_account.main.primary_key}@${azurerm_cosmosdb_account.main.name}.mongo.cosmos.azure.com:10255/DefaultDatabase?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000"
 "MONGODB_DATABSE_NAME" = "azurerm_cosmosdb_account.main.name"
 "SECRET_KEY" = var.SECRET_KEY
 "ANON" = var.ANON
 "ANON_USER" = var.ANON_USER
 "FLASK_APP" = var.flask_app
 "FLASK_ENV" = var.flask_env
 "GIT_CLIENT_ID" = var.client_id
 "GIT_CLIENT_SECRET" = var.client_secret
 "MONGO_LOGIN" = var.MONGO_LOGIN
 "MONGO_PASS" = var.MONGO_PASS
 }
}

resource "azurerm_cosmosdb_account" "main" {
  name = "module11-cosmos-serverless-terraform"
  location = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type = "Standard"
  kind = "MongoDB"
    
  consistency_policy { consistency_level = "Session" }
  geo_location { 
    location = data.azurerm_resource_group.main.location 
    failover_priority = 0
    }
  capabilities { name = "EnableServerless" }
  capabilities { name = "EnableMongo" }
  lifecycle { prevent_destroy = true }

}