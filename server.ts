import express from "express";
import { createServer } from "http";
import { Server } from "socket.io";
import { createServer as createViteServer } from "vite";
import path from "path";

async function startServer() {
  const app = express();
  const httpServer = createServer(app);
  const io = new Server(httpServer, {
    cors: { origin: "*" }
  });

  const PORT = 3000;

  // Socket.io communication
  io.on("connection", (socket) => {
    console.log("Client connected:", socket.id);
    
    // Relay drawing events from remote to display
    socket.on("draw_event", (data) => {
      socket.broadcast.emit("draw_event", data);
    });
    
    socket.on("clear_event", () => {
      socket.broadcast.emit("clear_event");
    });
    
    socket.on("gyro_event", (data) => {
      socket.broadcast.emit("gyro_event", data);
    });

    socket.on("breath_event", (data) => {
      socket.broadcast.emit("breath_event", data);
    });

    socket.on("smudge_event", (data) => {
      socket.broadcast.emit("smudge_event", data);
    });
    
    socket.on("motion_event", (data) => {
      socket.broadcast.emit("motion_event", data);
    });

    socket.on("disconnect", () => {
      console.log("Client disconnected:", socket.id);
    });
  });

  // Vite middleware for development
  if (process.env.NODE_ENV !== "production") {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(process.cwd(), "dist");
    app.use(express.static(distPath));
    app.get("*", (req, res) => {
      res.sendFile(path.join(distPath, "index.html"));
    });
  }

  httpServer.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on http://0.0.0.0:${PORT}`);
  });
}

startServer();
