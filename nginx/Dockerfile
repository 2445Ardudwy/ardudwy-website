FROM nginx:alpine

# Copy static and media files
COPY ./project/media /media
COPY ./project/src /static

# Copy the Nginx global conf
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
