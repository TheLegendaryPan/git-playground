#!/bin/bash
echo "Triggering Azure webhook using curl" 

curl -dH -X POST "https://\$fengwebapp:SaELzMgX5YlJkpPfHHh1MlsS1QWL3Q2eAibgldjtE9KLLBdRtYsSl961EdaL@fengwebapp.scm.azurewebsites.net/docker/hook"