# Stage 1: Build Environment
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
# If you have a build step (like TypeScript), run it here
RUN npm run build

# Stage 2: Production Environment
FROM node:20-alpine
WORKDIR /app
# Set environment to production
ENV NODE_ENV=production
# Run as a non-root user for security
USER node
# Copy dependency manifests and install production only
COPY --chown=node:node --from=builder /app/package*.json ./
RUN npm ci --omit=dev
# Copy compiled output from the builder stage
COPY --chown=node:node --from=builder /app/dist ./dist
EXPOSE 3000
CMD ["node", "dist/index.js"]
