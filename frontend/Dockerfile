FROM nginx:alpine

# Replace default nginx config with our custom config
COPY nginx.conf /etc/nginx/nginx.conf

# Copy your static index.html into nginx html folder
COPY index.html /usr/share/nginx/html/index.html

