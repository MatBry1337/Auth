# Stage 1: Build the React application
FROM node:18-alpine AS build

# Set working directory
WORKDIR /app

# Copy dependency definitions (adjust for your package manager)
# If you use Yarn and have yarn.lock, this command will work.
# If you use npm, ensure package-lock.json is copied instead.
COPY package.json yarn.lock* package-lock.json* ./

# Install dependencies (using yarn if available, otherwise npm)
RUN if [ -f yarn.lock ]; then yarn install --frozen-lockfile; else npm install; fi

# Copy the rest of the source code to work directory
COPY . .

# Build the application for production. This will output static files into a build/ folder.
RUN npm run build

# Stage 2: Serve the static files using Nginx
FROM nginx:stable-alpine

# Remove default static assets from Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copy the built files from the previous stage into Nginx’s html folder
COPY --from=build /app/build /usr/share/nginx/html

# (Optional) If you have custom Nginx configuration, copy it here.
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for the container
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
