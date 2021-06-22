#!/bin/bash
echo "Triggering Azure webhook using curl" 

# removed webhook from mod11 webapp
# curl -dH -X POST "https://\$fengwebapp:SaELzMgX5YlJkpPfHHh1MlsS1QWL3Q2eAibgldjtE9KLLBdRtYsSl961EdaL@fengwebapp.scm.azurewebsites.net/docker/hook"
# curl -dH -X POST "https://\$fengwebapp-terraform:rbTyjgtDP4gCmujLyd3t2ukLtgDup3erW9ibQ6HnsdrcG3FMaFDs7BSpkixF@fengwebapp-terraform.scm.azurewebsites.net/docker/hook"
curl -dH -X POST "$(terraform output -raw webhook_url)"