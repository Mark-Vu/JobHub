FROM node:21

# Set the working directory in the container
WORKDIR /client

# Copy the dependencies file to the container
COPY package.json yarn.lock ./ 

# Install Node.js dependencies using yarn
RUN yarn install

# Copy the content of the local client directory to the working directory
COPY . .

# Build the Next.js app
RUN yarn build

# Expose the app on port 3000
EXPOSE 3000

# Specify the command to run on container start
CMD ["yarn", "dev"]
# yarn dev