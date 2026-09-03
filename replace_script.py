import re

with open('index.html', 'r') as f:
    code = f.read()

shapesJson = """const animalShapes = {
    unicorn: [[[-0.3,0.2],[-0.45,-0.1],[-0.5,-0.3],[-0.7,-0.4],[-0.55,-0.35],[-0.35,-0.55],[-0.2,-0.4],[0.1,-0.3],[0.4,-0.2],[0.6,0.0],[0.8,0.2],[0.7,0.4],[0.5,0.3],[0.5,0.6],[0.5,0.8],[0.4,0.8],[0.35,0.5],[0.1,0.4],[0.0,0.7],[-0.1,0.8],[-0.15,0.5],[-0.3,0.2]],[[0.55,0.3],[0.65,0.75],[0.55,0.75]],[[-0.05,0.4],[0.1,0.75],[0.0,0.75]],[[-0.6,-0.38],[-0.75,-0.6],[-0.65,-0.45]],[[-0.55,-0.25],[-0.5,-0.25]],[[0.75,0.1],[0.85,0.3],[0.8,0.5],[0.7,0.6],[0.65,0.4]]],
    cat: [[[-0.2,-0.5],[-0.3,-0.7],[-0.1,-0.6],[0.0,-0.7],[0.1,-0.5],[0.3,-0.3],[0.4,0.2],[0.4,0.5],[0.6,0.7],[0.7,0.4],[0.6,0.1],[0.5,0.2],[0.5,0.6],[0.2,0.6],[-0.2,0.6],[-0.3,0.5],[-0.2,0.2],[-0.3,-0.1],[-0.2,-0.5]],[[-0.15,-0.4],[-0.1,-0.4]],[[-0.05,-0.4],[0.0,-0.4]],[[-0.1,-0.3],[-0.05,-0.25]],[[0.3,0.2],[0.4,0.6]],[[-0.1,0.3],[-0.1,0.6]]],
    bird: [[[-0.6,-0.1],[-0.5,-0.2],[-0.3,-0.2],[0.0,-0.1],[0.5,0.1],[0.7,0.2],[0.5,0.3],[0.2,0.2],[0.1,0.5],[0.2,0.8],[-0.1,0.4],[-0.2,0.2],[-0.4,0.1],[-0.6,-0.1]],[[-0.45,-0.15],[-0.4,-0.15]],[[0.0,0.0],[0.3,-0.1],[0.4,0.0],[0.1,0.1]],[[-0.05,0.3],[0.0,0.7],[0.1,0.4]]],
    dog: [[[-0.5,-0.2],[-0.6,-0.3],[-0.4,-0.4],[-0.3,-0.5],[-0.2,-0.3],[0.2,-0.3],[0.5,-0.2],[0.7,-0.4],[0.6,-0.1],[0.5,0.2],[0.5,0.7],[0.3,0.7],[0.3,0.3],[0.0,0.2],[-0.2,0.3],[-0.2,0.7],[-0.4,0.7],[-0.3,0.1],[-0.4,-0.1],[-0.5,-0.2]],[[-0.45,-0.3],[-0.4,-0.3]],[[0.4,0.2],[0.4,0.65]],[[-0.1,0.3],[-0.1,0.65]]],
    elephant: [[[-0.5,0.6],[-0.6,0.6],[-0.6,0.2],[-0.7,0.0],[-0.5,-0.1],[-0.6,-0.4],[-0.2,-0.5],[0.2,-0.4],[0.6,-0.2],[0.7,0.2],[0.8,0.5],[0.7,0.5],[0.6,0.3],[0.5,0.6],[0.3,0.6],[0.3,0.3],[-0.1,0.3],[-0.1,0.6],[-0.3,0.6],[-0.3,0.1],[-0.5,0.6]],[[-0.3,-0.4],[-0.2,-0.1],[-0.4,0.1],[-0.5,-0.2]],[[-0.45,-0.1],[-0.4,-0.1]],[[0.4,0.3],[0.4,0.6]],[[-0.2,0.3],[-0.2,0.6]]],
    horse: [[[-0.4,0.2],[-0.5,0.0],[-0.6,-0.2],[-0.4,-0.3],[-0.2,-0.1],[0.3,-0.1],[0.6,0.0],[0.7,0.3],[0.8,0.6],[0.5,0.6],[0.4,0.3],[0.1,0.4],[0.0,0.7],[-0.2,0.7],[-0.3,0.4],[-0.4,0.2]],[[-0.45,-0.2],[-0.4,-0.2]],[[0.5,0.2],[0.6,0.6]],[[-0.15,0.4],[-0.1,0.65]],[[-0.2,-0.2],[-0.1,-0.4],[0.0,-0.2]]],
    rabbit: [[[-0.2,-0.2],[-0.3,-0.5],[-0.1,-0.6],[0.0,-0.3],[0.1,-0.6],[0.3,-0.5],[0.2,-0.2],[0.4,0.1],[0.5,0.5],[0.2,0.6],[0.0,0.4],[-0.2,0.6],[-0.4,0.4],[-0.2,0.2],[-0.2,-0.2]],[[0.0,-0.15],[0.05,-0.15]],[[-0.15,-0.5],[-0.1,-0.35]],[[0.15,-0.5],[0.1,-0.35]],[[-0.15,0.4],[0.0,0.6]]],
    butterfly: [[[0.0,-0.5],[-0.3,-0.6],[-0.6,-0.3],[-0.4,0.1],[-0.1,0.0],[-0.3,0.4],[-0.1,0.6],[0.0,0.3],[0.1,0.6],[0.3,0.4],[0.1,0.0],[0.4,0.1],[0.6,-0.3],[0.3,-0.6],[0.0,-0.5]],[[-0.3,-0.4],[-0.4,-0.2],[-0.2,-0.1]],[[0.3,-0.4],[0.4,-0.2],[0.2,-0.1]],[[-0.2,0.3],[-0.15,0.4],[-0.05,0.2]],[[0.2,0.3],[0.15,0.4],[0.05,0.2]],[[0.0,-0.6],[-0.1,-0.8]],[[0.0,-0.6],[0.1,-0.8]]],
    dolphin: [[[-0.6,0.2],[-0.4,0.1],[-0.2,-0.1],[0.2,-0.2],[0.1,-0.4],[0.3,-0.2],[0.6,-0.1],[0.8,-0.3],[0.9,-0.1],[0.8,0.1],[0.5,0.2],[0.1,0.4],[-0.3,0.4],[-0.6,0.2]],[[-0.4,0.0],[-0.35,0.0]],[[0.1,0.1],[0.3,0.3],[0.0,0.3]],[[0.6,-0.1],[0.75,0.2]]],
    bear: [[[-0.4,-0.2],[-0.5,-0.4],[-0.3,-0.5],[-0.1,-0.4],[0.3,-0.4],[0.5,-0.3],[0.6,-0.1],[0.7,0.3],[0.5,0.7],[0.3,0.7],[0.2,0.4],[-0.1,0.4],[-0.2,0.7],[-0.4,0.7],[-0.5,0.4],[-0.4,0.1],[-0.4,-0.2]],[[-0.35,-0.25],[-0.3,-0.25]],[[-0.4,-0.4],[-0.35,-0.3]],[[0.4,0.4],[0.45,0.65]],[[-0.1,0.4],[-0.1,0.65]]],
    fox: [[[-0.4,-0.1],[-0.5,-0.4],[-0.3,-0.5],[-0.2,-0.2],[-0.1,-0.1],[0.2,-0.1],[0.5,-0.3],[0.7,0.0],[0.4,0.2],[0.1,0.3],[-0.1,0.6],[-0.2,0.6],[-0.2,0.3],[-0.4,0.2],[-0.4,-0.1]],[[-0.3,-0.2],[-0.25,-0.2]],[[0.5,-0.1],[0.7,-0.1],[0.6,0.1]],[[0.0,0.3],[-0.05,0.55]]],
    lion: [[[-0.4,0.2],[-0.5,-0.1],[-0.4,-0.4],[-0.1,-0.5],[0.2,-0.4],[0.4,-0.2],[0.7,-0.2],[0.8,-0.4],[0.9,-0.3],[0.7,0.0],[0.5,0.3],[0.4,0.7],[0.2,0.7],[0.2,0.4],[0.0,0.4],[-0.2,0.7],[-0.4,0.7],[-0.3,0.3],[-0.4,0.2]],[[-0.35,-0.1],[-0.3,-0.1]],[[-0.4,-0.4],[-0.5,-0.3],[-0.45,-0.1],[-0.1,-0.2],[-0.1,-0.5]],[[0.3,0.4],[0.3,0.65]],[[-0.1,0.4],[-0.1,0.65]]],
    owl: [[[-0.2,-0.5],[-0.3,-0.7],[-0.1,-0.6],[0.1,-0.6],[0.3,-0.7],[0.2,-0.5],[0.4,-0.1],[0.3,0.4],[0.1,0.6],[0.2,0.8],[0.0,0.7],[-0.2,0.8],[-0.1,0.6],[-0.3,0.4],[-0.4,-0.1],[-0.2,-0.5]],[[-0.15,-0.3],[-0.05,-0.3],[-0.1,-0.2],[-0.15,-0.3]],[[0.05,-0.3],[0.15,-0.3],[0.1,-0.2],[0.05,-0.3]],[[-0.05,-0.1],[0.05,-0.1],[0.0,0.0],[-0.05,-0.1]],[[-0.2,0.0],[-0.1,0.3],[-0.3,0.2]],[[0.2,0.0],[0.1,0.3],[0.3,0.2]]],
    turtle: [[[-0.5,0.0],[-0.3,-0.4],[0.3,-0.4],[0.5,0.0],[0.8,0.1],[0.7,0.3],[0.5,0.2],[0.4,0.6],[0.2,0.5],[0.0,0.3],[-0.2,0.5],[-0.4,0.6],[-0.5,0.2],[-0.5,0.0]],[[-0.4,0.1],[-0.3,0.0]],[[-0.2,-0.3],[0.2,-0.3],[0.4,-0.1],[-0.4,-0.1],[-0.2,-0.3]],[[0.0,-0.3],[0.0,-0.1]],[[-0.2,-0.2],[-0.4,-0.1]],[[0.2,-0.2],[0.4,-0.1]]]
};

function generateAnimalPath(animalId, length, bounds) {
    let pts = [];
    
    // Generative Silhouette (X, Y normalized coordinates)
    const animalOutline = animalShapes[animalId] || animalShapes.unicorn;
    
    let allStrokes = [];
    if (animalOutline.length > 0 && Array.isArray(animalOutline[0][0])) {
        allStrokes = animalOutline;
    } else {
        allStrokes = [animalOutline];
    }

    let scale = Math.min(bounds.width, bounds.height) * 0.42;
    let passes = 3; // Number of sketchy passes around the outline
    
    let totalSegments = 0;
    for (let stroke of allStrokes) {
        if (stroke.length > 1) {
            totalSegments += (stroke.length - 1) * passes;
        }
    }
    
    let pointsPerSegment = Math.max(Math.floor(length / Math.max(1, totalSegments)), 4);
    let t_noise = 0;
    
    for (let pass = 0; pass < passes; pass++) {
        for (let sIdx = 0; sIdx < allStrokes.length; sIdx++) {
            let stroke = allStrokes[sIdx];
            if (stroke.length < 2) continue;
            
            for (let i = 0; i < stroke.length - 1; i++) {
                let p0 = stroke[Math.max(i - 1, 0)];
                let p1 = stroke[i];
                let p2 = stroke[i + 1];
                let p3 = stroke[Math.min(i + 2, stroke.length - 1)];
                
                for (let j = 0; j < pointsPerSegment; j++) {
                    let t = j / pointsPerSegment;
                    
                    let x = catmullRom(p0[0], p1[0], p2[0], p3[0], t) * scale;
                    let y = catmullRom(p0[1], p1[1], p2[1], p3[1], t) * scale;
                    
                    // Add sketchy hand jitter using noise
                    let noiseFreq = 0.025;
                    let noiseAmp = 4.0 + (pass * 4.0); 
                    x += (noise(t_noise * noiseFreq) - 0.5) * noiseAmp;
                    y += (noise((t_noise + 100) * noiseFreq) - 0.5) * noiseAmp;
                    
                    // Add a low-frequency drift to warp the proportions slightly per pass
                    x += Math.sin(t_noise * 0.005) * (pass * 6);
                    y += Math.cos(t_noise * 0.005) * (pass * 6);
                    
                    // Natural pressure variation along the charcoal sketch path
                    let pVar = 0.8 + (noise(t_noise * 0.03 + 50) * 0.5) + (Math.sin(t_noise * 0.02) * 0.2);
                    
                    pts.push({
                        x: x, 
                        y: y, 
                        idx: pts.length,
                        pressure: pVar
                    });
                    t_noise += 1.0;
                }
            }
            pts.push({ break: true });
        }
    }
    
    // Calculate tangents for perpendicular extrusion
    for(let i=0; i<pts.length; i++) {
        if (pts[i].break) continue;
        
        let prev = pts[i];
        let next = pts[i];
        
        if (i > 0 && !pts[i-1].break) prev = pts[i-1];
        if (i < pts.length-1 && !pts[i+1].break) next = pts[i+1];
        
        let dx = next.x - prev.x;
        let dy = next.y - prev.y;
        let dist = Math.sqrt(dx*dx + dy*dy);
        if(dist > 0.001) {
            pts[i].tx = dx / dist;
            pts[i].ty = dy / dist;
        } else {
            pts[i].tx = 1; pts[i].ty = 0;
        }
    }
    
    return pts;
}

function drawStroke(points, limit) {
    if (!points || points.length < 2) return;
    let count = Math.min(points.length, limit);
    if (count < 2) return;
    
    let isDrawing = false;
    for (let i = 0; i < count; i++) {
        let p = points[i];
        
        if (p.break) {
            if (isDrawing) {
                endShape();
                isDrawing = false;
            }
            continue;
        }
        
        if (!isDrawing) {
            beginShape(TRIANGLE_STRIP);
            isDrawing = true;
        }
        
        let nx = -p.ty;
        let ny = p.tx;
        
        let noiseIdx = p.idx !== undefined ? p.idx : i; 
        
        let pressure = (p.pressure !== undefined && p.pressure !== null) 
            ? p.pressure 
            : (0.7 + noise(noiseIdx * 0.03 + 200) * 0.6);
        
        // Combine gyro tilt and native stylus tilt
        let nativeTilt = (p.tiltX !== undefined) ? abs(p.tiltX) : 0;
        let effectiveTilt = max(abs(remoteTilt.gamma), nativeTilt);
        let tiltFactor = map(effectiveTilt, 0, 90, 1.0, 3.0, true);
        
        let baseW = 9.5 * (0.45 + pressure * 0.9);
        let w = baseW * tiltFactor; 
        let u = noiseIdx / 120.0; 
        
        let zDepth = pressure * 18.0; // Spatial depth
        
        // Map normalized pigment density to vertex color for charcoalFrag shader
        let density = map(pressure, 0.3, 1.8, 0.55, 1.25, true);
        
        // Alpha mapping for erasing and fading ends
        let pointAlpha = map(pressure, 0.0, 0.15, 0.0, 1.0, true);
        
        fill(density * 255, density * 255, density * 255, pointAlpha * 255);
        
        vertex(p.x + nx * w, p.y + ny * w, zDepth, u, 0.0);
        vertex(p.x - nx * w, p.y - ny * w, zDepth, u, 1.0);
    }
    
    if (isDrawing) {
        endShape();
    }
}
"""

start_marker = "const animalShapes = {"
end_marker = "function draw() {"

start_idx = code.find(start_marker)
end_idx = code.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_code = code[:start_idx] + shapesJson + "\n\n" + code[end_idx:]
    with open('index.html', 'w') as f:
        f.write(new_code)
    print("Success Python")
else:
    print("Markers not found")
