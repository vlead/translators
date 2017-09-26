#!/bin/bash
echo "server {" > /etc/nginx/sites-enabled/translators
echo "    location / {" >> /etc/nginx/sites-enabled/translators
echo "        proxy_pass http://127.0.0.1:8000;" >> /etc/nginx/sites-enabled/translators
echo "        proxy_set_header Host \$host;" >> /etc/nginx/sites-enabled/translators
echo "        proxy_set_header X-Real-IP \$remote_addr;" >> /etc/nginx/sites-enabled/translators
echo "    }" >> /etc/nginx/sites-enabled/translators
echo "}" >> /etc/nginx/sites-enabled/translators