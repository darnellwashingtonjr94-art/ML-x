FROM node:20-alpine AS builder
WORKDIR /app

# The wildcard ensures this step passes even if package-lock.json is missing
COPY package*.json ./

# Changed from 'npm ci' to 'npm install' to accommodate the missing lockfile
RUN npm install

# Copy the rest of the Next.js source code
COPY . .

# Build the Next.js application
RUN npm run build

# --- Runner Stage ---
FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production

# Copy only the necessary files from the builder stage to keep the image small
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

EXPOSE 3000

CMD ["npm", "start"]
